
#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Routes:
    POST /ping    — worked example; do not edit
    POST /submit  — submit and score writing
    POST /appeal  — appeal a decision
    GET  /log     — audit log
    GET  /health  — service and model status
"""

import math
import uuid

from flask import Flask, jsonify, request

import audit
import config
import scoring
import stylometry

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────

class _LimiterOff:
    """No-op limiter while rate limiting is disabled."""

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()

if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """Identify the caller for rate limiting."""
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            return get_remote_address()

        creator = payload.get("creator_id")

        return (
            creator
            if isinstance(creator, str) and creator.strip()
            else get_remote_address()
        )

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """Record requests rejected by the rate limiter."""
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            payload = {}

        creator_id = payload.get("creator_id", "unknown")
        if not isinstance(creator_id, str) or not creator_id.strip():
            creator_id = "unknown"

        audit.log_rejection(
            creator_id=creator_id,
            reason="rate_limited",
            limit=str(exc.description),
        )

        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── Worked example: leave /ping alone ─────────────────────────────────────────

@app.post("/ping")
def ping():
    """Receive a JSON message and return it."""
    payload = request.get_json(silent=True) or {}

    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


# ── Health check ──────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    """Report service status and whether the detector model is loaded."""
    import detector

    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": detector._model is not None,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── Submit text ───────────────────────────────────────────────────────────────

@app.post("/submit")
# Enable this decorator in Unit 8 when rate limiting is configured.
# @limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """Validate, score, label, and log a submission."""
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        audit.log_rejection(
            creator_id="unknown",
            reason="invalid_request",
        )
        return jsonify({
            "error": "invalid_request",
            "message": "Send a JSON object.",
        }), 400

    text = payload.get("text")
    creator_id = payload.get("creator_id")

    if not isinstance(text, str) or not text.strip():
        audit.log_rejection(
            creator_id=(
                creator_id.strip()
                if isinstance(creator_id, str) and creator_id.strip()
                else "unknown"
            ),
            reason="invalid_text",
        )
        return jsonify({
            "error": "invalid_text",
            "message": "Text must be a non-empty string.",
        }), 400

    if not isinstance(creator_id, str) or not creator_id.strip():
        audit.log_rejection(
            creator_id="unknown",
            reason="invalid_creator_id",
        )
        return jsonify({
            "error": "invalid_creator_id",
            "message": "creator_id must be a non-empty string.",
        }), 400

    creator_id = creator_id.strip()

    # Reject excessively large input before running the detector.
    if len(text) > 100_000:
        audit.log_rejection(
            creator_id=creator_id,
            reason="text_too_long",
        )
        return jsonify({
            "error": "text_too_long",
            "message": "Text must not exceed 100000 characters.",
        }), 413

    # Run both independent signals.
    import detector

    model_score = float(detector.model_signal(text))
    style_score = float(stylometry.style_signal(text))

    # Validate the signal outputs before combining them.
    if not (
        math.isfinite(model_score)
        and 0.0 <= model_score <= 1.0
        and math.isfinite(style_score)
        and 0.0 <= style_score <= 1.0
    ):
        app.logger.error("A signal returned an invalid score.")
        return jsonify({
            "error": "scoring_error",
            "message": "A scoring signal returned an invalid result.",
        }), 500

    combined_score = float(
        scoring.combine_signals(model_score, style_score)
    )

    if not math.isfinite(combined_score):
        app.logger.error("The combining function returned an invalid score.")
        return jsonify({
            "error": "scoring_error",
            "message": "The combined score is invalid.",
        }), 500

    # Keep the combined score within its documented range.
    combined_score = max(0.0, min(1.0, combined_score))

    guess, label = scoring.score_to_label(combined_score)

    content_id = str(uuid.uuid4())

    # Record the decision and all three scores.
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
        status="decided",
    )

    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "confidence": combined_score,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "text_length": len(text),
    }), 200


# ── Appeal ────────────────────────────────────────────────────────────────────

@app.post("/appeal")
def appeal():
    """Record a writer's appeal and mark the item under review."""
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_request",
            "message": "Send a JSON object.",
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")

    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({
            "error": "invalid_content_id",
            "message": "content_id must be a non-empty string.",
        }), 400

    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({
            "error": "invalid_reasoning",
            "message": "Reasoning must be a non-empty string.",
        }), 400

    content_id = content_id.strip()
    reasoning = reasoning.strip()

    # Only allow appeals for IDs with an original decision.
    entries = audit.entries_for(content_id)
    decisions = [
        entry for entry in entries
        if entry.get("status") == "decided"
        and entry.get("guess") is not None
    ]

    if not decisions:
        return jsonify({
            "error": "content_not_found",
            "message": "No original decision was found for this content_id.",
        }), 404

    original = decisions[0]
    creator_id = original.get("creator_id", "unknown")

    # Append the appeal without deleting the original decision.
    appeal_entry = audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning,
    )

    return jsonify({
        "ok": True,
        "content_id": content_id,
        "status": appeal_entry["status"],
        "message": (
            "Your appeal has been recorded. "
            "This submission is now under review."
        ),
    }), 200


# ── Audit log ────────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """Return audit log entries, optionally limited to recent entries."""
    limit = request.args.get("limit", type=int)

    if limit is not None and limit < 1:
        return jsonify({
            "error": "invalid_limit",
            "message": "limit must be a positive integer.",
        }), 400

    entries = audit.read_entries(limit=limit)

    return jsonify({
        "count": len(entries),
        "entries": entries,
    })


# ── Start the service ─────────────────────────────────────────────────────────

def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(
        "  rate limiting:   "
        f"{'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}"
    )
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()

    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()