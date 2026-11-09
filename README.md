# Provenance Guard

A local Flask web service that examines submitted writing using authorship-related signals, combines the results, assigns a classification, and records decisions in an audit log.

**Current progress:** The core service, scoring pipeline, audit logging, appeal endpoint, and Unit 8 rate limiting are implemented. The service has been tested with a 72-sample evaluation, a dedicated flood test, and a 56-case attack suite.

A measurable input-handling improvement was implemented and verified on November 9, 2026. All five operational capstone acceptance criteria are documented as passing. Evaluation against known human- and AI-written samples and a measurable improvement to detector-classification performance remain outstanding. Local CPU and memory measurements have been recorded; direct energy and financial cost measurement remain outstanding.

---

## 1. What This Extends

Provenance Guard is a local Flask application that evaluates submitted writing using two signals:

- A GPT-2-based model signal.
- A heuristic stylometry signal.

The submission flow is:

1. A caller sends text and a `creator_id` to `POST /submit`.
2. The route checks that the request contains a JSON object.
3. The route validates that `text` and `creator_id` are non-empty strings.
4. The route rejects text exceeding 10,000 characters.
5. The GPT-2 detector calculates the model signal.
6. The stylometry implementation calculates the style signal.
7. The scoring module combines both signals using configured weights.
8. The combined score determines the machine-readable classification and reader-facing label.
9. The service creates a unique `content_id`.
10. The decision is recorded in the audit log.
11. The service returns the scores, classification, label, and submission ID as JSON.

The service also supports health checks, audit-log retrieval, invalid-request logging, appeals, and configurable rate limiting.

**Important limitation:** These scores are heuristic indicators of writing patterns, not proof of authorship. Human writing can be incorrectly flagged, and AI-generated writing can receive a human or uncertain classification.

## 2. The Shape: Signals and Scoring

### Signal One — The Model Signal

**Implementation:** `detector.model_signal(text)`

The local GPT-2 language model estimates how predictable submitted text is and converts that information into a model score.

AI-generated writing can have predictable statistical patterns, but human writing can also be predictable. The score provides evidence about statistical patterns rather than proof of who wrote the text.

The model cannot establish authorship or intent from text alone. Simple writing, second-language writing, short sentences, and other ordinary writing patterns can produce misleading results.

**Status:** Implemented and connected to the submission route.

Verified examples from earlier submissions include:

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

Verified examples from earlier submissions include:

- Style score of approximately `0.3064` for an earlier submission.
- Style score of approximately `0.4230` for the rain sentence.
- Style score of approximately `0.5366` for the store sentence.

These results demonstrate that the style signal produces actual scores rather than always returning a placeholder value of `0.5`.

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

**Example: Two Signals Produce Different Scores**

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
| 0.00–0.35, inclusive | `human` | This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it. |
| Greater than 0.35 and less than 0.65 | `unsure` | We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI. |
| 0.65–1.00, inclusive | `ai` | This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it. |

The numeric ranges refer to the combined score. The reader-facing message is returned in the `label` field, while the machine-readable classification is returned in the `guess` field.

The implementation also returns the combined score in the `confidence` field. This is a numeric heuristic score, not a calibrated probability that the classification is correct.

**Verification completed:** Running `python scoring.py` displayed the three ranges, tested representative scores of `0.20`, `0.50`, and `0.80`, and printed the signal-combination test. A separate command verified that scores of `0.35` and `0.34` both return the human classification.

The thresholds are configurable and have not been established as optimal through a sufficiently large evaluation dataset. A score in the high-confidence AI range must not be interpreted as definitive proof of AI authorship.

## 3. Running It and Sample Runs

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

### Another Submission

Request:

```bash
curl.exe -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"I walked to the store. I bought milk and bread. Then I went home.\",\"creator_id\":\"writer-001\"}"
```

Observed response:

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

### Latest 72-Sample Evaluation

**Evaluation file:** `results/run_2026-11-02_1155_after.md`

A separate evaluation included 72 submissions. PowerShell was used to extract the individual scores and calculate their averages, minimums, and maximums.

**Individual Signal Results**

