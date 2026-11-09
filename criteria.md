# Capstone Acceptance Criteria — Provenance Guard

1. **Malformed input safety:** All 10 malformed-request tests must return appropriate 4xx responses without crashing. This protects service availability.

2. **Rate limiting:** When one creator submits 15 requests within the configured window, at least one must receive HTTP 429. This prevents flooding.

3. **Audit completeness:** Every tested rejected request must produce an audit record with a timestamp, outcome, and rejection reason. This supports accountability.

4. **Normal operation:** Valid submissions must return HTTP 200, and /ping must return HTTP 200 after malformed-request and flood tests. This checks service availability.

5. **Failure recovery:** After a malformed submission receives a controlled 4xx response, a subsequent valid submission must still succeed. This checks recovery.

These criteria evaluate the capstone extension: safer input handling, rate limiting, structured audit logging, and service availability.
