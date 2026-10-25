Acceptance Criteria — Provenance Guard

Five criteria that define what "working" means for this service.

1. False positives on human writing

When I submit 10 pieces of writing that I wrote myself, no more than 1 should receive the high-confidence AI label.

Why this target: A false accusation can damage a writer's reputation. I would rather miss some AI-generated text than incorrectly accuse too many human writers.

2. Different scores for different writing

Across 5 human-written samples and 5 AI-generated samples, the average combined score for the AI-generated samples should be higher than the average combined score for the human-written samples by at least 0.15.

Why this target: The system should distinguish between the two groups better than chance alone. A measurable gap helps me evaluate whether the signals are useful, although it does not prove that individual predictions are correct.

3. All three labels are reachable

All three labels — high-confidence human, unsure, and high-confidence AI — must appear in at least one of my test submissions.

Why this target: If a label is unreachable, the scoring thresholds may be incorrectly configured. The unsure label is especially important because the system should be able to acknowledge uncertainty instead of making every case a confident decision.

4. Appeals are recorded

For every valid appeal submitted against an existing content_id, the service must return a successful response, record the appeal in the audit log, and change the content's status to under_review.

Why this target: Writers need a way to challenge decisions. An appeal that is not recorded provides no evidence that the system reconsidered a potentially incorrect judgment.

5. Invalid input is handled safely

In 10 tests involving missing text, empty text, whitespace-only text, non-string text, missing creator IDs, and invalid JSON, the service must return an appropriate 4xx status code without crashing. The /ping route must continue returning HTTP 200 afterward.

Why this target: Malformed requests should not crash the service or interrupt other users. Testing invalid inputs also helps identify weaknesses before the service is exposed to more traffic.