| Measurement | Average | Minimum | Maximum |
|---|---:|---:|---:|
| Model score | 0.6651 | 0.1452 | 0.8705 |
| Style score | 0.3569 | 0.2292 | 0.4687 |

The model signal produced a noticeably higher average than the style signal.

This suggests that the two heuristic signals respond differently to the tested writing samples.

**Combined Score Results**

The combined score was returned by the API in the `confidence` field. The average was calculated from the 72 confidence values.

PowerShell command:

```powershell
$path = "results/run_2026-11-02_1155_after.md"

$combined = Select-String -Path $path `
    -Pattern '"confidence":\s*([0-9.]+)' |
    ForEach-Object {
        [double]$_.Matches[0].Groups[1].Value
    }

$combined | Measure-Object -Average -Minimum -Maximum
```

Observed results:

| Measurement | Result |
|---|---:|
| Number of submissions | 72 |
| Average combined score | 0.5110 |
| Minimum combined score | 0.2053 |
| Maximum combined score | 0.6376 |

The average combined score was approximately `0.5110`, which falls inside the `unsure` classification range.

**Classification Distribution**

The classification counts were extracted from the same report:

```powershell
Select-String `
    -Path $path `
    -Pattern '"guess": "ai"|"guess": "human"|"guess": "unsure"' |
    ForEach-Object {
        if ($_.Line -match '"guess": "([^"]+)"') {
            $Matches[1]
        }
    } |
    Group-Object |
    Select-Object Name, Count
```

Observed results:

| Classification | Count | Percentage |
|---|---:|---:|
| human | 6 | 8.33% |
| unsure | 66 | 91.67% |
| ai | 0 | 0.00% |
| **Total** | **72** | **100%** |

**Interpretation**

The highest observed combined score was approximately `0.6376`, below the configured AI threshold of `0.65`. Consequently, none of these 72 submissions received an AI classification.

The results indicate that the current configuration is conservative for this particular test set. However, they do not establish detector accuracy because the ground-truth authorship labels for the 72 submissions have not been systematically compared with the predicted classifications.

The relatively high model scores and lower style scores also demonstrate that the two signals contribute differently to the combined result.

The results should be used as experimental evidence rather than proof that the detector can reliably distinguish human and AI-generated writing.

## 4. Instrumentation

### Audit Log

**Implementation:** `audit.py`

The audit log records decisions and rejected requests in JSON Lines format, with one JSON object per line.

Request:

```bash
curl.exe "http://127.0.0.1:5000/log?limit=5"
```

The log returns JSON containing recent entries.

A successful submission contains the nine decision fields:

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

Verified rejection reasons from the project's tests include:

- `invalid_text`
- `invalid_creator_id`
- `invalid_request`
- `missing_or_empty_text`
- `missing_creator_id`
- `text_too_short`
- `text_too_long`
- `invalid_json`
- `rate_limited`

To find the configured audit-log path, run:

```bash
python -c "import config; print(config.AUDIT_LOG)"
```

The log is append-only during normal decision and appeal operations. The `audit.clear()` utility exists for clearing the log between tests; it should not be used when existing evidence must be preserved.

### Selected Audit Evidence

The following examples are from the November 9 attack testing and related verification runs. They are selected fields from actual audit events; the complete records, including timestamps and other available fields, are preserved in the audit files.

**1. Evasion test — EV01**

```json
{
  "creator_id": "attacker_EV01",
  "guess": "human",
  "combined_score": 0.27884523026890057,
  "status": "decided"
}
```

**2. Evasion test — EV10**

```json
{
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "combined_score": 0.7331687267332978,
  "status": "decided"
}
```

**3. False-positive test — FP07**

```json
{
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "combined_score": 0.6816354162608713,
  "status": "decided"
}
```

FP07 is an important failure because the test was designed as a false-positive case, but the detector classified it as AI.

**4. Prompt-injection test — PI02**

```json
{
  "creator_id": "attacker_PI02",
  "guess": "human",
  "combined_score": 0.27002910624218573,
  "status": "decided"
}
```

**5. Empty input — MF01**

```json
{
  "creator_id": "attacker_MF01",
  "event": "rejected",
  "reason": "missing_or_empty_text",
  "status": "rejected"
}
```

**6. Short input — MF02**

```json
{
  "creator_id": "attacker_MF02",
  "event": "rejected",
  "reason": "text_too_short",
  "status": "rejected"
}
```

**7. Oversized input — MF08**

```json
{
  "creator_id": "attacker_MF08",
  "event": "rejected",
  "reason": "text_too_long",
  "status": "rejected"
}
```

**8. Missing creator ID**

```json
{
  "creator_id": "unknown",
  "event": "rejected",
  "reason": "missing_creator_id",
  "status": "rejected"
}
```

**9. Invalid JSON**

```json
{
  "creator_id": "unknown",
  "event": "rejected",
  "reason": "invalid_json",
  "status": "rejected"
}
```

**10. Rate-limit rejection**

```json
{
  "creator_id": "attacker_flood",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected"
}
```

The `attacker_flood` entry came from the attack-suite flood cases. The separate dedicated flood test used `flood_tester`, as documented below.

These entries demonstrate that the service records both successful classifications and rejected requests. The log also makes it possible to investigate false positives and identify requests that trigger input validation or rate limits.

The complete extracted log is saved in:

`results/audit_extract.json`

The November 9 final extraction was 76,421 bytes.

### Latest Rate-Limit Audit Evidence

On November 9, 2026, I ran a 15-submission flood test using the same creator ID, `flood_tester`.

I checked the audit log using:

```bash
curl "http://127.0.0.1:5000/log?limit=20"
```

The returned log contained ten accepted decision entries and five rejected entries for `flood_tester`.

Each of the five rejected entries included:

```json
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected"
}
```

All five rate-limit rejections were visible in the audit log.

The extracted dedicated flood evidence is saved in:

`results/flood_audit_evidence.json`

This confirms that rejected requests are recorded in the audit log, rather than only being returned as HTTP 429 responses.

## 5. What It Costs

The current implementation uses a local GPT-2 model and in-memory rate-limit storage.

The GPT-2 model runs locally rather than through a paid hosted inference API. Therefore, model inference does not incur a per-request hosted API charge in the current configuration.

The service still uses local computing resources, including CPU or GPU time, memory, and storage.

**Configuration**

- Per-minute limit: 10 submissions per creator.
- Per-day limit: 200 submissions per creator.
- Storage: In-memory (`memory://`).

