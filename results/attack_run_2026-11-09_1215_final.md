# Attack run — final

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 12:15
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `54e3e456-e583-44d5-844a-650b824ebc2b` | human | 0.279 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `95c5fe3c-2aa8-4950-880c-b999631e2242` | unsure | 0.463 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `117c2552-1678-4121-9953-c3571884a93b` | unsure | 0.525 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3aefd216-40ce-4019-b706-cdf7b093a5ec` | unsure | 0.504 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8f79f04f-dcbe-434e-8f81-2b190e72942f` | unsure | 0.360 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ed3b8ea4-66ca-40f3-a0e4-608d31a34bdf` | unsure | 0.429 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `2b43c272-98be-4c6f-aa1e-23a8b016d542` | unsure | 0.473 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `7811de9b-3485-4257-96e9-1a96ae1d9cae` | human | 0.312 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `e4a555cf-55ab-4746-a160-ff191cf7fd11` | unsure | 0.537 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `2b45465d-bcf9-4dec-820c-1e3eeca5121a` | ai | 0.733 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4812adb0-dfa0-456c-a824-441df0fce4ed` | unsure | 0.511 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `30ad316b-8812-4024-aa49-9e4bc4e86ab8` | unsure | 0.585 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `332c0b5f-9be9-43d2-aaeb-f8a671bc18b6` | unsure | 0.609 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d262572f-9642-4528-ae47-6c97e9d3dbc4` | unsure | 0.610 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e1f765e0-34f8-4fb0-b35e-c8ed11d3ddb5` | unsure | 0.646 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `bb57c829-2549-4083-a58c-41dfa5a2bd9a` | unsure | 0.635 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d46c2b1c-0791-475a-9659-7376778cfe60` | ai | 0.682 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `ea10737d-bfa5-4601-a9af-8fcb070193fe` | unsure | 0.444 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `68919973-7a17-4127-a6f7-9c06c3239b14` | unsure | 0.373 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `646a6853-2fc4-4ef2-88f9-7a5adbaf35d9` | human | 0.270 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c26674b2-c14b-47b3-8c4b-2a29c2f05f8a` | unsure | 0.473 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d7cd8013-6e44-4c34-b052-40f51b406234` | unsure | 0.516 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7d869836-bf2b-482f-8c0b-534d847e5f1b` | unsure | 0.606 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4a5f222e-a6a2-4df3-b4a4-adcd0dd7c787` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `47be83b8-36c2-4ac0-94d3-cdf5f9f63dc0` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `b673bf2c-466e-4cf7-8451-419569e2bc85` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `2984aa59-ad1b-4f25-80d7-3dede68a1726` | unsure | 0.582 |  |
| MF06 | malformed | text is emoji only | 200 | `8948b7b1-8dd8-4554-b998-aad2ef8013b8` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `21518e6d-3148-48c5-bd9e-1605d9a7381c` | ai | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `95c2f9d9-4b36-4eba-8d51-23e29c0f53f4` | human | 0.133 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `28943086-fbe6-42de-93ba-9eb9398e93db` | human | 0.133 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e1d8b107-28c0-43e4-9dea-5243d9fcb0bb` | human | 0.133 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9de66bc6-a541-473d-b127-40173e2d6cee` | human | 0.133 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fbf8704d-82f3-4ace-b767-1383729317f7` | human | 0.133 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8d9af61b-b00e-4db4-a923-53bc51bd529b` | human | 0.133 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a7b7142-f782-4b64-93d1-db4da1d86ebb` | human | 0.133 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3212980b-5a06-4186-b4da-d94d972ea4d2` | human | 0.133 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `42742ab5-285d-42e4-abad-8cc3d8572031` | human | 0.133 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1373d312-86b7-4ee4-8eb0-9124224c2f73` | human | 0.133 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "54e3e456-e583-44d5-844a-650b824ebc2b",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.27884523026890057,
  "model_score": 0.1635,
  "style_score": 0.3941904605378011,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "95c5fe3c-2aa8-4950-880c-b999631e2242",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4625802633042163,
  "model_score": 0.5943,
  "style_score": 0.3308605266084326,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "117c2552-1678-4121-9953-c3571884a93b",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5249766739856688,
  "model_score": 0.6662,
  "style_score": 0.3837533479713377,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "3aefd216-40ce-4019-b706-cdf7b093a5ec",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5037615335924515,
  "model_score": 0.6114,
  "style_score": 0.3961230671849029,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "8f79f04f-dcbe-434e-8f81-2b190e72942f",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3601083290874082,
  "model_score": 0.3212,
  "style_score": 0.39901665817481646,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "ed3b8ea4-66ca-40f3-a0e4-608d31a34bdf",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4285484871375451,
  "model_score": 0.5727,
  "style_score": 0.2843969742750902,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "2b43c272-98be-4c6f-aa1e-23a8b016d542",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.47302747665127653,
  "model_score": 0.5862,
  "style_score": 0.35985495330255307,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "7811de9b-3485-4257-96e9-1a96ae1d9cae",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.31204360798855246,
  "model_score": 0.2452,
  "style_score": 0.3788872159771049,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "e4a555cf-55ab-4746-a160-ff191cf7fd11",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5367580979775846,
  "model_score": 0.7042,
  "style_score": 0.369316195955169,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "2b45465d-bcf9-4dec-820c-1e3eeca5121a",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7331687267332978,
  "model_score": 0.9792,
  "style_score": 0.48713745346659554,
  "label": "This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4812adb0-dfa0-456c-a824-441df0fce4ed",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5112326941502947,
  "model_score": 0.6175,
  "style_score": 0.4049653883005893,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "30ad316b-8812-4024-aa49-9e4bc4e86ab8",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5851338632151204,
  "model_score": 0.7387,
  "style_score": 0.43156772643024083,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "332c0b5f-9be9-43d2-aaeb-f8a671bc18b6",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6089411218436425,
  "model_score": 0.8051,
  "style_score": 0.4127822436872848,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d262572f-9642-4528-ae47-6c97e9d3dbc4",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6101564455197319,
  "model_score": 0.8329,
  "style_score": 0.3874128910394638,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "e1f765e0-34f8-4fb0-b35e-c8ed11d3ddb5",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6461196442072241,
  "model_score": 0.8005,
  "style_score": 0.49173928841444825,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "bb57c829-2549-4083-a58c-41dfa5a2bd9a",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6349101820212063,
  "model_score": 0.8814,
  "style_score": 0.3884203640424127,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d46c2b1c-0791-475a-9659-7376778cfe60",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6816354162608713,
  "model_score": 0.8816,
  "style_score": 0.4816708325217427,
  "label": "This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "ea10737d-bfa5-4601-a9af-8fcb070193fe",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4441217534580063,
  "model_score": 0.3223,
  "style_score": 0.5659435069160126,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "68919973-7a17-4127-a6f7-9c06c3239b14",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.372795653059222,
  "model_score": 0.4625,
  "style_score": 0.283091306118444,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "646a6853-2fc4-4ef2-88f9-7a5adbaf35d9",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.27002910624218573,
  "model_score": 0.2044,
  "style_score": 0.3356582124843715,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c26674b2-c14b-47b3-8c4b-2a29c2f05f8a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4726286955423058,
  "model_score": 0.5943,
  "style_score": 0.3509573910846116,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d7cd8013-6e44-4c34-b052-40f51b406234",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5158305754748722,
  "model_score": 0.4998,
  "style_score": 0.5318611509497443,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "7d869836-bf2b-482f-8c0b-534d847e5f1b",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.6055426820527154,
  "model_score": 0.6401,
  "style_score": 0.5709853641054309,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "4a5f222e-a6a2-4df3-b4a4-adcd0dd7c787",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.48132274366819805,
  "model_score": 0.5583,
  "style_score": 0.404345487336396,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "47be83b8-36c2-4ac0-94d3-cdf5f9f63dc0",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "b673bf2c-466e-4cf7-8451-419569e2bc85",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "2984aa59-ad1b-4f25-80d7-3dede68a1726",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5821333333333334,
  "model_score": 0.9976,
  "style_score": 0.16666666666666666,
  "label": "We couldn't confidently distinguish the writing patterns. This result is uncertain and should not be treated as proof that the text was written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "8948b7b1-8dd8-4554-b998-aad2ef8013b8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7484500000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "21518e6d-3148-48c5-bd9e-1605d9a7381c",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This text has patterns often associated with AI-generated writing, but this result does not prove who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
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

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
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

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
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

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
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

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
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

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
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

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "95c2f9d9-4b36-4eba-8d51-23e29c0f53f4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "28943086-fbe6-42de-93ba-9eb9398e93db",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "e1d8b107-28c0-43e4-9dea-5243d9fcb0bb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "9de66bc6-a541-473d-b127-40173e2d6cee",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "fbf8704d-82f3-4ace-b767-1383729317f7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "8d9af61b-b00e-4db4-a923-53bc51bd529b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "2a7b7142-f782-4b64-93d1-db4da1d86ebb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "3212980b-5a06-4186-b4da-d94d972ea4d2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "42742ab5-285d-42e4-abad-8cc3d8572031",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "1373d312-86b7-4ee4-8eb0-9124224c2f73",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.13314432624113473,
  "model_score": 0.0287,
  "style_score": 0.23758865248226949,
  "label": "This text has patterns often associated with human writing. Automated analysis cannot confirm who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
