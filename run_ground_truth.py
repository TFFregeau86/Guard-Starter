#!/usr/bin/env python3
"""Evaluate Provenance Guard against a provenance-verified CSV dataset."""

import csv
import datetime as dt
import json
import sys
import uuid
from pathlib import Path

import requests

import config

DATASET = Path("results/ground_truth_samples.csv")
RESULTS = Path("results")
BASE_URL = f"http://{config.HOST}:{config.PORT}"


def load_samples():
    if not DATASET.exists():
        raise SystemExit(f"Dataset not found: {DATASET}")

    with DATASET.open("r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if len(rows) != 15:
        raise SystemExit(f"Expected 15 samples; found {len(rows)}.")

    ids = [row["sample_id"] for row in rows]
    if len(set(ids)) != 15:
        raise SystemExit("Duplicate sample IDs found.")

    for row in rows:
        sid = row["sample_id"]
        if row["expected_label"] not in ("human", "ai"):
            raise SystemExit(f"{sid}: invalid expected label.")
        if row["provenance_verified"].strip().lower() != "yes":
            raise SystemExit(f"{sid}: provenance is not verified.")
        if not row["source"].strip():
            raise SystemExit(f"{sid}: source is missing.")
        if not row["text"].strip():
            raise SystemExit(f"{sid}: text is blank.")
        if len(row["text"].split()) < 30:
            raise SystemExit(f"{sid}: text must contain at least 30 words.")

    human = [r for r in rows if r["expected_label"] == "human"]
    ai = [r for r in rows if r["expected_label"] == "ai"]

    if len(human) != 10 or len(ai) != 5:
        raise SystemExit(
            f"Expected 10 human and 5 AI samples; "
            f"found {len(human)} human and {len(ai)} AI."
        )

    return rows


def main():
    samples = load_samples()
    print("Dataset validation passed: 10 human and 5 AI samples.")

    health = requests.get(f"{BASE_URL}/health", timeout=10)
    health.raise_for_status()
    health_data = health.json()

    if not health_data.get("ok") or not health_data.get("detector_loaded"):
        raise SystemExit("Service or detector is not ready.")

    print("Service healthy. Submitting 15 samples...")

    results = []

    for sample in samples:
        creator_id = f"ground_truth_{sample['sample_id']}_{uuid.uuid4().hex[:8]}"

        try:
            response = requests.post(
                f"{BASE_URL}/submit",
                json={
                    "text": sample["text"],
                    "creator_id": creator_id,
                },
                timeout=120,
            )

            try:
                payload = response.json()
            except ValueError:
                payload = {}

            result = {
                "sample_id": sample["sample_id"],
                "expected_label": sample["expected_label"],
                "topic": sample["topic"],
                "source": sample["source"],
                "status": response.status_code,
                "creator_id": creator_id,
                "guess": payload.get("guess"),
                "label": payload.get("label"),
                "combined_score": payload.get("combined_score"),
                "model_score": payload.get("model_score"),
                "style_score": payload.get("style_score"),
                "content_id": payload.get("content_id"),
                "error": payload.get("error"),
            }

        except requests.RequestException as exc:
            result = {
                "sample_id": sample["sample_id"],
                "expected_label": sample["expected_label"],
                "status": None,
                "error": f"{type(exc).__name__}: {exc}",
            }

        results.append(result)
        print(
            f"{sample['sample_id']}: HTTP {result['status']} "
            f"label={result.get('label')} "
            f"score={result.get('combined_score')}"
        )

    successful = [r for r in results if r.get("status") == 200]
    classified = [
        r for r in successful
        if r.get("label") in ("human", "ai")
    ]

    correct = sum(
        r["label"] == r["expected_label"] for r in classified
    )
    unsure = sum(r.get("label") == "unsure" for r in successful)
    overall_accuracy = correct / len(samples)
    classification_coverage = len(classified) / len(successful) if successful else 0

    human_results = [r for r in successful if r["expected_label"] == "human"]
    ai_results = [r for r in successful if r["expected_label"] == "ai"]

    human_ai_labels = sum(r.get("label") == "ai" for r in human_results)
    ai_ai_labels = sum(r.get("label") == "ai" for r in ai_results)

    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    json_path = RESULTS / f"ground_truth_{timestamp}.json"
    md_path = RESULTS / f"ground_truth_{timestamp}.md"

    report = {
        "timestamp": timestamp,
        "dataset": str(DATASET),
        "health": health_data,
        "sample_count": len(samples),
        "successful_responses": len(successful),
        "classified_responses": len(classified),
        "unsure_responses": unsure,
        "correct_classifications": correct,
        "classification_coverage": classification_coverage,
        "accuracy_among_classified": (
            correct / len(classified) if classified else None
        ),
        "overall_accuracy_all_15_samples": overall_accuracy,
        "human_samples_labelled_ai": human_ai_labels,
        "ai_samples_labelled_ai": ai_ai_labels,
        "results": results,
    }

    RESULTS.mkdir(exist_ok=True)
    json_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Ground-Truth Evaluation",
        "",
        f"- Date: {timestamp}",
        f"- Samples: {len(samples)}",
        f"- Successful HTTP responses: {len(successful)}",
        f"- Classified responses: {len(classified)}",
        f"- Unsure responses: {unsure}",
        f"- Classification coverage: {classification_coverage:.1%}",
        f"- Correct classifications: {correct}",
        f"- Overall accuracy (all 15 samples; unsure/errors count as incorrect): "
        f"{overall_accuracy:.1%}",
        f"- Accuracy among classified responses: "
        f"{correct / len(classified):.1%}" if classified else
        "- Accuracy among classified responses: N/A",
        f"- Human samples labelled AI: {human_ai_labels}/{len(human_results)}",
        f"- AI samples labelled AI: {ai_ai_labels}/{len(ai_results)}",
        "",
        "| ID | Expected | Actual | Combined | Model | Style | HTTP |",
        "|---|---|---|---:|---:|---:|---:|",
    ]

    for r in results:
        lines.append(
            f"| {r['sample_id']} | {r['expected_label']} | "
            f"{r.get('label', 'N/A')} | "
            f"{r.get('combined_score', 'N/A')} | "
            f"{r.get('model_score', 'N/A')} | "
            f"{r.get('style_score', 'N/A')} | "
            f"{r.get('status', 'N/A')} |"
        )

    lines.extend([
        "",
        "Accuracy is calculated only among successful responses "
        "with a human or AI label. Unsure responses are not counted "
        "as correct classifications.",
        "",
        "This small dataset is an initial experiment, not proof "
        "that the detector can reliably establish authorship.",
    ])

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\nJSON report: {json_path}")
    print(f"Markdown report: {md_path}")
    print(f"Successful responses: {len(successful)}/15")


if __name__ == "__main__":
    main()