Rate limits are applied per `creator_id` when a valid creator ID is supplied. Requests without a valid creator ID fall back to the caller's IP address.

These are development limits, not production-tested values.

The in-memory storage is suitable for local development but would need shared, persistent storage for a multi-instance production service.

### Measured Response Time — November 9, 2026

I measured 10 consecutive submissions to the local `/submit` endpoint using Python's `time.perf_counter()` and the `requests` library.

| Measurement | Result |
|---|---:|
| Successful submissions | 10/10 |
| Total elapsed time | 11.0212 seconds |
| Average including model loading | 1.1021 seconds |
| First run (cold start) | 10.1557 seconds |
| Average for runs 2–10 | 0.0962 seconds |

All 10 requests returned HTTP 200.

The first request took considerably longer because the model was loaded during that request. Subsequent requests were much faster.

The measurements include HTTP request overhead, application processing, and model inference. They represent wall-clock response time, not pure CPU time.

### Additional CPU and Memory Measurement — November 9, 2026

The final corrected local test sent 10 submissions to `/submit` while monitoring the Flask processes discovered in the project directory with `psutil`. Each request used a unique `creator_id` to avoid per-user rate-limit interference. The results are saved in `results/performance_2026-11-09_201615.md` and its matching JSON file.

| Measurement | Result |
|---|---:|
| Successful submissions | 10/10 |
| Total wall-clock time | 0.948 seconds |
| Average latency, all 10 requests | 0.094 seconds |
| Median latency | 0.090 seconds |
| Nearest-rank P95 latency | 0.110 seconds |
| Aggregate Flask CPU time during test | 12.672 seconds |
| Peak sampled summed process RSS | 1,910.1 MB |
| Final summed process RSS | 1,909.9 MB |

