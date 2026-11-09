# Attack run — malformed_trial3

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 16:50
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `006931ec-97a1-415a-9f36-56465f3b4a7e` | human | 0.279 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `5d4cf568-0a96-47de-95a7-05a47748060d` | unsure | 0.463 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5bdda2be-f148-473f-8731-b5446f766444` | unsure | 0.525 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `01c903a1-5351-4cf1-9e63-f62329aec626` | unsure | 0.504 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c2e40c8f-c8b0-4274-a2f7-15bcc3a17807` | unsure | 0.360 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e1b7abbd-f205-41c8-be27-948f03b15af7` | unsure | 0.429 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `fcbf33ef-d2cd-4110-afaa-c899893792fa` | unsure | 0.473 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `638aa4d1-19a5-4f6d-90ee-fe73ad2d870a` | human | 0.312 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `cbbb6785-5495-4742-bfbe-0e02e3ce7227` | unsure | 0.537 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e174aead-59b5-42fd-a5ec-3277a392fe46` | ai | 0.733 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `86604f80-f2e1-4f83-86fe-4428c3aef913` | unsure | 0.511 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7fdfb095-6724-485b-97df-c2584ab9c57a` | unsure | 0.585 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `0a8da3db-aff9-477f-b082-87c82138d681` | unsure | 0.609 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `642bb9dc-e0d3-4d5b-87d0-01725da8156d` | unsure | 0.610 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e2334452-ce1b-4ce1-a8df-ea7d891ccd5b` | unsure | 0.646 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f874cd86-df9d-4ef2-be63-024107723a57` | unsure | 0.635 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `16f0f1ff-49e7-45da-ac3a-9e22300f904b` | ai | 0.682 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `11e2625e-937e-4ad5-8436-dfe6e09f60c9` | unsure | 0.444 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b3ae364c-2ad4-4b5d-beb6-0f292f13a59f` | unsure | 0.373 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3bf67604-0499-416b-89ba-14bf38d7f49c` | human | 0.270 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5a91b519-2b2e-4542-b0bc-7d948978bcf2` | unsure | 0.473 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `569df167-961b-44b1-bed2-61aaa9b03826` | unsure | 0.516 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a7cac72b-0209-402d-bb1a-79a2973ed79f` | unsure | 0.606 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `31c04190-c349-49e9-a12b-c35e4cc04681` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `723651a8-d5f4-470b-8f1a-a8adf684ef73` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `a9caa71f-f8c1-468d-82e2-eb038217044b` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `d484a516-0fd9-47c9-ad49-6356bcb475f5` | unsure | 0.582 |  |
| MF06 | malformed | text is emoji only | 200 | `b677f351-214a-4f51-a73c-a6e75bf54001` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `5cd74db2-97c4-4c56-b621-70324ce1dfb7` | ai | 0.703 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fbceca0e-9f86-4c34-a1ad-635df90b6444` | human | 0.133 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `31619eac-7370-4e28-989d-3356ee8f1fcc` | human | 0.133 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bf36be77-5cec-4d16-87ce-1a990d6206b5` | human | 0.133 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f5add052-39e5-4f15-8adf-7b47522f3362` | human | 0.133 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `60c59121-f576-46f9-a3f2-d6972db6a7ae` | human | 0.133 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4eaa2e99-db05-4a88-b8d1-6aeaf9be8864` | human | 0.133 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `103e7513-8654-4c96-a5fe-9ff8574b7334` | human | 0.133 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8c98bef7-b315-4b4a-b9ae-6dafb1fbb875` | human | 0.133 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `870b13e2-87c0-4751-ba9d-3cee842568ae` | human | 0.133 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `65ee8694-c855-4197-97d9-8514f981ca0b` | human | 0.133 |  |
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
  "content_id": "006931ec-97a1-415a-9f36-56465f3b4a7e",
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
  "content_id": "5d4cf568-0a96-47de-95a7-05a47748060d",
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
  "content_id": "5bdda2be-f148-473f-8731-b5446f766444",
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
  "content_id": "01c903a1-5351-4cf1-9e63-f62329aec626",
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
  "content_id": "c2e40c8f-c8b0-4274-a2f7-15bcc3a17807",
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
  "content_id": "e1b7abbd-f205-41c8-be27-948f03b15af7",
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
  "content_id": "fcbf33ef-d2cd-4110-afaa-c899893792fa",
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
  "content_id": "638aa4d1-19a5-4f6d-90ee-fe73ad2d870a",
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
  "content_id": "cbbb6785-5495-4742-bfbe-0e02e3ce7227",
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
  "content_id": "e174aead-59b5-42fd-a5ec-3277a392fe46",
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
  "content_id": "86604f80-f2e1-4f83-86fe-4428c3aef913",
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
  "content_id": "7fdfb095-6724-485b-97df-c2584ab9c57a",
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
  "content_id": "0a8da3db-aff9-477f-b082-87c82138d681",
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
  "content_id": "642bb9dc-e0d3-4d5b-87d0-01725da8156d",
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
  "content_id": "e2334452-ce1b-4ce1-a8df-ea7d891ccd5b",
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
  "content_id": "f874cd86-df9d-4ef2-be63-024107723a57",
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
  "content_id": "16f0f1ff-49e7-45da-ac3a-9e22300f904b",
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
  "content_id": "11e2625e-937e-4ad5-8436-dfe6e09f60c9",
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
  "content_id": "b3ae364c-2ad4-4b5d-beb6-0f292f13a59f",
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
  "content_id": "3bf67604-0499-416b-89ba-14bf38d7f49c",
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
  "content_id": "5a91b519-2b2e-4542-b0bc-7d948978bcf2",
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
  "content_id": "569df167-961b-44b1-bed2-61aaa9b03826",
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
  "content_id": "a7cac72b-0209-402d-bb1a-79a2973ed79f",
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
  "content_id": "31c04190-c349-49e9-a12b-c35e4cc04681",
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
  "content_id": "723651a8-d5f4-470b-8f1a-a8adf684ef73",
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
  "content_id": "a9caa71f-f8c1-468d-82e2-eb038217044b",
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
  "content_id": "d484a516-0fd9-47c9-ad49-6356bcb475f5",
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
  "content_id": "b677f351-214a-4f51-a73c-a6e75bf54001",
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
  "content_id": "5cd74db2-97c4-4c56-b621-70324ce1dfb7",
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
  "content_id": "fbceca0e-9f86-4c34-a1ad-635df90b6444",
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
  "content_id": "31619eac-7370-4e28-989d-3356ee8f1fcc",
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
  "content_id": "bf36be77-5cec-4d16-87ce-1a990d6206b5",
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
  "content_id": "f5add052-39e5-4f15-8adf-7b47522f3362",
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
  "content_id": "60c59121-f576-46f9-a3f2-d6972db6a7ae",
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
  "content_id": "4eaa2e99-db05-4a88-b8d1-6aeaf9be8864",
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
  "content_id": "103e7513-8654-4c96-a5fe-9ff8574b7334",
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
  "content_id": "8c98bef7-b315-4b4a-b9ae-6dafb1fbb875",
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
  "content_id": "870b13e2-87c0-4751-ba9d-3cee842568ae",
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
  "content_id": "65ee8694-c855-4197-97d9-8514f981ca0b",
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
