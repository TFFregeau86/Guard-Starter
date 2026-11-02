
#!/usr/bin/env python3
"""
Run evaluation scenarios three times each.

Usage:
    python app.py
    python run_eval.py --label before
    python run_eval.py --label after

Tests five acceptance criteria:
    1. False positives on human writing
    2. Different scores for different writing
    3. All three labels are reachable
    4. Appeals are recorded
    5. Invalid input is handled safely
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import config


# Windows console encoding support
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def bodies_for(scenario):
    """Return request bodies for a scenario."""

    if scenario.get("bodies"):
        return list(scenario["bodies"])

    return [
        {
            "text": text,
            "creator_id": f"eval_{scenario['name'][:12]}_{i}"
        }
        for i, text in enumerate(scenario["texts"], 1)
    ]


def describe(body):
    """Create a readable description of submitted input."""

    if (
        set(body) == {"text", "creator_id"}
        and isinstance(body.get("text"), str)
    ):
        text = body["text"]
        return text[:70] if text else "(empty text)"

    return json.dumps(body)[:120]


def submit_request(requests, url, body, timeout):
    """Submit one request and return its response information."""

    try:
        response = requests.post(
            f"{url}/submit",
            json=body,
            timeout=timeout
        )

        try:
            payload = response.json()
        except ValueError:
            payload = {}

        return {
            "status": response.status_code,
            "guess": payload.get("guess"),
            "confidence": payload.get("confidence"),
            "model_score": payload.get("model_score"),
            "style_score": payload.get("style_score"),
            "label": payload.get("label"),
            "content_id": payload.get("content_id"),
            "error": payload.get("error"),
            "sent": describe(body),
        }

    except Exception as exc:
        return {
            "status": None,
            "error": f"{type(exc).__name__}: {exc}",
            "sent": describe(body),
        }


def test_appeal(requests, url, timeout):
    """Test the complete appeal workflow."""

    result = {
        "test": "appeal workflow"
    }

    original = submit_request(
        requests,
        url,
        {
            "text": (
                "I am requesting a review of this submission "
                "because I believe the assessment may be inaccurate."
            ),
            "creator_id": "eval_appeal"
        },
        timeout
    )

    result["original_submission"] = original

    content_id = original.get("content_id")

    if original.get("status") != 200 or not content_id:
        result["appeal_status"] = "not attempted"
        result["passed"] = False
        return result

    try:
        response = requests.post(
            f"{url}/appeal",
            json={
                "content_id": content_id,
                "reasoning": (
                    "I believe this assessment should be reviewed."
                )
            },
            timeout=timeout
        )

        try:
            payload = response.json()
        except ValueError:
            payload = {}

        result["appeal_response"] = {
            "status": response.status_code,
            "body": payload
        }

        audit_response = requests.get(
            f"{url}/log",
            timeout=timeout
        )

        audit_data = audit_response.json()

        matching_entries = [
            entry
            for entry in audit_data.get("entries", [])
            if entry.get("content_id") == content_id
        ]

        result["audit_check"] = {
            "status": audit_response.status_code,
            "entries_found": len(matching_entries),
            "statuses": [
                entry.get("status")
                for entry in matching_entries
            ]
        }

        appeal_recorded = any(
            entry.get("status") == "under_review"
            for entry in matching_entries
        )

        result["passed"] = (
            response.status_code == 200
            and payload.get("status") == "under_review"
            and audit_response.status_code == 200
            and appeal_recorded
        )

    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["passed"] = False

    return result


def test_invalid_json(requests, url, timeout):
    """Send syntactically malformed JSON."""

    try:
        response = requests.post(
            f"{url}/submit",
            data='{"text": "broken", "creator_id": ',
            headers={
                "Content-Type": "application/json"
            },
            timeout=timeout
        )

        try:
            payload = response.json()
        except ValueError:
            payload = {}

        return {
            "test": "malformed JSON",
            "status": response.status_code,
            "body": payload,
            "passed": 400 <= response.status_code < 500
        }

    except Exception as exc:
        return {
            "test": "malformed JSON",
            "error": f"{type(exc).__name__}: {exc}",
            "passed": False
        }


def test_ping(requests, url, timeout):
    """Verify the service remains operational."""

    try:
        response = requests.post(
            f"{url}/ping",
            json={"message": "health check"},
            timeout=timeout
        )

        return {
            "test": "ping after invalid input",
            "status": response.status_code,
            "passed": response.status_code == 200
        }

    except Exception as exc:
        return {
            "test": "ping after invalid input",
            "error": f"{type(exc).__name__}: {exc}",
            "passed": False
        }


def run_scenario(requests, scenario, url, timeout):
    """Run one scenario."""

    name = scenario["name"]

    if scenario.get("criterion") == 4:
        return [test_appeal(requests, url, timeout)]

    results = []

    for body in bodies_for(scenario):
        results.append(
            submit_request(requests, url, body, timeout)
        )

    if scenario.get("criterion") == 5:
        results.append(
            test_invalid_json(requests, url, timeout)
        )

        results.append(
            test_ping(requests, url, timeout)
        )

    return results


def write_report(rows, args):
    """Write the complete evaluation report."""

    config.RESULTS_DIR.mkdir(exist_ok=True)

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")

    label = f"_{args.label}" if args.label else ""

    path = (
        config.RESULTS_DIR /
        f"run_{stamp}{label}.md"
    )

    n = args.trials

    headers = " | ".join(
        f"Run {i}" for i in range(1, n + 1)
    )

    divider = "|".join(["---"] * n)

    lines = [
        f"# Run log — {args.label}" if args.label else "# Run log",
        "",
        "- Produced by: `run_eval.py::main`",
        "- Service: `app.py::submit`",
        f"- {n} trials per criterion",
        f"- {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Fill in Target and Verdict based on criteria.md.",
        "",
        f"| Criterion | Target | {headers} | Verdict |",
        f"|---|---|{divider}|---|",
    ]

    for row in rows:
        scenario = row["scenario"]

        lines.append(
            f"| {scenario.get('criterion')}. "
            f"{scenario['name']} | | "
            + " | ".join([" "] * n)
            + " | |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## What actually came back",
        "",
        "The following sections contain the actual HTTP responses.",
        ""
    ])

    for row in rows:
        lines.extend([
            f"### {row['scenario']['name']}",
            ""
        ])

        for trial_number, results in enumerate(
            row["trials"], 1
        ):
            lines.extend([
                f"**Trial {trial_number}**",
                "",
                "```json",
                json.dumps(results, indent=2),
                "```",
                ""
            ])

    path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Commit the report when you have reviewed it.")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)

    args = parser.parse_args()

    if args.trials < 1:
        parser.error("--trials must be at least 1")

    try:
        import requests
    except ImportError:
        print(
            "requests is not installed. Run: "
            "pip install -r requirements.txt",
            file=sys.stderr
        )
        sys.exit(1)

    try:
        import scenarios
    except ImportError:
        print(
            "scenarios.py was not found.",
            file=sys.stderr
        )
        sys.exit(1)

    problems = scenarios.validate()

    if problems:
        print("scenarios.py has problems:")

        for problem in problems:
            print(f"- {problem}")

        sys.exit(1)

    try:
        response = requests.get(
            f"{args.url}/health",
            timeout=5
        )

        if response.status_code != 200:
            raise RuntimeError("Health check failed.")

    except Exception:
        print(
            f"Nothing answering at {args.url}. "
            "Start it using: python app.py",
            file=sys.stderr
        )
        sys.exit(1)

    rows = []

    for scenario in scenarios.SCENARIOS:
        print(
            f"\n{scenario['name']} "
            f"(criterion {scenario.get('criterion')})"
        )

        trials = []

        for trial in range(1, args.trials + 1):
            results = run_scenario(
                requests,
                scenario,
                args.url,
                args.timeout
            )

            trials.append(results)

            summaries = []

            for result in results:
                if result.get("test") == "appeal workflow":
                    summaries.append(
                        "PASS" if result.get("passed") else "FAIL"
                    )

                elif result.get("test") in (
                    "malformed JSON",
                    "ping after invalid input"
                ):
                    summaries.append(
                        "PASS" if result.get("passed") else "FAIL"
                    )

                else:
                    summaries.append(
                        result.get("guess") or
                        str(result.get("status"))
                    )

            print(
                f"  trial {trial}: {', '.join(summaries)}"
            )

        rows.append({
            "scenario": scenario,
            "trials": trials
        })

    write_report(rows, args)


if __name__ == "__main__":
    main()