CPU time is the sum of user and system CPU seconds for the monitored Flask processes. It can exceed wall-clock time when work runs across multiple CPU cores. Memory is the sampled sum of the processes' resident-set sizes (RSS). Summing RSS can count shared memory pages more than once, so it is not a measure of unique physical memory consumption. The peak is based on periodic samples, not continuous monitoring.

This was a small, local, sequential test. It is not a production load test. The earlier response-time and CPU/memory experiments are separate runs and should not be directly combined with these measurements.

Electrical energy was not directly measured. CPU time and memory are resource measurements, not watt-hours. A direct energy or financial cost estimate would require reliable power-consumption data and the applicable electricity rate.

### Estimated Workload for 100 Users per Day

Assuming each of the 100 users makes one submission:

- Using the warm average: 100 × 0.0962 = 9.62 seconds.
- Using the cold-start-inclusive average: 100 × 1.1021 = 110.21 seconds.

These are estimated cumulative response times, not guaranteed processing times for simultaneous users.

### Financial Cost Limitation

A complete financial cost-per-run estimate has not yet been established. Calculating electricity cost would require measuring hardware power consumption and applying the local electricity rate.

No measured dollar amount is claimed. The current implementation has no per-request hosted inference API charge, but local computing still consumes electricity and hardware resources.

## 6. Run Log and Verdicts

### Appeals

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

**Verified November 9 Appeal Test**

The test first submitted writing and received this content ID:

`670e93bc-13da-4821-ba5e-5dad33a80e30`

The appeal request was:

```bash
curl -i -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"670e93bc-13da-4821-ba5e-5dad33a80e30","reasoning":"I wrote this text myself based on my personal camping experience. I would like the decision reviewed."}'
```

Observed response:

```json
{
  "content_id": "670e93bc-13da-4821-ba5e-5dad33a80e30",
  "message": "Your appeal has been recorded. This submission is now under review.",
  "ok": true,
  "status": "under_review"
}
```

The audit log showed the original decision and the separate appeal event using the same content ID:

- Original decision: `decided`
- Appeal event: `appeal`
- Appeal status: `under_review`

This confirms that the appeal was appended without deleting the original decision.

An earlier test using a nonexistent placeholder content ID returned HTTP 404.

The endpoint records an appeal and its review status. It does not independently determine whether the original classification was correct.

### Current Verification

**Verified So Far**

- `POST /ping` returns HTTP 200 and the expected JSON response.
- `GET /health` returns the service status.
- `POST /submit` validates request data.
- Missing or invalid submission fields are rejected.
- Whitespace-only text returns HTTP 400 with `invalid_text` in earlier validation tests.
- Missing `creator_id` returns HTTP 400 with `invalid_creator_id` in earlier validation tests.
- Invalid JSON returns HTTP 400 with `invalid_request` or `invalid_json`, depending on the tested request path.
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
- The environment check passed all nine checks in an earlier run inside the activated virtual environment.
- The 72-sample evaluation produced 72 model scores, 72 style scores, and 72 combined scores.
- The November 9 dedicated flood test produced ten HTTP 200 responses followed by five HTTP 429 responses.
- All five dedicated flood rejections were verified in the audit log.
- The November 9 final 56-case attack suite completed with zero automatically marked BROKE cases.
- The final attack suite verified the MF02 input-handling fix with an HTTP 400 response.
- The final attack suite also exercised malformed requests, oversized input, and flood cases.

### Detector Classification Evaluation Still Outstanding

The operational acceptance criteria are documented as passing in the November 9 capstone tests. The following classification-performance evaluations still require known ground-truth samples.

**1. False Positives on Human Writing**

Submit ten pieces of writing known to be human-written.

The target is for no more than one to receive the high-confidence AI classification. Record the actual authorship and predicted classification for every sample.

**2. Score Separation**

Submit five human-written samples and five AI-generated samples.

Calculate the mean combined score for each group. The target is for the AI-generated group to have an average at least `0.15` higher than the human-written group.

