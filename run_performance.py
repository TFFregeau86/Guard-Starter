#!/usr/bin/env python3
"""Measure local Flask inference latency, CPU time, and memory."""

import datetime as dt
import json
import statistics
import time
import uuid
from pathlib import Path

import psutil
import requests

BASE_URL = "http://127.0.0.1:5000"
PROJECT_ROOT = Path(__file__).resolve().parent
REQUEST_COUNT = 10

SAMPLES = [
    "Our school library is a quiet place where students can read books, "
    "finish homework, and learn about different subjects. I usually visit "
    "after classes because it helps me concentrate.",

    "Playing sports with friends is a good way to stay active. We practice "
    "together, learn new skills, and encourage one another when a game "
    "becomes difficult.",

    "A community garden gives neighbors an opportunity to grow vegetables "
    "and share useful knowledge. People can work together to keep the area "
    "clean and welcoming.",

    "Learning a language takes time and regular practice. Listening to "
    "conversations, reading short stories, and speaking with other learners "
    "can gradually improve confidence.",

    "Public transportation can make travel easier in busy cities. Buses "
    "and trains allow many people to travel without using separate cars.",

    "A weekend trip does not need an expensive destination. Planning "
    "transportation, packing useful items, and allowing free time can make "
    "a short holiday enjoyable.",

    "Students can benefit from joining a school club. They meet people "
    "with similar interests, develop practical skills, and learn how to "
    "organize activities as a group.",

    "Rainy weather can change outdoor plans, but preparation helps. "
    "Waterproof clothing and a flexible schedule make it easier to "
    "continue enjoying a camping trip.",

    "Regular exercise supports general well-being. Walking, cycling, "
    "and playing team sports are simple activities that can become "
    "part of a weekly routine.",

    "Technology has changed how people communicate and find information. "
    "It is useful, but people should still check whether online information "
    "is accurate and reliable.",
]


def get_processes():
    processes = []

    for p in psutil.process_iter(["pid", "cmdline", "cwd"]):
        try:
            command = p.info.get("cmdline") or []
            cwd = p.info.get("cwd")

            runs_app = any(
                str(arg).replace("\\\\", "/").rsplit("/", 1)[-1].lower()
                == "app.py"
                for arg in command
            )

            if runs_app and cwd and Path(cwd).resolve() == PROJECT_ROOT:
                p.cpu_percent(None)
                processes.append(p)

        except (psutil.NoSuchProcess, psutil.AccessDenied, OSError):
            continue

    if not processes:
        raise SystemExit(
            "No Flask app.py processes found in the project directory. "
            "Start the Flask server first."
        )

    return processes


def process_snapshot(processes):
    cpu_seconds = 0.0
    rss_bytes = 0
    for p in processes:
        try:
            times = p.cpu_times()
            cpu_seconds += times.user + times.system
            rss_bytes += p.memory_info().rss
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return {
        "cpu_seconds": cpu_seconds,
        "rss_bytes": rss_bytes,
    }


def percentile(values, percent):
    ordered = sorted(values)
    if not ordered:
        return None
    index = max(0, min(len(ordered) - 1,
                       int(round((percent / 100) * (len(ordered) - 1)))))
    return ordered[index]


def main():
    health = requests.get(f"{BASE_URL}/health", timeout=10)
    health.raise_for_status()
    if not health.json().get("detector_loaded"):
        raise SystemExit("Detector is not loaded.")

    processes = get_processes()
    before = process_snapshot(processes)
    peak_rss = before["rss_bytes"]
    latencies = []
    results = []

    wall_start = time.perf_counter()

    for index in range(REQUEST_COUNT):
        creator_id = f"performance_{uuid.uuid4().hex}"
        payload = {
            "text": SAMPLES[index],
            "creator_id": creator_id,
        }

        start = time.perf_counter()
        try:
            response = requests.post(
                f"{BASE_URL}/submit",
                json=payload,
                timeout=120,
            )
            elapsed = time.perf_counter() - start
            data = response.json()
            result = {
                "sample": index + 1,
                "status": response.status_code,
                "latency_seconds": round(elapsed, 6),
                "label": data.get("label"),
                "content_id": data.get("content_id"),
                "error": data.get("error"),
            }
        except (requests.RequestException, ValueError) as exc:
            elapsed = time.perf_counter() - start
            result = {
                "sample": index + 1,
                "status": None,
                "latency_seconds": round(elapsed, 6),
                "error": f"{type(exc).__name__}: {exc}",
            }

        latencies.append(elapsed)
        results.append(result)

        snapshot = process_snapshot(processes)
        peak_rss = max(peak_rss, snapshot["rss_bytes"])

        print(
            f"{index + 1:02d}/{REQUEST_COUNT}: "
            f"HTTP {result['status']} "
            f"{elapsed:.3f}s "
            f"label={result.get('label')}"
        )

    wall_seconds = time.perf_counter() - wall_start
    after = process_snapshot(processes)
    peak_rss = max(peak_rss, after["rss_bytes"])
    successful = [r for r in results if r["status"] == 200]
    cpu_delta = max(0.0, after["cpu_seconds"] - before["cpu_seconds"])

    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report = {
        "timestamp": timestamp,
        "server_pids": [p.pid for p in processes],
        "detector_model": health.json().get("detector_model"),
        "requested_submissions": REQUEST_COUNT,
        "successful_responses": len(successful),
        "wall_clock_seconds": wall_seconds,
        "average_latency_seconds": statistics.mean(latencies),
        "median_latency_seconds": statistics.median(latencies),
        "p95_latency_seconds": percentile(latencies, 95),
        "server_cpu_seconds_delta": cpu_delta,
        "server_peak_sampled_rss_mb": peak_rss / (1024 * 1024),
        "server_final_rss_mb": after["rss_bytes"] / (1024 * 1024),
        "cpu_measurement_note": (
            "CPU time is the sum of user and system CPU seconds for "
            "the monitored Flask processes."
        ),
        "energy_measurement_note": (
            "Electrical energy was not directly measured. CPU time and "
            "memory are not substitutes for watt-hours."
        ),
        "results": results,
    }

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    json_path = results_dir / f"performance_{timestamp}.json"
    md_path = results_dir / f"performance_{timestamp}.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# Local Performance Measurement",
        "",
        f"- Date: {timestamp}",
        f"- Model: {report['detector_model']}",
        f"- Successful responses: {len(successful)}/{REQUEST_COUNT}",
        f"- Total wall time: {wall_seconds:.3f} seconds",
        f"- Average latency: {statistics.mean(latencies):.3f} seconds",
        f"- Median latency: {statistics.median(latencies):.3f} seconds",
        f"- Nearest-rank P95 latency: {percentile(latencies, 95):.3f} seconds",
        f"- Server CPU time delta: {cpu_delta:.3f} seconds",
        f"- Peak sampled combined server memory: {peak_rss / (1024 * 1024):.1f} MB",
        f"- Final monitored server memory: {after['rss_bytes'] / (1024 * 1024):.1f} MB",
        "",
        "Electrical energy was not directly measured. CPU time and memory "
        "must not be interpreted as watt-hours.",
        "",
        "| Request | HTTP | Latency (s) | Label |",
        "|---:|---:|---:|---|",
    ]

    for r in results:
        lines.append(
            f"| {r['sample']} | {r['status']} | "
            f"{r['latency_seconds']:.3f} | {r.get('label', 'N/A')} |"
        )

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\nJSON report: {json_path}")
    print(f"Markdown report: {md_path}")
    print(f"Successful responses: {len(successful)}/{REQUEST_COUNT}")


if __name__ == "__main__":
    main()
