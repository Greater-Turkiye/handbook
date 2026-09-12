> translation_of: tr/05-verification.md

# 05 · Verification

Every record states **explicitly** how reliable it is. A reader must be able to tell at a glance whether something is "verified" or "one party's claim". This page describes the scales and rules we use. For the rationale see [ADR 0006](../decisions/0006-verification-scale.md).

Verification answers two separate questions:

1. **How reliable is the source?** → Source reliability (A–F), kept in the **source registry** (`src_` record).
2. **How credible is this information?** → Information credibility (1–6), kept on **the record itself** (`assessment.credibility`).

The two are independent: a reliable source can relay false information; an unreliable source can provide true information.

## The Admiralty (NATO) scale

### Source reliability

| Code | Turkish | English | When? |
|---|---|---|---|
| **A** | Tamamen güvenilir | Completely reliable | No doubt about authenticity, trustworthiness or competence. In practice given **very rarely**. |
| **B** | Genellikle güvenilir | Usually reliable | Minor doubts; has provided valid information most of the time. |
| **C** | Oldukça güvenilir | Fairly reliable | Doubts; has provided valid information in the past. |
| **D** | Genellikle güvenilir değil | Not usually reliable | Significant doubts; has provided valid information occasionally. |
| **E** | Güvenilmez | Unreliable | Lacks authenticity, trustworthiness and competence; history of invalid information. |
| **F** | Güvenilirliği değerlendirilemez | Reliability cannot be judged | No basis for evaluation. **Default for new sources.** |

**Notes:**
- Official sources are not automatically A. A defence ministry is a party when it speaks about its own losses, enemy losses or contested incidents. A state's **factual announcement about its own activity** (e.g. "the exercise has begun") differs from a **contested claim** (e.g. "an enemy aircraft was shot down"); the latter is always attributed in `claims[]`.
- Source reliability is changed by a maintainer or reviewer through a registry PR, with a written rationale.

### Information credibility

| Code | Turkish | English | When? |
|---|---|---|---|
| **1** | Başka kaynaklarca doğrulanmış | Confirmed by other sources | Confirmed by independent sources or visual/spatial evidence; logical and consistent. |
| **2** | Muhtemelen doğru | Probably true | Not confirmed, but logical, consistent and fits the known picture. |
| **3** | Belki doğru | Possibly true | Not confirmed; reasonable but somewhat inconsistent or incomplete. |
| **4** | Şüpheli | Doubtful | Not confirmed; possible but not logical, contrary information exists. |
| **5** | Olası değil | Improbable | Illogical, contradicted by other information. |
| **6** | Doğruluğu değerlendirilemez | Truth cannot be judged | No basis for evaluation. **Default for new records.** |

## Status values (`assessment.status`)

| Value | Turkish | Meaning |
|---|---|---|
| `unverified` | Doğrulanmamış | Sourced and archived, but not yet meeting the verification rules. **Default.** |
| `partially_verified` | Kısmen doğrulanmış | Part of the event (e.g. place and time) is verified, another part (e.g. perpetrator, outcome) is not. The summary states which part is verified. |
| `verified` | Doğrulanmış | Meets **all** conditions below. |
| `disputed` | İhtilaflı | Reliable sources contradict each other; the project takes no side and attributes the claims. |
| `false` | Yanlış | The claim has been shown to be false. The record is **not deleted**; the fact that it was false is permanent. |

## Rules for `verified`

A record may be `verified` only if it meets **all** of these conditions (checked by CI):

1. `assessment.credibility` is **1 or 2**.
2. **English text** (title and summary) is present.
3. **Every source** has an archive link ([06](06-sourcing-archiving.md)).
4. One of:
   - **At least two independent sources**, or
   - Verification by **geolocation**, **chronolocation** or **satellite imagery** — with the method and evidence link stated in the record ([07](07-geo-time-disputed.md)).
5. A restricted (`restricted` / `no-redistribution`) source cannot be the **sole** basis.

`verified` means "the event happened"; it **does not mean contested characterisations are true**. For example, it can be verified that an aircraft flew in a certain area; whether that was a "violation" is attributed to the parties in `claims[]`.

## What is an independent source?

Two sources are independent if they obtained the information **through separate paths**.

| Situation | Independent? |
|---|---|
| Two news sites publish the same wire story (e.g. AA, Reuters, AFP) | **No** — one source |
| A newspaper relays a ministry statement | **No** — the source is the ministry |
| Two state media outlets of the same government | **No** |
| A Telegram channel reposts another channel's post | **No** |
| Two opposing parties to a conflict confirm the same fact | **Yes** — and a strong confirmation (where parties with conflicting interests agree) |
| Official statement + an outlet reporting on the ground with its own correspondent | **Yes** |
| Official statement + independent satellite imagery | **Yes** |
| Geolocated videos filmed by different people from different angles | **Yes** (but the videos themselves are never committed) |

When in doubt, **don't assume independence**; trace where each source got its information (the circular-reporting trap).

## Handling disinformation

- If a false claim has circulated widely, that is **itself a notable event**. A record is opened, the claim attributed, `status: false` set and debunking sources added.
- `false` records are **not deleted**: they serve as a reference when the same claim resurfaces.
- The title never presents the claim as fact: use the "İddia: …" / "Claim: …" pattern ([08](08-style-guide.md)).
- When debunking, avoid re-amplifying the falsehood: state the truth first, then the claim, then why it is false.
- Old footage presented as new, footage from other countries, video-game footage and AI-generated images are the most common types. Reverse image search and chronolocation are the first steps.
- If you notice coordinated behaviour (the same text posted by many accounts simultaneously), notify the maintainers; such networks may involve information about private individuals and are assessed before anything enters a record.

## Estimative language

In assessments and analysis, probability expressions are used **consistently**. We base ours on US Intelligence Community Directive 203 (ICD 203):

| Turkish | English | Approximate probability |
|---|---|---|
| Neredeyse hiç | Almost no chance | 1–5% |
| Çok düşük ihtimal | Very unlikely | 5–20% |
| Düşük ihtimal | Unlikely | 20–45% |
| Yaklaşık eşit | Roughly even chance | 45–55% |
| Muhtemel | Likely | 55–80% |
| Çok muhtemel | Very likely | 80–95% |
| Neredeyse kesin | Almost certain | 95–99% |

Rules:
- Use these expressions **only** with these meanings. Avoid off-scale phrases like "most probably", "maybe", "strongly likely".
- Don't confuse likelihood (how probable) with confidence (the quality of the information behind the assessment). State "low/moderate/high confidence" separately if needed.
- Estimative language is for **analysis**. In factual records an event is either verified or attributed as a claim.

## Reviewer verification checklist

- [ ] Every source is in the registry with a reliability grade.
- [ ] Every source's archive link works.
- [ ] Source independence was actually checked.
- [ ] `credibility` and `status` are consistent with each other and the rules.
- [ ] Contested characterisations are in `claims[]` and attributed.
- [ ] Any geolocation/chronolocation method is explained and reproducible.
- [ ] No restricted source is the sole basis.
