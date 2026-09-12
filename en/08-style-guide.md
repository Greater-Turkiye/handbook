> translation_of: tr/08-style-guide.md

# 08 · Style Guide

Our records and posts must be **neutral, attributed and concise**. A reader should immediately understand what happened, who said so, and how sure we are.

> The examples on this page are **fictional**; they do not represent real events.

## Core principles

1. **Neutral**: no adjectives or emotion. Never write "scandalous", "arrogant", "historic", "shocking", "major threat".
2. **Attributed**: anything unverified or contested is tied to its source: "according to…", "…said in a statement", "…claimed".
3. **Concise**: title is one sentence; summary 1–3 sentences. Background, if needed, goes in a separate field.
4. **Right degree of certainty**: plain statement if verified; attribution if unverified; estimative language for analysis ([05](05-verification.md)).
5. **No sensationalism**: no ALL CAPS, exclamation marks, "BREAKING" or siren emojis.

## Expressions the project never uses in its own voice

The following characterisations appear only in `claims[]`, attributed to their author:

violation · provocation · aggression · occupation · incitement · terrorist attack · massacre · genocide · war crime · self-defence · retaliation · "so-called" · "enemy/adversary" (unless quoting a party)

Right: "The Hellenic National Defence General Staff said Turkish aircraft violated its airspace." (Because this example involves Turkish forces, it must also pass the [Turkish forces gate](02-red-lines.md).)
Wrong: "An airspace violation occurred."

## Title patterns

Titles use the **past tense**, active voice, in **subject–verb–object–place** order. English titles are also in the past tense.

| Type | TR | EN |
|---|---|---|
| Verified event | Yunanistan, Girit açıklarında deniz tatbikatı başlattı | Greece began a naval exercise off Crete |
| Official statement | Rusya Savunma Bakanlığı: Karadeniz'de insansız deniz aracı imha edildi | Russian MoD said an uncrewed surface vessel was destroyed in the Black Sea |
| Unverified claim | Yerel kaynaklara göre Musul yakınlarında patlama | Explosion near Mosul, according to local sources |
| Claim proven false | İddia: Görüntü Halep'te yeni bir saldırıyı gösteriyor (yanlış — görüntü eski) | Claim: Footage shows new strike in Aleppo (false — footage is old) |
| Procurement | Mısır, ek savaş uçağı alımı için sözleşme imzaladı | Egypt signed a contract for additional fighter aircraft |
| Disputed | İsrail ve Hizbullah, güney Lübnan'daki çatışmaya dair çelişkili açıklamalar yaptı | Israel and Hezbollah gave conflicting accounts of clash in southern Lebanon |

## Summary pattern

The summary answers these questions in order:
1. **What happened?** (the fact)
2. **Who?** (actors, by official title)
3. **Where, when?** (UTC, consistent with its precision)
4. **According to whom?** (source)
5. **How sure are we?** (state what isn't known)

Example (TR):
> Yunanistan Deniz Kuvvetleri, 11 Eylül 2026'da Girit'in güneyinde üç gün sürecek bir deniz tatbikatı başlattı. Tatbikat bölgesi, Yunanistan'ın yayımladığı NAVTEX ile duyuruldu. Katılan birlik sayısı açıklanmadı.

Example (EN):
> The Hellenic Navy began a three-day naval exercise south of Crete on 11 September 2026. The exercise area was announced in a NAVTEX issued by Greece. The number of participating units was not disclosed.

## Numbers, units, dates

| Topic | TR | EN |
|---|---|---|
| Thousands / decimal separator | 1.250 · 3,5 | 1,250 · 3.5 |
| Date (in prose) | 12 Eylül 2026 | 12 September 2026 |
| Time (in prose) | 14.30 UTC | 14:30 UTC |
| In data fields | ISO 8601 (`2026-09-12T14:30:00Z`), decimal point | same |

- The **metric system** is used. In maritime and aviation contexts the source's unit is kept: nautical miles (nmi), knots, flight levels (FL). Give the metric equivalent in parentheses if helpful: "12 nautical miles (about 22 km)".
- Money: the source's currency and ISO code ("USD 2.1 billion"). No conversion unless the source provides one.
- Casualty and figure claims are **always** attributed and written as the source gives them: "at least 12", "about 300". If sources give different figures, all are written with attribution.
- Spell out abbreviations on first use: "Exclusive Economic Zone (EEZ)". See the [Glossary](09-glossary.md) for common ones.

## Actor names

- Use official names; full on first mention, short thereafter.
- For non-state armed groups, Türkiye's official designation is given, stating who lists them ([02 §7](02-red-lines.md)).
- People are referred to only by official title: "Spokesperson of the Iranian Ministry of Foreign Affairs", with a name only if needed and alongside the title.

## Machine translation

- Machine-translated text is flagged with `i18n.machine: true` (the field indicates which language was translated; exact structure is in the `datasets` schema).
- The flag is removed after a human who knows both languages has reviewed and corrected the text.
- Machine translation makes mistakes especially with **place names, ranks, weapon system names and negation**; check these specifically.
- When translating short quotes from the source's original language, keep the original text too.

## Posts (Telegram, Bluesky, X)

- Every post links to a record; no record, no post (except bulletins, see [ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)).
- Status label at the start of the post: `[DOĞRULANDI]`, `[DOĞRULANMADI]`, `[İHTİLAFLI]`, `[YANLIŞ]` / `[VERIFIED]`, `[UNVERIFIED]`, `[DISPUTED]`, `[FALSE]`.
- Short: title + one sentence of context + link.
- No attached imagery (copyright and red lines); only maps or charts the project produced itself, if needed.
- No mentions and no provocative hashtags.

## How to write corrections

Each correction is added to the record's `corrections[]` field and contains: **date (UTC)**, **what changed**, **why**.

Example:
```yaml
corrections:
  - date: 2026-09-13T08:00:00Z
    text:
      tr: "Konum hassasiyeti locality'den admin2'ye düşürüldü; ilk geolokasyondaki eşleşme hatalıydı."
      en: "Location precision lowered from locality to admin2; the initial geolocation match was incorrect."
```

Rules:
- Write corrections **candidly**: without minimising the error and without unnecessary apologies.
- Any status change (e.g. `unverified` → `false`) must come with a correction entry.
- Corrections that don't change meaning, such as typos, need no entry; git history suffices.
- Significant corrections are also announced on the channels where the original was posted: "DÜZELTME: …" / "CORRECTION: …".
