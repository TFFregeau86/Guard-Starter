
"""
Signal two: stylistic measurements.

The score is a heuristic, not proof of authorship.
Higher style_signal values mean more AI-like patterns.
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split text into sentences."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, stripping punctuation."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    """
    Return the coefficient of variation of sentence lengths.
    Higher means sentence lengths vary more.
    """
    sentence_list = sentences(text)
    lengths = [len(words(sentence)) for sentence in sentence_list]
    lengths = [length for length in lengths if length > 0]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    return statistics.stdev(lengths) / mean_length


def type_token_ratio(text: str) -> float:
    """
    Return unique words divided by total words.
    Higher means more varied vocabulary.
    """
    word_list = words(text)

    if not word_list:
        return 0.0

    return len(set(word_list)) / len(word_list)


def punctuation_density(text: str) -> float:
    """
    Return punctuation characters divided by all non-whitespace
    characters. The result is between 0 and 1.
    """
    characters = [char for char in text if not char.isspace()]

    if not characters:
        return 0.0

    punctuation_count = sum(
        1 for char in characters
        if not char.isalnum() and char != "_"
    )

    return punctuation_count / len(characters)


def style_signal(text: str) -> float:
    """
    Combine three heuristic measurements into a 0–1 score.
    Higher means more AI-like according to these assumptions.

    Sentence spread: lower variation raises the AI-like component.
    Vocabulary: lower type-token ratio raises the AI-like component.
    Punctuation: density is scaled to 0–1, but its direction is
    only a heuristic and is not reliable evidence of authorship.
    """
    sentence_list = sentences(text)
    word_list = words(text)

    if not word_list:
        return 0.5

    # A single sentence provides no evidence about variation.
    if len(sentence_list) < 2:
        spread_score = 0.5
    else:
        spread = sentence_length_spread(text)
        spread_score = 1.0 / (1.0 + spread)

    # Invert vocabulary variety: lower variety raises this score.
    vocabulary_score = 1.0 - type_token_ratio(text)

    # Scale punctuation density so it contributes on a comparable scale.
    density = punctuation_density(text)
    punctuation_score = min(1.0, density / 0.10)

    score = (
        spread_score
        + vocabulary_score
        + punctuation_score
    ) / 3.0

    return max(0.0, min(1.0, score))


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and "
        "provides good results. Users generally find it easy to use "
        "and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text):.4f}")
    print(f"type_token_ratio         {type_token_ratio(text):.4f}")
    print(f"punctuation_density      {punctuation_density(text):.4f}")
    print(f"style_signal             {style_signal(text):.4f}   (higher = more likely AI)")