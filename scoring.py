
"""
Combine the model and style signals, then produce a reader-facing label.

Higher scores indicate writing patterns more associated with AI.
These heuristic scores are not proof of authorship.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals using a weighted average.

    The configured weights should add up to 1.0.
    Higher scores indicate more AI-like patterns.
    """
    model_score = max(0.0, min(1.0, float(model_score)))
    style_score = max(0.0, min(1.0, float(style_score)))

    total_weight = (
        config.WEIGHT_MODEL_SIGNAL
        + config.WEIGHT_STYLE_SIGNAL
    )

    if total_weight <= 0:
        raise ValueError("Signal weights must have a positive sum.")

    combined_score = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    ) / total_weight

    return max(0.0, min(1.0, combined_score))


def score_to_label(score: float) -> tuple[str, str]:
    """
    Convert a combined score into a machine-readable guess
    and a full sentence for the reader.

    Scores at or below HUMAN_THRESHOLD are labeled human.
    Scores at or above AI_THRESHOLD are labeled ai.
    Scores between the thresholds are labeled unsure.
    """
    score = max(0.0, min(1.0, float(score)))

    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "This text has patterns often associated with AI-generated "
            "writing, but this result does not prove who wrote it."
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "This text has patterns often associated with human writing. "
            "Automated analysis cannot confirm who wrote it."
        )

    return (
        "unsure",
        "We couldn't confidently distinguish the writing patterns. "
        "This result is uncertain and should not be treated as proof "
        "that the text was written by AI."
    )


def label_ranges() -> list[tuple[str, str]]:
    """Return the configured score range for each label."""
    return [
        (
            "high-confidence human",
            f"0.00 – {config.HUMAN_THRESHOLD:.2f} (inclusive)",
        ),
        (
            "unsure",
            f"greater than {config.HUMAN_THRESHOLD:.2f} "
            f"and less than {config.AI_THRESHOLD:.2f}",
        ),
        (
            "high-confidence AI",
            f"{config.AI_THRESHOLD:.2f} – 1.00 (inclusive)",
        ),
    ]


if __name__ == "__main__":
    print("Label ranges:")
    for name, score_range in label_ranges():
        print(f"{name}: {score_range}")

    print("\nLabel tests:")
    for score in (0.20, 0.50, 0.80):
        guess, label = score_to_label(score)
        print(f"{score:.2f} -> {guess}: {label}")

    print("\nSignal combination test:")
    print(f"Combined score: {combine_signals(0.20, 0.80):.3f}")