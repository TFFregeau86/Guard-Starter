# Provenance Guard

A local Flask web service that examines submitted writing using authorship-related signals, combines the results, assigns a label, and records decisions in an audit log.

**Current progress:** Milestones 3, 4, and 5 are implemented in the current local version. The `/submit` route validates input, calls the GPT-2 detector and style signal, combines their scores, assigns a classification, and records the decision. The `/appeal` endpoint has also been implemented and tested successfully. Unit 8 rate limiting and attack/evaluation evidence have been collected. The before/after evaluation currently shows no measurable change, so the improvement requirement still needs to be completed and verified.

## What This Does

The submission flow is:

1. A caller sends text and a `creator_id` to `POST /submit`.
2. The route checks that the request contains a JSON object.
3. The route validates that `text` and `creator_id` are non-empty strings.
4. The route rejects text exceeding 100,000 characters.
5. The GPT-2 detector calculates the model signal.
6. The stylometry implementation calculates the style signal.
7. The scoring module combines both signals using configured weights.
8. The combined score determines the machine-readable classification and reader-facing label.
9. The service creates a unique `content_id`.
10. The decision is recorded in the audit log.
11. The service returns the scores, classification, label, and submission ID as JSON.

The service also supports health checks, audit-log retrieval, invalid-request logging, and appeals. Rate limiting is configurable for Unit 8.

**Important limitation:** These scores are heuristic indicators of writing patterns, not proof of authorship. Human writing can be incorrectly flagged, and AI-generated writing can receive a human or uncertain classification.

## Signals and Scoring

### Signal One — The Model Signal

**Implementation:** `detector.model_signal(text)`

The local GPT-2 language model estimates how predictable submitted text is and converts that information into a model score.

AI-generated writing can have predictable statistical patterns, but human writing can also be predictable. The score provides evidence about statistical patterns rather than proof of who wrote the text.

The model cannot establish authorship or intent from text alone. Simple writing, second-language writing, short sentences, and other ordinary writing patterns can produce misleading results.

**Status:** Implemented and connected to the submission route.

Verified examples include:

- Model score of `0.2710` for an earlier submission.
- Model score of `0.5093` for the sentence about rain falling on an empty street.
- Model score of `0.7663` for the sentence about walking to the store.

These results demonstrate that the model produces different scores for different inputs.

### Signal Two — The Style Signal

**Implementation:** `stylometry.style_signal(text)`

The style signal measures stylistic properties of submitted text using heuristic measurements, including:

- **Sentence-length spread:** Measures variation in sentence lengths using the coefficient of variation.
- **Type-token ratio:** Measures vocabulary variety by dividing the number of unique words by the total number of words.
- **Punctuation density:** Measures punctuation relative to non-whitespace characters.

These measurements are combined into a score between `0.0` and `1.0`. Higher scores are treated as more AI-like under the project's assumptions.

The style signal does not understand meaning or prove authorship. Editing, quotations, writing ability, typos, and sentence structure can affect its measurements.

**Status:** Implemented and connected to `POST /submit`.

Verified examples include:

- Style score of approximately `0.3064` for an earlier submission.
- Style score of approximately `0.4230` for the rain sentence.
- Style score of approximately `0.5366` for the store sentence.

These results demonstrate that the style signal is producing actual scores rather than always returning the placeholder value of `0.5`.

### The Combining Rule

**Implementation:** `scoring.py::combine_signals`

The service combines the model signal and style signal using a weighted average.

The current configuration in `config.py` specifies:

- Model signal weight: `0.5`
- Style signal weight: `0.5`

The calculation is:

```python
combined_score = (
    (model_weight * model_score + style_weight * style_score)
    / (model_weight + style_weight)
)
```

With equal weights, both signals contribute equally to the combined score.

The implementation validates the signal outputs in the submission route, combines the scores, and keeps the final score within the range `0.0–1.0`.

#### Example: Two Signals Produce Different Scores

An earlier submission produced these results:

