# Attack run — practice

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 11 attacks · 2026-11-02 11:45
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **11**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| FP01 | false_positive | Get genuine human writing incorrectly labelled as AI | 200 | `cabb6058-1c85-42a7-9b40-62c3dadf6e63` | unsure | 0.584 |  |
| EV01 | evasion | Get AI-generated text labelled as human | 200 | `e6d1d37a-9e5a-4483-a050-15b8683f9529` | unsure | 0.577 |  |
| PI01 | prompt_injection | Test whether instructions embedded in submitted text affect the detector | 200 | `3843c967-e755-4999-b8be-7097daed017b` | unsure | 0.355 |  |
| MR01 | malformed | Test handling of unusual or unexpected text content | 400 | `—` | — | — |  |
| EV02 | evasion | Test whether unusual formatting affects classification | 200 | `9c9f8145-72b2-4413-b653-6a4eea0e7334` | unsure | 0.432 |  |
| FP02 | false_positive | Test whether short, natural personal writing is wrongly flagged | 200 | `3c8a3620-bc73-46ae-8ba5-d6ecb2e0317e` | unsure | 0.569 |  |
| MAL01 | malformed | Empty HTTP body | 400 | `—` | — | — |  |
| MAL02 | malformed | Invalid JSON body | 400 | `—` | — | — |  |
| MAL03 | malformed | JSON array instead of object | 400 | `—` | — | — |  |
| MAL04 | malformed | JSON null instead of object | 400 | `—` | — | — |  |
| MAL05 | malformed | Missing text field | 400 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 2 | 0 | 2 |
| `false_positive` | 2 | 0 | 2 |
| `malformed` | 6 | 0 | 6 |
| `prompt_injection` | 1 | 0 | 1 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### FP01 — `false_positive`

*Targeting:* Get genuine human writing incorrectly labelled as AI

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "cabb6058-1c85-42a7-9b40-62c3dadf6e63",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5840819913961014,
  "model_score": 0.7767,
  "style_score": 0.3914639827922029,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV01 — `evasion`

*Targeting:* Get AI-generated text labelled as human

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e6d1d37a-9e5a-4483-a050-15b8683f9529",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5767083333333334,
  "model_score": 0.8305,
  "style_score": 0.3229166666666667,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* Test whether instructions embedded in submitted text affect the detector

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "3843c967-e755-4999-b8be-7097daed017b",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3546638890140742,
  "model_score": 0.2632,
  "style_score": 0.44612777802814835,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

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
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* Test whether unusual formatting affects classification

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9c9f8145-72b2-4413-b653-6a4eea0e7334",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4324078631107775,
  "model_score": 0.5268,
  "style_score": 0.3380157262215549,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* Test whether short, natural personal writing is wrongly flagged

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "3c8a3620-bc73-46ae-8ba5-d6ecb2e0317e",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5694745614035088,
  "model_score": 0.7793,
  "style_score": 0.35964912280701755,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### MAL01 — `malformed`

*Targeting:* Empty HTTP body

```json
{
  "id": "MAL01",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MAL02 — `malformed`

*Targeting:* Invalid JSON body

```json
{
  "id": "MAL02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MAL03 — `malformed`

*Targeting:* JSON array instead of object

```json
{
  "id": "MAL03",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MAL04 — `malformed`

*Targeting:* JSON null instead of object

```json
{
  "id": "MAL04",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MAL05 — `malformed`

*Targeting:* Missing text field

```json
{
  "id": "MAL05",
  "status": 400,
  "content_id": null,
  "creator_id": "practice_MAL05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
