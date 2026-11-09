# Attack run — malformed_trial2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 16:48
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `207d65e1-6c4d-491f-b873-1d62e5e1fed7` | human | 0.279 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `45cb5ded-e679-4fb4-8f57-48479c4a09b6` | unsure | 0.463 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9ab244c7-234c-4053-a9e6-c5ca80084f38` | unsure | 0.525 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `65ecb60a-1cc1-4538-b0ff-623ffed69f54` | unsure | 0.504 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `56a1acff-56c6-4dfd-8a7e-1f24a8832398` | unsure | 0.360 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `f2aad038-57be-4bca-aba1-ce3495085e5e` | unsure | 0.429 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `a2935c0e-53df-4a90-a6b1-97d04c2d243a` | unsure | 0.473 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `9d4901d0-ffe3-4b0f-a978-27b130d5c7e7` | human | 0.312 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `69a443d2-f52c-4b8a-bfce-9b9eabd2bae7` | unsure | 0.537 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3010a695-41b0-48c2-a3e6-f43917e75552` | ai | 0.733 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `27e34d6c-e6ea-436a-b009-85c61b46783f` | unsure | 0.511 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `276ad2e6-1be1-4d0e-9ff9-ef24c87577f4` | unsure | 0.585 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `b8de0b49-1e05-4992-b628-7575ea2525e3` | unsure | 0.609 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `45fd6b80-82b8-41de-968b-2d336ef3515f` | unsure | 0.610 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `fe73f975-a1b4-4db2-b6a5-e7d7e767d904` | unsure | 0.646 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f2cafec6-14cc-4700-bc21-213b12284857` | unsure | 0.635 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `bef7acb8-287e-4244-8e21-1f9a97976f63` | ai | 0.682 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `6698c8b9-f394-4c87-af89-6623064c6056` | unsure | 0.444 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `38888775-f213-46f6-b441-aaed39e54d0f` | unsure | 0.373 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e3b4e184-cc7f-46ea-a87a-1d46f9bd8c4c` | human | 0.270 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `6b8d8491-193e-496a-8bdc-a5043661b220` | unsure | 0.473 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0f88e800-b99d-4d37-8321-916da1e07ecd` | unsure | 0.516 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `756c2049-db8d-4e65-a917-7077e2e84bd4` | unsure | 0.606 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bf9d58b5-6ad9-42e6-a639-19e0956d6042` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `c79964b4-6725-48d1-9d17-ade7a8e7c39e` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `785c8be1-c015-439d-98fc-e1055df94836` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `78ac6e97-42b7-4f71-bf7a-cd3e3294b3e9` | unsure | 0.582 |  |
| MF06 | malformed | text is emoji only | 200 | `94ac2757-6b9b-4af5-972a-374219cfb536` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `4e615d6d-205e-4c0d-a6eb-e27338397bee` | ai | 0.703 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c0f8ea4e-d55a-4e5c-a54c-955e3ab61a55` | human | 0.133 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `71aa0f69-af43-4390-83c4-6a0d4b57eb1f` | human | 0.133 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9bc57fa7-1f54-4284-89df-78d83afac21a` | human | 0.133 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `34fe7ce2-a68a-4031-9f4b-15b88bb3d552` | human | 0.133 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `90df9a51-deb8-4ac8-acc6-f99e4cf8babc` | human | 0.133 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e1016a65-befc-4a87-8b6d-8db2e142bcd5` | human | 0.133 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5ce82ea5-63fc-461d-8c13-3b286387e7ac` | human | 0.133 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c1525ea-2429-4bf4-ab42-41eae78b2c57` | human | 0.133 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6ef6b7cd-bf97-4b98-a837-6630c34febfd` | human | 0.133 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2542a9dc-54c8-4533-ba9d-91f55ed218c5` | human | 0.133 |  |
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
  "content_id": "207d65e1-6c4d-491f-b873-1d62e5e1fed7",
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
  "content_id": "45cb5ded-e679-4fb4-8f57-48479c4a09b6",
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
  "content_id": "9ab244c7-234c-4053-a9e6-c5ca80084f38",
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
  "content_id": "65ecb60a-1cc1-4538-b0ff-623ffed69f54",
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
  "content_id": "56a1acff-56c6-4dfd-8a7e-1f24a8832398",
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
  "content_id": "f2aad038-57be-4bca-aba1-ce3495085e5e",
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
  "content_id": "a2935c0e-53df-4a90-a6b1-97d04c2d243a",
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
  "content_id": "9d4901d0-ffe3-4b0f-a978-27b130d5c7e7",
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
  "content_id": "69a443d2-f52c-4b8a-bfce-9b9eabd2bae7",
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
  "content_id": "3010a695-41b0-48c2-a3e6-f43917e75552",
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
  "content_id": "27e34d6c-e6ea-436a-b009-85c61b46783f",
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
  "content_id": "276ad2e6-1be1-4d0e-9ff9-ef24c87577f4",
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
  "content_id": "b8de0b49-1e05-4992-b628-7575ea2525e3",
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
  "content_id": "45fd6b80-82b8-41de-968b-2d336ef3515f",
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
  "content_id": "fe73f975-a1b4-4db2-b6a5-e7d7e767d904",
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
  "content_id": "f2cafec6-14cc-4700-bc21-213b12284857",
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
  "content_id": "bef7acb8-287e-4244-8e21-1f9a97976f63",
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
  "content_id": "6698c8b9-f394-4c87-af89-6623064c6056",
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
  "content_id": "38888775-f213-46f6-b441-aaed39e54d0f",
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
  "content_id": "e3b4e184-cc7f-46ea-a87a-1d46f9bd8c4c",
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
  "content_id": "6b8d8491-193e-496a-8bdc-a5043661b220",
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
  "content_id": "0f88e800-b99d-4d37-8321-916da1e07ecd",
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
  "content_id": "756c2049-db8d-4e65-a917-7077e2e84bd4",
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
  "content_id": "bf9d58b5-6ad9-42e6-a639-19e0956d6042",
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
  "content_id": "c79964b4-6725-48d1-9d17-ade7a8e7c39e",
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
  "content_id": "785c8be1-c015-439d-98fc-e1055df94836",
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
  "content_id": "78ac6e97-42b7-4f71-bf7a-cd3e3294b3e9",
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
  "content_id": "94ac2757-6b9b-4af5-972a-374219cfb536",
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
  "content_id": "4e615d6d-205e-4c0d-a6eb-e27338397bee",
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
  "content_id": "c0f8ea4e-d55a-4e5c-a54c-955e3ab61a55",
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
  "content_id": "71aa0f69-af43-4390-83c4-6a0d4b57eb1f",
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
  "content_id": "9bc57fa7-1f54-4284-89df-78d83afac21a",
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
  "content_id": "34fe7ce2-a68a-4031-9f4b-15b88bb3d552",
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
  "content_id": "90df9a51-deb8-4ac8-acc6-f99e4cf8babc",
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
  "content_id": "e1016a65-befc-4a87-8b6d-8db2e142bcd5",
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
  "content_id": "5ce82ea5-63fc-461d-8c13-3b286387e7ac",
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
  "content_id": "0c1525ea-2429-4bf4-ab42-41eae78b2c57",
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
  "content_id": "6ef6b7cd-bf97-4b98-a837-6630c34febfd",
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
  "content_id": "2542a9dc-54c8-4533-ba9d-91f55ed218c5",
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