- Model score: `0.2710`
- Style score: `0.3064`
- Combined score: approximately `0.2887`

The two signals produced different values, but both were below the human threshold of `0.35`. Their weighted average was also below that threshold.

This demonstrates how the configured combining rule handles different signal values. It does not establish whether the submitted text was actually written by a human.

### Label Variants

**Implementation:** `scoring.py::score_to_label`

The configured thresholds in `config.py` are:

```python
HUMAN_THRESHOLD = 0.35
AI_THRESHOLD = 0.65
```

| Combined score | Machine-readable guess | Reader-facing label |
|---|---|---|
| `0.00–0.35`, inclusive | `human` | This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it. |
| Greater than `0.35` and less than `0.65` | `unsure` | We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI. |
| `0.65–1.00`, inclusive | `ai` | This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it. |

The numeric ranges refer to the combined score. The reader-facing message is returned in the `label` field, while the machine-readable classification is returned in the `guess` field.

**Verification completed:** Running `python scoring.py` displayed the three ranges, tested representative scores of `0.20`, `0.50`, and `0.80`, and printed the signal-combination test. A separate command verified that scores of `0.35` and `0.34` both return the human classification.

The thresholds are configurable and have not been established as optimal through a sufficiently large evaluation dataset. A score in the high-confidence AI range must not be interpreted as definitive proof of AI authorship.

## Sample Runs

### A Submission

Request:

```bash
curl.exe -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"The rain fell softly on the empty street. The windows glowed warmly as evening settled over the town.\",\"creator_id\":\"writer-001\"}"
```

Observed response:

```json
{
  "combined_score": 0.46614423716209413,
  "confidence": 0.46614423716209413,
  "content_id": "e8fa3cca-b691-4711-af46-ba7a1218c1ee",
  "creator_id": "writer-001",
  "guess": "unsure",
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "model_score": 0.5093,
  "style_score": 0.4229884743241883,
  "text_length": 101
}
```

This submission demonstrates that both signals are connected, the scores are combined, the label is assigned, and a unique content ID is returned.

The combined score falls between `0.35` and `0.65`, so the service returns the `unsure` classification.

The `confidence` field currently contains the combined score. It should not be interpreted as a calibrated probability that the classification is correct.

### Another Submission

Request:

```bash
curl.exe -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"I walked to the store. I bought milk and bread. Then I went home.\",\"creator_id\":\"writer-001\"}"
```

Observed result:

```json
{
  "combined_score": 0.6514305450013973,
  "confidence": 0.6514305450013973,
  "content_id": "ec7efae9-ef77-4595-b926-0e61dc7bd9d4",
  "creator_id": "writer-001",
  "guess": "ai",
  "label": "This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it.",
  "model_score": 0.7663,
  "style_score": 0.5365610900027947,
  "text_length": 65
}
```

This submission reached the `ai` classification because its combined score was above the `0.65` threshold. This is an example of the service's classification behavior, not proof that the text was AI-generated.

## Audit Log

**Implementation:** `audit.py`

The audit log records decisions and rejected requests in JSON Lines format, with one JSON object per line.

Request:

```bash
curl.exe "http://127.0.0.1:5000/log?limit=5"
```

The log returns JSON containing recent entries. A successful submission contains the nine required decision fields:

- `timestamp`
- `content_id`
- `creator_id`
- `guess`
- `model_score`
- `style_score`
- `combined_score`
- `label`
- `status`

The initial decision status is `decided`.

Example of a recorded decision:

```json
{
  "combined_score": 0.46614423716209413,
  "content_id": "e8fa3cca-b691-4711-af46-ba7a1218c1ee",
  "creator_id": "writer-001",
  "guess": "unsure",
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "model_score": 0.5093,
  "status": "decided",
  "style_score": 0.4229884743241883,
  "timestamp": "2026-10-25T11:20:11+00:00"
}
```

The audit log also records rejected requests with information such as the creator ID, rejection reason, event type, status, and timestamp.

