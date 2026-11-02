
"""
Evaluation scenarios for Provenance Guard.

Run with:
    python run_eval.py --label before
    python run_eval.py --label after
"""

SCENARIOS = [
    {
        "name": "false positives on human writing",
        "criterion": 1,
        "texts": [
            (
                "Last week I had several things to finish, so I tried to "
                "organize my time better. I started with the easiest tasks "
                "because I wanted to make some progress before working on "
                "the difficult ones. I did not finish everything, but I "
                "learned that making a simple plan helps me stay focused."
            ),
            (
                "When I study something new, I usually need time to "
                "understand it. Sometimes I read the instructions more than "
                "once because I miss small details the first time."
            ),
            (
                "Yesterday I went through my notes and realized that I had "
                "forgotten some important details. I decided to review them "
                "again before starting the next assignment."
            ),
            (
                "I usually prefer working in a quiet place because it helps "
                "me concentrate. When there is too much noise, I find it "
                "difficult to remember what I was doing."
            ),
            (
                "This week has been busy because I have several assignments "
                "to complete. I am trying to work on them one at a time "
                "instead of waiting until the last minute."
            ),
            (
                "I made a mistake while completing my assignment today. "
                "At first I did not understand what went wrong, so I checked "
                "my code carefully and tried again."
            ),
            (
                "Sometimes I learn better by watching someone demonstrate "
                "a task. After that, I like to practice it myself so I can "
                "remember the steps."
            ),
            (
                "I planned to finish my work early, but a few things took "
                "longer than expected. I changed my schedule and continued "
                "the remaining tasks the next day."
            ),
            (
                "One thing I have noticed about studying is that taking "
                "short breaks helps me stay focused. I sometimes get tired "
                "when I try to work for too long without stopping."
            ),
            (
                "I enjoy learning new technical skills, although some "
                "instructions can be confusing at first. I usually improve "
                "after trying different solutions and learning from mistakes."
            ),
        ],
    },

    {
        "name": "different scores for different writing",
        "criterion": 2,
        "texts": [
            # Human-written samples: replace or verify these with
            # genuinely human-authored writing before evaluating.

            (
                "Yesterday I planned to finish my work early, but a few "
                "things took longer than I expected. I had to change my "
                "schedule and leave one task for today."
            ),
            (
                "When I first started learning Python, I found loops "
                "confusing. After practicing with a few examples, I began "
                "to understand how they worked."
            ),
            (
                "I prefer doing assignments in the morning because I feel "
                "more focused. In the evening, I sometimes get distracted "
                "and need more time to finish my work."
            ),
            (
                "Last weekend I spent some time organizing my files. "
                "There were many documents in different folders, so I "
                "decided to arrange everything more carefully."
            ),
            (
                "I think planning is useful because it helps people "
                "remember what they need to do. However, plans do not "
                "always work, and sometimes it is better to change them."
            ),

            # AI-generated samples: label these as AI-generated
            # only if their provenance is accurate.

            (
                "Effective time management requires individuals to "
                "establish clear priorities, allocate sufficient time "
                "to important tasks, and regularly evaluate their progress. "
                "Consistent planning can improve productivity."
            ),
            (
                "Artificial intelligence is transforming many industries "
                "by automating repetitive tasks, analyzing large datasets, "
                "and supporting decision-making processes."
            ),
            (
                "A successful cybersecurity strategy combines technical "
                "safeguards, employee awareness, regular monitoring, "
                "and effective incident response procedures."
            ),
            (
                "Environmental sustainability requires coordinated efforts "
                "from individuals, organizations, and governments to "
                "reduce waste and conserve natural resources."
            ),
            (
                "Education plays an essential role in economic and social "
                "development. Access to quality learning opportunities "
                "helps individuals develop knowledge and practical skills."
            ),
        ],
    },

    {
        "name": "all three labels are reachable",
        "criterion": 3,
        "texts": [
            (
                "I went to the store yesterday and bought some groceries. "
                "After returning home, I prepared dinner and watched a movie."
            ),
            (
                "Effective time management requires individuals to "
                "establish clear priorities and evaluate their progress "
                "regularly. Consistent planning improves productivity."
            ),
            (
                "I think learning new skills takes patience. Sometimes "
                "I understand something quickly, but other times I need "
                "to practice several times before it makes sense."
            ),
        ],
    },

    {
        "name": "appeals are recorded",
        "criterion": 4,
        "texts": [
            (
                "I am submitting this text for review because I believe "
                "the automated assessment may not accurately represent "
                "how it was written. Please review the available evidence "
                "before making a final decision."
            ),
        ],
    },

    {
        "name": "invalid input is handled safely",
        "criterion": 5,
        "bodies": [
            # Missing text
            {
                "creator_id": "eval_missing_text"
            },

            # Empty text
            {
                "text": "",
                "creator_id": "eval_empty_text"
            },

            # Whitespace-only text
            {
                "text": "     ",
                "creator_id": "eval_whitespace"
            },

            # Non-string text
            {
                "text": 12345,
                "creator_id": "eval_non_string"
            },

            # Null text
            {
                "text": None,
                "creator_id": "eval_null_text"
            },

            # Missing creator ID
            {
                "text": "This is a test submission."
            },

            # Empty creator ID
            {
                "text": "This is a test submission.",
                "creator_id": ""
            },

            # Null creator ID
            {
                "text": "This is a test submission.",
                "creator_id": None
            },

            # Oversized text
            {
                "text": "word " * 50000,
                "creator_id": "eval_oversized"
            },

            # Invalid JSON is not a JSON object.
            # This dictionary tests a non-object JSON value instead.
            # Actual malformed JSON needs a separate raw HTTP request.
            {
                "text": ["not", "a", "string"],
                "creator_id": "eval_array_text"
            },
        ],
    },
]


def validate():
    """Check scenarios for missing or unfinished test inputs."""
    errors = []

    if not SCENARIOS:
        errors.append("SCENARIOS is empty.")

    for scenario in SCENARIOS:
        name = scenario.get("name", "<unnamed>")

        if scenario.get("bodies"):
            for index, body in enumerate(
                scenario["bodies"], start=1
            ):
                if not isinstance(body, dict):
                    errors.append(
                        f"{name}, body {index}: expected a dictionary."
                    )

        else:
            texts = scenario.get("texts")

            if not isinstance(texts, list) or not texts:
                errors.append(
                    f"{name}: 'texts' must be a non-empty list."
                )
                continue

            for index, sample in enumerate(texts, start=1):
                if sample is not None and not isinstance(sample, str):
                    errors.append(
                        f"{name}, sample {index}: "
                        "expected a string or None."
                    )

                elif (
                    isinstance(sample, str)
                    and sample.startswith("REPLACE")
                ):
                    errors.append(
                        f"{name}, sample {index}: "
                        "unfinished placeholder."
                    )

    return errors


if __name__ == "__main__":
    problems = validate()

    if problems:
        print("Scenario validation failed:")

        for problem in problems:
            print(f"- {problem}")

        raise SystemExit(1)

    print(f"Validated {len(SCENARIOS)} scenarios.")