The existing 72-sample evaluation does not satisfy this requirement because its ground-truth authorship labels have not been systematically established.

The separate requirement to demonstrate a measurable before/after improvement to detector-classification performance is documented in Section 7.

### Unit 8 — Rate Limiting

**Configuration**

- Per-minute limit: 10 submissions per creator.
- Per-day limit: 200 submissions per creator.
- Storage: In-memory (`memory://`).

**Why These Limits?**

The limit of 10 submissions per minute allows a writer to submit several pieces without being unnecessarily restricted, while stopping scripts that rapidly submit variations to probe the detector's thresholds.

The daily limit of 200 permits normal testing while placing a cap on repeated submissions.

These are development limits, not production-tested values.

**Flood Test — October 25, 2026**

Command:

```bash
python run_attacks.py --flood 15
```

Earlier results:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Output file:

`results/flood_2026-10-25_1854.md`

**Latest Dedicated Flood Test — November 9, 2026**

Command:

```bash
python run_attacks.py --flood 15
```

Actual output:

```text
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

[ 1/15] 200
[ 2/15] 200
[ 3/15] 200
[ 4/15] 200
[ 5/15] 200
[ 6/15] 200
[ 7/15] 200
[ 8/15] 200
[ 9/15] 200
[10/15] 200
[11/15] 429
[12/15] 429
[13/15] 429
[14/15] 429
[15/15] 429
```

Summary:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429