Verified rejection reasons include:

- `invalid_text`
- `invalid_creator_id`
- `invalid_request`

To find the configured audit-log path, run:

```bash
python -c "import config; print(config.AUDIT_LOG)"
```

The log is append-only during normal decision and appeal operations. The `audit.clear()` utility exists for clearing the log between tests; it should not be used when existing evidence must be preserved.

## Appeals

**Implementation:** `POST /appeal`

The appeal endpoint allows a writer to challenge an existing decision.

The endpoint:

1. Validates that the request is a JSON object.
2. Checks that `content_id` is a non-empty string.
3. Checks that `reasoning` is a non-empty string.
4. Verifies that an original decision exists for the submitted content ID.
5. Records the appeal in the audit log.
6. Returns a successful response with the status `under_review`.

An appeal does not delete or overwrite the original decision. Instead, a separate audit entry records the appeal and its reasoning.

### Example Appeal

Request:

```bash
curl.exe -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d "{\"content_id\":\"e8fa3cca-b691-4711-af46-ba7a1218c1ee\",\"reasoning\":\"I wrote this text myself and would like the decision reviewed.\"}"
```

Observed response:

```json
{
  "content_id": "e8fa3cca-b691-4711-af46-ba7a1218c1ee",
  "message": "Your appeal has been recorded. This submission is now under review.",
  "ok": true,
  "status": "under_review"
}
```

This confirms that the appeal endpoint successfully accepted an appeal for an existing content ID.

The audit log records a separate entry containing:

- The original `content_id`
- The associated `creator_id`
- `event: "appeal"`
- The appeal reasoning
- `status: "under_review"`

An appeal submitted for a nonexistent content ID returns a 404 response. An earlier test using a placeholder content ID verified that behavior.

The endpoint records an appeal and its review status. It does not independently determine whether the original classification was correct.

## Current Verification

### Verified So Far

- `POST /ping` returns HTTP 200 and the expected JSON response.
- `GET /health` returns the service status.
- `POST /submit` validates request data.
- Missing or invalid submission fields are rejected.
- Whitespace-only text returns HTTP 400 with `invalid_text`.
- Missing `creator_id` returns HTTP 400 with `invalid_creator_id`.
- Invalid JSON returns HTTP 400 with `invalid_request`.
- The GPT-2 detector returns a model score.
- `stylometry.style_signal(text)` returns a style score.
- `scoring.combine_signals()` combines the two signals.
- `scoring.score_to_label()` returns a classification and reader-facing message.
- The configured label ranges print correctly.
- The boundary scores `0.34` and `0.35` return the human classification.
- A successful submission receives a unique `content_id`.
- The audit writer records decisions with all nine required fields.
- `GET /log` returns recorded decisions and rejected requests.
- An appeal for an existing content ID returns HTTP 200 and records `under_review`.
- An appeal for a nonexistent content ID is rejected with HTTP 404.
- The audit log contains the appeal event alongside the original decision.
- The environment check passes all nine checks when run inside the activated virtual environment.

### Acceptance Criteria Still Requiring Systematic Evaluation

The following tests must be completed and documented before claiming that all evaluation criteria have passed.

#### False positives on human writing

Submit ten pieces of writing known to be human-written. The target is for no more than one to receive the high-confidence AI classification.

#### Score separation

Submit five human-written samples and five AI-generated samples. Calculate the mean combined score for each group. The target is for the AI-generated group to have an average at least `0.15` higher than the human-written group.

#### All three classifications are reachable

Verify that actual submissions receive each classification:

- `human`
- `unsure`
- `ai`

The scoring tests demonstrate that the three classification branches are available. The observed submission results already include `unsure` and `ai`. A new successful submission with a human result should be recorded to complete this particular verification.

#### Appeals are recorded

Verify that a valid appeal for an existing content ID returns success, creates an audit entry, and records `under_review`. Also verify that nonexistent content IDs are rejected.

The basic successful and nonexistent-ID cases have already been tested. Preserve the corresponding evidence in the audit log.

