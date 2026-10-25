
# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 6 attacks · 2026-10-25 19:22
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **0**

The verdicts below are based on the observed responses and the stated attack targets. `HELD` means the attack did not achieve its stated goal in this run. These results do not establish that the service is secure against all attacks.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| FP01 | false_positive | Get genuine human writing incorrectly labelled as AI | 200 | `dc39f731-9e4f-49d6-8833-7d4ec03039c0` | unsure | 0.584 | HELD |
| EV01 | evasion | Get AI-generated text labelled as human | 200 | `3968b8a6-04ef-4547-afd8-91af5a7c29e1` | unsure | 0.577 | HELD |
| PI01 | prompt_injection | Test whether instructions embedded in submitted text affect the detector | 200 | `316262bc-a163-4bcd-a8f2-97a8609313cd` | unsure | 0.355 | HELD |
| MR01 | malformed | Test handling of unusual or unexpected text content | 400 | `—` | — | — | HELD |
| EV02 | evasion | Test whether unusual formatting affects classification | 200 | `df45f902-53eb-4149-b843-48701b909e17` | unsure | 0.432 | HELD |
| FP02 | false_positive | Test whether short, natural personal writing is wrongly flagged | 200 | `50e80379-3576-4b59-9282-fdb5f55f6bb4` | unsure | 0.569 | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 2 | 0 | 0 |
| `false_positive` | 2 | 0 | 0 |
| `malformed` | 1 | 0 | 0 |
| `prompt_injection` | 1 | 0 | 0 |

---

## What came back

### FP01 — `false_positive`

*Targeting:* Get genuine human writing incorrectly labelled as AI

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "dc39f731-9e4f-49d6-8833-7d4ec03039c0",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5840819913961014,
  "model_score": 0.7767,
  "style_score": 0.3914639827922029,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The service returned `unsure`, rather than labelling the submitted text as AI-written. The false-positive attempt did not achieve its stated goal in this run.

### EV01 — `evasion`

*Targeting:* Get AI-generated text labelled as human

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "3968b8a6-04ef-4547-afd8-91af5a7c29e1",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5767083333333334,
  "model_score": 0.8305,
  "style_score": 0.3229166666666667,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The service did not classify the submitted text as human-written. The evasion attempt did not achieve its stated goal in this run.

### PI01 — `prompt_injection`

*Targeting:* Test whether instructions embedded in submitted text affect the detector

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "316262bc-a163-4bcd-a8f2-97a8609313cd",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3546638890140742,
  "model_score": 0.2632,
  "style_score": 0.44612777802814835,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The response remained `unsure`. This run did not show a confident classification caused by the embedded instruction, although the output alone cannot establish complete prompt-injection resistance.

### MR01 — `malformed`

*Targeting:* Test handling of unusual or unexpected text content

```json
{
  "id": "MR01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MR01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The service returned HTTP 400 and did not produce a content ID. This is consistent with rejecting malformed input, assuming HTTP 400 is the expected behavior under the assignment criteria.

### EV02 — `evasion`

*Targeting:* Test whether unusual formatting affects classification

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "df45f902-53eb-4149-b843-48701b909e17",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4324078631107775,
  "model_score": 0.5268,
  "style_score": 0.3380157262215549,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The unusual-formatting attempt did not cause the service to classify the submitted text as human-written. It returned `unsure`.

### FP02 — `false_positive`

*Targeting:* Test whether short, natural personal writing is wrongly flagged

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "50e80379-3576-4b59-9282-fdb5f55f6bb4",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5694745614035088,
  "model_score": 0.7793,
  "style_score": 0.35964912280701755,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

**Assessment:** The service returned `unsure`, not an AI-written classification. The short-writing false-positive attempt did not achieve its stated goal in this run.

---

## Summary

All five valid submissions returned HTTP 200 with a classification of `unsure`. The malformed submission returned HTTP 400. None of the six attacks achieved its stated goal according to the provisional verdicts above.

The main limitation is that `unsure` indicates uncertainty, not correct authorship detection. These results should be compared with the assignment's exact success criteria and the subsequent after-improvement run.