5 of 15 were rate limited.
```

Output file:

`results/flood_2026-11-09_1130.md`

**Result:** Ten submissions succeeded, and five were rejected with HTTP 429 (Too Many Requests).

The latest `/health` check during subsequent verification returned:

```json
{
  "detector_loaded": true,
  "detector_model": "gpt2",
  "log_entries": 553,
  "ok": true,
  "rate_limiting": true
}
```

This is the observed health response from the November 9 regression testing, not the earlier pre-loading health result.

**Audit Verification**

The audit log was checked after the dedicated flood test:

```bash
curl "http://127.0.0.1:5000/log?limit=20"
```

The returned entries included five rejected requests with:

- `creator_id`: `flood_tester`
- `event`: `rejected`
- `reason`: `rate_limited`
- `status`: `rejected`
- `limit`: `10 per 1 minute`

**Conclusion:** The rate limiter correctly enforced the configured per-minute limit during the test, and the service recorded the rejected requests in its audit log.

**Limitation:** The limiter uses in-memory storage, so its counters reset when the service restarts. It is suitable for local development but would need shared, persistent storage for a multi-instance production service.

### Unit 8 — Attack Evaluation

The attack set is used to test how the service responds to false-positive attempts, evasion, prompt injection, malformed inputs, and repeated submissions.

The preview command:

```bash
python run_attacks.py --set . --show
```

successfully displayed 56 attacks without sending them or writing a report.

The 56 cases include:

- Evasion cases.
- False-positive cases.
- Prompt-injection cases.
- Malformed text cases.
- Malformed request cases.
- Repeated-submission flood cases.

The preview is not itself an attack-test result because no requests were sent.

**Earlier Before Run**

Attack report:

`results/attack_run_2026-10-25_1922_before.md`

The earlier practice attack set contained six cases:

| ID | Family | Observed result | Interpretation |
|---|---|---|---|
| FP01 | false_positive | HTTP 200, unsure, score approximately 0.584 | The service did not return an AI classification for this case. |
| EV01 | evasion | HTTP 200, unsure, score approximately 0.577 | The service did not return a human classification for this case. |
| PI01 | prompt_injection | HTTP 200, unsure, score approximately 0.355 | The response was uncertain; this alone does not prove prompt-injection resistance. |
| MR01 | malformed | HTTP 400 | The malformed request was rejected. |
| EV02 | evasion | HTTP 200, unsure, score approximately 0.432 | The service did not return a human classification for this case. |
| FP02 | false_positive | HTTP 200, unsure, score approximately 0.569 | The service did not return an AI classification for this case. |

The five valid requests returned `unsure`, and the malformed request returned HTTP 400.

The report's verdicts should be assessed against the assignment's precise definitions of HELD and BROKE. An unsure response is not proof that authorship was identified correctly.

**Earlier After Run**

Attack report:

`results/attack_run_2026-10-25_1935_after.md`

The same six cases were run again.

The observed results were:

| ID | Observed result |
|---|---|
| FP01 | HTTP 200, unsure |
| EV01 | HTTP 200, unsure |
| PI01 | HTTP 200, unsure |
| MR01 | HTTP 400 |
| EV02 | HTTP 200, unsure |
| FP02 | HTTP 200, unsure |

**Before/After Evaluation**

| Evaluation | Before report | After report | Observation |
|---|---|---|---|
| Attack set | `attack_run_2026-10-25_1922_before.md` | `attack_run_2026-10-25_1935_after.md` | Same reported classifications and HTTP statuses. |
| Scenario evaluation | `run_2026-10-25_1928_before.md` | `run_2026-10-25_1935_after.md` | The displayed results are unchanged across the five scenarios. |

**Current conclusion:** The October 25 before/after tests ran successfully, but the available output does not demonstrate a measurable improvement between those runs.

The after run should not be described as a successful classification improvement. The November 9 input-handling fix is a separate improvement, documented in Section 7.

**Scenario Evaluation Details**

The evaluation script ran three trials for each of five scenarios:

| Scenario | Observed result | Limitation |
|---|---|---|
| My own writing | All displayed classifications were unsure | The samples must genuinely represent the intended human-writing test group. |
| Label coverage | All displayed classifications were unsure | The results do not demonstrate all three classifications with the selected samples. |
| Bad input | Outputs displayed as — | Confirm the report or application responses show that each input was safely rejected. |
| Prompt injection resistance | human, unsure across the displayed samples | The outputs are unchanged between runs and do not establish complete resistance. |
| Appeal path | unsure | This scenario alone does not verify the actual appeal endpoint and audit event. |

After report:

`results/run_2026-10-25_1935_after.md`

The evaluation scenarios are useful for repeatable testing, but their outputs should be checked against the actual acceptance criteria.

In particular, an appeal workflow should be tested by submitting a real existing `content_id` to `POST /appeal` and confirming the resulting audit entry. The separate November 9 appeal test now provides that evidence.

**November 9 Attack Runs**

An earlier 56-case run was saved as:

`results/attack_run_2026-11-09_1148.md`

The final regression run was then completed after restoring the original application and reapplying the MF02 fix.

Command:

```bash
python run_attacks.py --set . --label final
```

Final report:

`results/attack_run_2026-11-09_1215_final.md`

The final run contained 56 attacks. Its results were:

| HTTP response | Count |
|---|---:|
| 200 | 39 |
| 400 | 14 |
| 413 | 1 |
| 429 | 2 |
| **Total** | **56** |

The runner reported:

- 56 attacks executed.
- 0 automatically marked BROKE.
- 56 cases left for manual judgment.

Notable results included:

- EV01 returned a `human` classification.
- EV10 returned an `ai` classification.
- FP07 returned an `ai` classification despite being a false-positive test.
- PI02 returned a `human` classification.
- MF01 returned HTTP 400.
- MF02 returned HTTP 400 after the fix.
- MF08 returned HTTP 413.
- RQ01–RQ12 returned HTTP 400.
- FL01_01–FL01_10 returned HTTP 200.
- FL01_11–FL01_12 returned HTTP 429.

**Interpretation**

The zero BROKE count means the attack runner did not automatically identify a crash, 5xx response, or missing response in this run. It does not mean that all 56 tests passed their intended security or classification objectives.

The final run confirms that the application handled the tested request formats without an automatically detected server failure. The classification results still need manual interpretation against their expected targets.

The full audit extract is saved in:

`results/audit_extract.json`

The November 9 dedicated flood evidence is saved in:

`results/flood_audit_evidence.json`

### Capstone Acceptance Test Results — November 9, 2026

The five capstone criteria were checked against repeated tests. No application changes were made between the three trials for each repeated test.

| Criterion | Evidence | Verdict |
|---|---|---|
| C1 — Malformed input safety | 12 malformed cases returned HTTP 400 in each of 3 trials (36 responses). | MET |
| C2 — Rate limiting | Each of 3 valid 15-request flood trials returned 10 HTTP 200 and 5 HTTP 429 responses. | MET |
| C3 — Audit completeness | The inspected audit extract contained rejected-request records with timestamps and rejection reasons. | MET |
| C4 — Normal operation | In each of 3 cycles, POST `/ping` and a valid submission returned HTTP 200. | MET |
| C5 — Failure recovery | In each of 3 cycles, a malformed submission returned HTTP 400 and the following valid submission returned HTTP 200. | MET |

**Test evidence files**

- Malformed-input trials: `results/attack_run_2026-11-09_1646_malformed_trial1.md`, `results/attack_run_2026-11-09_1648_malformed_trial2.md`, and `results/attack_run_2026-11-09_1650_malformed_trial3.md`.
- Passing flood trials: `results/flood_2026-11-09_1130.md`, `results/flood_2026-11-09_1206.md`, and `results/flood_2026-11-09_1645.md`.
- Excluded carryover run: `results/flood_2026-11-09_1643.md` (15 requests returned HTTP 429 because the rate-limit window was already active).
- Audit evidence: `results/audit_extract.json`.

The audit check used the accumulated log rather than three isolated audit-only trials. The repeated recovery checks were sequential: malformed request, health check, then valid submission. These results demonstrate controlled request handling and recovery; they do not establish that the detector correctly identifies every AI-generated or human-written submission.

## 7. The Improvement

### Verified Input-Handling Improvement — MF02

During November 9 testing, the single-character malformed-input case exposed an unhandled `ValueError` in the detector.

**Before:** Submitting a single character caused an HTTP 500 response because the detector could not score text containing too few tokens.

**Cause:** The detector's scoring function raised a `ValueError` when the input contained too few tokenizer tokens. The submission route did not handle this exception.

**Change:** I restored the original `app.py` from Git and reapplied a focused exception handler around the model-scoring call. The route now records the rejection and returns a structured HTTP 400 response.

The handler is:

```python
try:
    model_score = float(detector.model_signal(text))