#### Invalid input is handled safely

Run ten invalid-input tests covering missing text, empty text, whitespace-only text, non-string text, missing creator IDs, invalid JSON, and other relevant malformed requests.

Verify that each request returns an appropriate 4xx response without crashing the service. Then confirm that `POST /ping` still returns HTTP 200.

Several invalid-input cases have already passed, but the complete ten-case evaluation has not yet been documented.

These acceptance criteria are evaluation targets, not results that can be claimed solely from implementing the routes.

## Unit 8 — Rate Limiting

### Configuration

- Per-minute limit: 10 submissions per creator.
- Per-day limit: 200 submissions per creator.
- Storage: In-memory (`memory://`).

### Why These Limits?

The limit of 10 submissions per minute allows a writer to submit several pieces without being unnecessarily restricted, while stopping scripts that rapidly submit variations to probe the detector's thresholds. The daily limit of 200 permits normal testing while placing a cap on repeated submissions. These are development limits, not production-tested values.

### Flood Test

Command:

```bash
python run_attacks.py --flood 15
```

Results from October 25, 2026:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Result: 10 submissions succeeded, and 5 were rejected with HTTP 429 (Too Many Requests). The rate limiter is working as intended for this test.

Output file: `results/flood_2026-10-25_1854.md`

**Limitation:** The limiter uses in-memory storage, so its counters reset when the service restarts. It is suitable for local development but would need shared, persistent storage for a multi-instance production service.

## Unit 8 — Attack Evaluation

### Before Run

Attack report: `results/attack_run_2026-10-25_1922_before.md`

The practice attack set contained six cases:

| ID | Family | Observed result | Interpretation |
|---|---|---|---|
| FP01 | `false_positive` | HTTP 200, `unsure`, score approximately `0.584` | The service did not return an AI classification for this case. |
| EV01 | `evasion` | HTTP 200, `unsure`, score approximately `0.577` | The service did not return a human classification for this case. |
| PI01 | `prompt_injection` | HTTP 200, `unsure`, score approximately `0.355` | The response was uncertain; this alone does not prove prompt-injection resistance. |
| MR01 | `malformed` | HTTP 400 | The malformed request was rejected. |
| EV02 | `evasion` | HTTP 200, `unsure`, score approximately `0.432` | The service did not return a human classification for this case. |
| FP02 | `false_positive` | HTTP 200, `unsure`, score approximately `0.569` | The service did not return an AI classification for this case. |

The five valid requests returned `unsure`, and the malformed request returned HTTP 400. The report's verdicts should be assessed against the assignment's precise definitions of `HELD` and `BROKE`. An `unsure` response is not proof that authorship was identified correctly.

### After Run

Attack report: `results/attack_run_2026-10-25_1935_after.md`

The same six cases were run again. The observed results were:

| ID | Observed result |
|---|---|
| FP01 | HTTP 200, `unsure` |
| EV01 | HTTP 200, `unsure` |
| PI01 | HTTP 200, `unsure` |
| MR01 | HTTP 400 |
| EV02 | HTTP 200, `unsure` |
| FP02 | HTTP 200, `unsure` |

### Before/After Evaluation

| Evaluation | Before report | After report | Observation |
|---|---|---|---|
| Attack set | `attack_run_2026-10-25_1922_before.md` | `attack_run_2026-10-25_1935_after.md` | Same reported classifications and HTTP statuses. |
| Scenario evaluation | `run_2026-10-25_1928_before.md` | `run_2026-10-25_1935_after.md` | The displayed results are unchanged across the five scenarios. |

**Current conclusion:** The tests ran successfully, but the available output does not demonstrate a measurable improvement between the before and after runs. The `after` run should not be described as a successful improvement until a specific code change is made and its effect is demonstrated through testing.

### Scenario Evaluation Details

The evaluation script ran three trials for each of five scenarios:

