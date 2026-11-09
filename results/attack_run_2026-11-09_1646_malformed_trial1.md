# Attack run — malformed_trial1

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 16:46
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `1cefebd0-ee3d-4f7c-9668-3cfac33d786b` | human | 0.279 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `122aaa51-5ccc-473e-adb9-f7f329de5b96` | unsure | 0.463 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9765a105-4ddc-4179-8cf3-9bba1df09ed3` | unsure | 0.525 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f38649d0-c3ea-4e2f-bb55-f4e9a8178584` | unsure | 0.504 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3fd03374-ca55-49c4-ae5b-714f59b5f4ec` | unsure | 0.360 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2b039bcb-1aa3-4b63-9130-bc41005b23e5` | unsure | 0.429 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `498d75a8-c13f-48a3-a857-8bc0eb130f94` | unsure | 0.473 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f9396604-d910-4a42-9b8e-1b1849d21d8f` | human | 0.312 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `0d4b112f-7905-4272-9bb0-a9e9610ac592` | unsure | 0.537 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3cd75478-ee45-44dd-989d-46b69754538c` | ai | 0.733 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f5a9cade-a686-41b5-9999-a2c1e76097b5` | unsure | 0.511 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a7ea2eec-64cb-4198-a127-b6e83aa2ebdd` | unsure | 0.585 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `82d0eee6-008d-4ee6-94a7-2c78e48bdc5d` | unsure | 0.609 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ce7671f0-21df-4c22-b2af-5858b863561e` | unsure | 0.610 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `68832f67-3fbf-498e-b603-84ca550dae67` | unsure | 0.646 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `a0e203a9-c937-4eac-acc5-de3314bb60c5` | unsure | 0.635 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b81e48db-1c43-4819-b5e7-fd3078b3b188` | ai | 0.682 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `6760066d-0917-45bb-b410-4c7403eec7cd` | unsure | 0.444 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3990e7dc-51ad-47f9-ac4a-1cb918fa01ef` | unsure | 0.373 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `12e83506-c0ff-43a0-9c61-1643b79a5ddc` | human | 0.270 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ba2b167e-1b93-419f-8bb1-34613a71055f` | unsure | 0.473 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `de9d892a-ba8d-4e0f-8752-c02fc5c2f8f4` | unsure | 0.516 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `49377661-e956-418c-948a-a8b536e3bf11` | unsure | 0.606 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `3d7edbbd-ffee-42a2-b26b-f847d21f5725` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `2b85811f-52e8-44ef-a9a9-f6886e6b8b42` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `9e844e16-896c-40e8-b20d-db0a3e153fd1` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `d0a3f128-7707-4b2a-b571-d06f127c18cc` | unsure | 0.582 |  |
| MF06 | malformed | text is emoji only | 200 | `dad5f575-b073-42d6-8f99-0ee8880d72ea` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `6438e99a-90bc-49e3-9259-aaacbdef7e07` | ai | 0.703 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2fba75d2-0ef7-45cd-b59b-708e0bf09958` | human | 0.133 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b65de647-3d40-4b50-8149-48fb8fce819b` | human | 0.133 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad212319-65a0-44f3-9b14-f4a87ca7ada7` | human | 0.133 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `11438d57-6a88-416d-b508-dafbf8a8b186` | human | 0.133 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `75949d0d-e11a-4f5f-aa46-bc94338f31eb` | human | 0.133 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2306c101-2221-4f73-99cd-610be30eb417` | human | 0.133 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73def9c4-fb29-4db4-a400-d373c8635839` | human | 0.133 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cd977955-8894-4b61-8195-a398346c68a7` | human | 0.133 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0d375569-bab5-4db4-8407-2c6ef16aa202` | human | 0.133 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a670d70f-1b80-4cfa-afdc-5cee7d827d73` | human | 0.133 |  |
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
  "content_id": "1cefebd0-ee3d-4f7c-9668-3cfac33d786b",
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
  "content_id": "122aaa51-5ccc-473e-adb9-f7f329de5b96",
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
  "content_id": "9765a105-4ddc-4179-8cf3-9bba1df09ed3",
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
  "content_id": "f38649d0-c3ea-4e2f-bb55-f4e9a8178584",
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
  "content_id": "3fd03374-ca55-49c4-ae5b-714f59b5f4ec",
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
  "content_id": "2b039bcb-1aa3-4b63-9130-bc41005b23e5",
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
  "content_id": "498d75a8-c13f-48a3-a857-8bc0eb130f94",
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
  "content_id": "f9396604-d910-4a42-9b8e-1b1849d21d8f",
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
  "content_id": "0d4b112f-7905-4272-9bb0-a9e9610ac592",
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
  "content_id": "3cd75478-ee45-44dd-989d-46b69754538c",
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
  "content_id": "f5a9cade-a686-41b5-9999-a2c1e76097b5",
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
  "content_id": "a7ea2eec-64cb-4198-a127-b6e83aa2ebdd",
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
  "content_id": "82d0eee6-008d-4ee6-94a7-2c78e48bdc5d",
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
  "content_id": "ce7671f0-21df-4c22-b2af-5858b863561e",
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
  "content_id": "68832f67-3fbf-498e-b603-84ca550dae67",
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
  "content_id": "a0e203a9-c937-4eac-acc5-de3314bb60c5",
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
  "content_id": "b81e48db-1c43-4819-b5e7-fd3078b3b188",
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
  "content_id": "6760066d-0917-45bb-b410-4c7403eec7cd",
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
  "content_id": "3990e7dc-51ad-47f9-ac4a-1cb918fa01ef",
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
  "content_id": "12e83506-c0ff-43a0-9c61-1643b79a5ddc",
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
  "content_id": "ba2b167e-1b93-419f-8bb1-34613a71055f",
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
  "content_id": "de9d892a-ba8d-4e0f-8752-c02fc5c2f8f4",
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
  "content_id": "49377661-e956-418c-948a-a8b536e3bf11",
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
  "content_id": "3d7edbbd-ffee-42a2-b26b-f847d21f5725",
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
  "content_id": "2b85811f-52e8-44ef-a9a9-f6886e6b8b42",
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
  "content_id": "9e844e16-896c-40e8-b20d-db0a3e153fd1",
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
  "content_id": "d0a3f128-7707-4b2a-b571-d06f127c18cc",
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
  "content_id": "dad5f575-b073-42d6-8f99-0ee8880d72ea",
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
  "content_id": "6438e99a-90bc-49e3-9259-aaacbdef7e07",
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
  "content_id": "2fba75d2-0ef7-45cd-b59b-708e0bf09958",
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
  "content_id": "b65de647-3d40-4b50-8149-48fb8fce819b",
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
  "content_id": "ad212319-65a0-44f3-9b14-f4a87ca7ada7",
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
  "content_id": "11438d57-6a88-416d-b508-dafbf8a8b186",
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
  "content_id": "75949d0d-e11a-4f5f-aa46-bc94338f31eb",
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
  "content_id": "2306c101-2221-4f73-99cd-610be30eb417",
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
  "content_id": "73def9c4-fb29-4db4-a400-d373c8635839",
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
  "content_id": "cd977955-8894-4b61-8195-a398346c68a7",
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
  "content_id": "0d375569-bab5-4db4-8407-2c6ef16aa202",
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
  "content_id": "a670d70f-1b80-4cfa-afdc-5cee7d827d73",
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