except ValueError as exc:
    audit.log_rejection(
        creator_id=creator_id,
        reason="text_too_short",
    )
    return jsonify({
        "error": "text_too_short",
        "message": str(exc),
    }), 400
```

**After:** The same test returned:

```text
HTTP/1.1 400 BAD REQUEST
```

Response body:

```json
{
  "error": "text_too_short",
  "message": "Text is too short to score — a few sentences at least."
}
```

The audit log also recorded the rejection:

```json
{
  "creator_id": "mf02_final_test",
  "event": "rejected",
  "reason": "text_too_short",
  "status": "rejected"
}
```

The final regression test was run using:

```bash
python run_attacks.py --set . --label final
```

MF02 returned HTTP 400, and the complete 56-case run reported zero automatically marked BROKE cases.

**Interpretation:** This is a verified improvement in input handling and service robustness. It changes an unhandled server error into a controlled client error and records the rejection in the audit log.

It does not demonstrate improved authorship-classification accuracy.

### Classification Improvement Still Outstanding

The October 25 before/after attack and scenario reports showed unchanged results. Although rate limiting, audit logging, and input handling have been implemented and verified, those changes have not been shown to improve detector-classification performance.

A specific classification improvement must still be selected, implemented, and evaluated against the same test samples.

The improvement should be documented with:

- The original behavior.
- The code change.
- The reason for making the change.
- The before-test results.
- The after-test results.
- An explanation of whether the change improved, worsened, or did not affect the relevant criterion.

Until this comparison is completed, the project should not claim that its classification-improvement requirement has passed.

## 8. What's Still Broken

The service is functional, but several limitations remain.

1. **Authorship uncertainty:** The model and style signals cannot establish who wrote a piece of text.
2. **Conservative classification:** In the latest 72-sample evaluation, 66 submissions were classified as unsure and none as AI.
3. **Ground-truth evaluation:** The 72 samples have not been systematically compared against known authorship labels.
4. **False-positive evaluation:** Ten known human-written samples still need to be evaluated against the acceptance threshold.
5. **Score separation:** The five-human versus five-AI mean-score comparison remains incomplete.
6. **Classification improvement:** A measurable before/after improvement to detector-classification performance has not yet been demonstrated.
7. **Rate-limit persistence:** The limiter uses in-memory storage and resets when the service restarts.
8. **Production readiness:** The development Flask server and local model configuration have not been evaluated as a production deployment.
9. **Energy and financial cost:** CPU and memory measurements are recorded, but electrical energy and financial cost per run have not been directly measured.

**Next Step**

The next major task is to implement one specific classification improvement and rerun the same evaluation set. The results should be compared with the original run so that any measurable difference can be explained honestly.

## 9. How I Used AI

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

**What I changed:** Ran the six-case attack set and five scenario evaluations, preserved the reports, and documented the current findings.

The displayed October 25 before/after outputs were unchanged, so a classification improvement that produces a demonstrable difference remains to be completed.

I also evaluated 72 writing submissions and calculated the average model, style, and combined scores. This helped identify the large proportion of uncertain classifications and the difference between the two scoring signals.

### Moment 5 — Fixing Single-Character Input Handling

**What I asked for:** Help diagnosing why the single-character malformed-input test caused an HTTP 500 response.

**What came back:** Guidance to inspect the detector exception and handle the `ValueError` in the Flask submission route.

**What I changed:** Added exception handling, returned HTTP 400 with the `text_too_short` error, recorded the rejection in the audit log, and reran the full 56-case attack set.

This improved input handling and service robustness, although it did not change the detector's classification accuracy.

---

## Running the Project

See `RUNNING.md` for installation, setup, and command instructions.

Activate the virtual environment before running the project.

In Git Bash:

```bash
source .venv/Scripts/activate
```

Run the environment check:

```bash
python test.py
```

The environment check passed all nine checks in an earlier run, including Python version, virtual environment, declared dependency ranges, PyTorch, Flask, detector model, and service availability.

Start the service:

```bash
python app.py
```

The default address is:

```text
http://127.0.0.1:5000
```

Run requests from a second terminal while Flask is running.

Check service health:

```bash
curl http://127.0.0.1:5000/health
```

Run the flood test:

```bash
python run_attacks.py --flood 15
```

Run the attack-set preview without sending requests:

```bash
python run_attacks.py --set . --show
```

Run the full attack set:

```bash
python run_attacks.py --set . --label final
```

---

## Final Project Status

The core service, two scoring signals, weighted scoring implementation, configurable thresholds, audit logging, appeal workflow, and Unit 8 rate limiting have been implemented and tested.

The latest 72-sample evaluation produced:

- Average model score: `0.6651`
- Average style score: `0.3569`
- Average combined score: `0.5110`
- Human classifications: `6`
- Unsure classifications: `66`
- AI classifications: `0`

The November 9 dedicated flood test confirmed that the service accepts ten submissions per minute from the same creator and rejects the next five with HTTP 429. All five rejections were verified in the audit log.

The November 9 input-handling fix corrected the MF02 single-character input failure. The request now returns HTTP 400 instead of HTTP 500, and the rejection is recorded in the audit log.

The final November 9 attack run exercised 56 cases:

- 39 HTTP 200 responses.
- 14 HTTP 400 responses.
- 1 HTTP 413 response.
- 2 HTTP 429 responses.
- 0 automatically marked BROKE.
- 56 cases left for manual judgment.

The five capstone operational acceptance criteria are documented as passing in Section 6. Remaining work includes evaluation against known human and AI samples, a demonstrable before/after improvement to classification performance, and direct measurement of electrical energy and financial costs. A local CPU and memory resource measurement is now documented in Section 5.

The operational tests therefore pass. CPU and memory resource measurements are documented, but classification-performance evaluation and direct energy/financial cost measurement remain incomplete.

The system is an experimental writing-pattern classifier, not a reliable authorship verification system. Its results should be interpreted cautiously and should not be used as definitive evidence of who wrote a piece of text.