| Scenario | Observed result | Limitation |
|---|---|---|
| My own writing | All displayed classifications were `unsure` | The samples must genuinely represent the intended human-writing test group. |
| Label coverage | All displayed classifications were `unsure` | The results do not demonstrate all three classifications with the selected samples. |
| Bad input | Outputs displayed as `—` | Confirm the report or application responses show that each input was safely rejected. |
| Prompt injection resistance | `human`, `unsure` across the displayed samples | The outputs are unchanged between runs and do not establish complete resistance. |
| Appeal path | `unsure` | This scenario alone does not verify the actual appeal endpoint and audit event. |

After report: `results/run_2026-10-25_1935_after.md`

The evaluation scenarios are useful for repeatable testing, but their outputs should be checked against the actual acceptance criteria. In particular, an appeal workflow should be tested by submitting a real existing `content_id` to `POST /appeal` and confirming the resulting audit entry.

## Audit Evidence for Unit 8

The attack reports include content IDs for the five accepted submissions. Those IDs can be used to locate their corresponding decisions in the audit log.

Refresh the audit extract after running the tests:

```bash
curl "http://127.0.0.1:5000/log?limit=200" > results/audit_extract.json
```

The assignment asks for at least ten audit entries in the README. Select actual entries from the audit extract, including a rejected request if one is present, and preserve the original values. Do not invent audit records or claim that the extract contains ten distinct relevant entries without checking it.

Useful identifiers from the before attack run include:

- FP01: `dc39f731-9e4f-49d6-8833-7d4ec03039c0`
- EV01: `3968b8a6-04ef-4547-afd8-91af5a7c29e1`
- PI01: `316262bc-a163-4bcd-a8f2-97a8609313cd`
- EV02: `df45f902-53eb-4149-b843-48701b909e17`
- FP02: `50e80379-3576-4b59-9282-fdb5f55f6bb4`

The audit log records decisions and rejection events. A response's `unsure` classification means the service could not confidently distinguish the writing patterns; it should not be treated as proof of authorship.

## How I Used AI

### Moment 1 — Diagnosing Flask Routes

**What I asked for:** Help testing the Flask routes and diagnosing connection resets.

**What came back:** A sequence of checks for `/health`, `/ping`, and the detector.

**What I changed:** Tested the detector directly and confirmed it returned a score independently of Flask.

### Moment 2 — Implementing Submission Logging

**What I asked for:** Help implementing submission logging.

**What came back:** Guidance for calling `audit.log_decision()` and checking the log.

**What I changed:** Added the logging call to the submission route and verified that real submissions appeared in `/log`.

### Moment 3 — Implementing Scoring and Appeals

**What I asked for:** Help implementing the style signal, score-combination rule, label thresholds, and appeal workflow.

**What came back:** Guidance for combining the model and style scores, returning reader-facing labels, and recording appeals.

**What I changed:** Implemented the style signal and scoring functions, connected them to `/submit`, configured the weights and thresholds, and tested the appeal endpoint against an existing content ID.

### Moment 4 — Unit 8 Rate Limiting and Evaluation

**What I asked for:** Help collecting rate-limit evidence, running the attack set, creating evaluation scenarios, and interpreting the before/after results.

**What came back:** Commands for running the flood test, exporting audit records, running attack and scenario evaluations, and documenting the results.

**What I changed:** Ran the six-case attack set and five scenario evaluations, preserved the reports, and documented the current findings. The displayed before/after outputs were unchanged, so an improvement that produces a demonstrable difference remains to be completed.

## Running the Project

See `RUNNING.md` for installation, setup, and command instructions.

Activate the virtual environment before running the project. In Git Bash:

```bash
source .venv/Scripts/activate
```

Run the environment check:

```bash
python test.py
```

The latest environment check passed all nine checks, including Python version, virtual environment, pinned packages, PyTorch, Flask, detector model, and service availability.

Start the service:

```bash
python app.py
```

The default address is:

```text
http://127.0.0.1:5000
```

Run requests from a second terminal while Flask is running.