> translation_of: tr/06-sourcing-archiving.md

# 06 · Sourcing and Archiving

Information without a source does not enter a record; an unarchived source is not durable. This page explains which sources we use, how, and how we archive them.

## Source hierarchy

The ranking below is a **starting point**, not an automatic reliability grade. Every source is assessed on its own track record ([05](05-verification.md)).

| Level | Type | Examples | Note |
|---|---|---|---|
| 1 | Primary official documents and announcements | Ministry statements, official gazettes, NOTAM, NAVTEX, tender and contract notices, parliamentary records, UN documents | Strong for factual announcements; a party on contested matters |
| 2 | Primary data and imagery | Openly licensed satellite imagery (e.g. Copernicus Sentinel), public ADS-B/AIS records (within the service's terms), company financial reports | Requires interpretation; method is documented |
| 3 | Media doing their own reporting | Agencies and newspapers with correspondents on the ground | Check the chain of sourcing |
| 4 | Expert researchers and think tanks | OSINT researchers who explain their method, academic work | Method must be visible |
| 5 | Social media and Telegram channels | Official accounts of parties, war correspondents, local channels | Mostly **leads**; partisan and fast, often wrong |

**Rule:** a level-5 source alone cannot make a record `verified`; verification requires an independent source or geolocation/chronolocation.

## Source registry (`src_`)

Each source is defined **once** as a `source` record in the `datasets` repository; records reference it by ID.

A source record typically contains (exact fields are in the `datasets` schemas):
- name (TR/EN), type (official, media, researcher, social media channel…), language,
- affiliated state/organisation (if any; e.g. state media),
- **reliability grade (A–F)** and rationale,
- **terms of use (`terms`)**.

### Terms of use (`terms`)

| Value | Meaning | How to use |
|---|---|---|
| `open` | Openly licensed or public domain | May be summarised with attribution and linked |
| `attribution` | Freely linkable, attribution required | Own-words summary + link + archive; short quotes |
| `restricted` | Licence restricts redistribution or derivative works (e.g. ACLED) | **Leads only.** Data is never copied; cannot be a record's sole source; actual verification uses other sources |
| `no-redistribution` | May not be redistributed in any form | Leads only; no content relayed |

When adding a new source to the registry, read the site's terms of use and write the `terms` value with a rationale. If unsure, choose the more restrictive value.

## Archiving

**Every source link must have an archived copy.** Web pages change, disappear or get blocked; Telegram posts are removed. The archive proves that the claim was made **at that time**. A `verified` record cannot have an unarchived source.

### Wayback Machine (Internet Archive) — Save Page Now

Visit in your browser:

```
https://web.archive.org/save/<url>
```

or use the "Save Page Now" box at https://web.archive.org/. The resulting link looks like `https://web.archive.org/web/<timestamp>/<url>`; put it in the source's archive field.

### archive.today

Enter and save the link at https://archive.ph/. Put the resulting short link (`https://archive.ph/xxxxx`) in the source's archive field. For dynamic pages (social media), archive.today often works better than Wayback.

### Practical rules
- Archive to **both** services where possible.
- Check that the archive actually shows the content (a login page, cookie wall or "page not found" may have been archived instead).
- If archiving fails, say so in the PR description; the record cannot be `verified` but may enter as `unverified`.
- Automated collectors will eventually trigger archiving themselves; human checking is still required.

## Media files never go into git

- Photos, videos, audio, PDFs and screenshots are **never** committed to the `datasets` or `handbook` repositories.
- Why: copyright, personal-data risk, repository size and irreversibility (removing things from git history is hard).
- Instead: original link + archive link. If needed, describe in text what the imagery shows ("the water tower visible at 0:14 in the video…").

## URL rules

### Strip tracking parameters
Write links in canonical form. Remove parameters such as:

`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `fbclid`, `gclid`, `igshid`, `si`, `mc_cid`, `mc_eid`, `ref`, `ref_src`, `s` / `t` (X share parameters), etc.

Parameters that determine content (e.g. `?id=123`, `?p=456`) stay. If unsure, remove the parameter and check the page still shows the same content.

### No shortened links
Shorteners such as `bit.ly`, `t.co`, `tinyurl.com`, `goo.gl`, `ow.ly`, `buff.ly`, `is.gd`, `cutt.ly` are **not accepted** (CI blocks them; the full list is in `policy.yaml`). Find the real destination (preferably without clicking, using a link expander) and use that. Shorteners carry both tracking and redirect-attack risks.

## Social media and Telegram sources

- Use the post's **permalink** (not the profile or home page).
  - Telegram: `https://t.me/<channel>/<post-number>`
  - Telegram public web preview (for reading and archiving without an account): `https://t.me/s/<channel>`
- Only **open, public** channels and accounts can be sources. Closed groups, private messages and invite-only channels are not sources.
- Record in the registry who runs the channel (official account, partisan channel, state media).
- Posts may be deleted: **archive immediately**.
- Private individuals' accounts are not used as sources ([02 §4](02-red-lines.md)). Even if a witness's post shows the event, the account does not enter the record; try to confirm the information from another source.
- Content from channels of terrorist organisations is not relayed; their claims are recorded, if necessary, as text and with attribution ([03](03-legal-ethics.md)).

## Language codes

The language of sources and texts is given as a **BCP 47** code:

| Code | Language |
|---|---|
| `tr` | Turkish |
| `en` | English |
| `ar` | Arabic |
| `fa` | Persian |
| `ku` / `kmr` / `ckb` | Kurdish (general) / Kurmanji / Sorani |
| `el` | Greek |
| `ru` | Russian |
| `uk` | Ukrainian |
| `hy` | Armenian |
| `az` | Azerbaijani |
| `ka` | Georgian |
| `he` | Hebrew |
| `fr` | French |

A region subtag may be added if needed (e.g. `ar-SY`). Where the script matters, use a script subtag (e.g. `az-Latn`, `az-Arab`).
