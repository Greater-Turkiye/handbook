> translation_of: tr/02-red-lines.md

# 02 · Red Lines

The rules on this page are **absolute**. There are no exceptions, no bargaining, and no "but everyone is sharing it". If you are unsure whether a rule applies, **assume it does and do not publish**; ask the maintainers through the private channel.

Every contributor is deemed to have read and accepted this page. Reviewers check these rules on every PR; CI enforces some of them automatically ([ADR 0010](../decisions/0010-content-safety-gates.md)), but **final responsibility lies with humans**.

> **Core principle:** When in doubt, don't publish. The cost of publishing too little by mistake is small; the cost of publishing too much by mistake cannot be undone.

---

## 1. Positions and movements of Turkish forces

Nothing is published, collected or analysed about the **positions, movements, deployments, order of battle, capability gaps or vulnerabilities** of the Turkish Armed Forces, Gendarmerie, Coast Guard, Police, MİT or any other Turkish security/intelligence body.

- **The only exception is official disclosures** (Ministry of National Defence, General Staff, official announcements of the relevant bodies). Even these may only be published:
  - **without coordinates**,
  - with location precision `admin1`, `country` or `sea-area` only,
  - **at least 24 hours** after the event,
  - with `policy.sensitivity: elevated`,
  - with a maintainer's `policy:approved` label.
- These rules are also enforced by the **"Turkish forces gate"** in CI: if a Turkish military/security/intelligence actor appears with role `perpetrator`, `participant`, `target` or `host`, or `policy.involves_tur_forces: true`, the record cannot be merged unless the conditions above are met.
- Unofficial imagery (convoy videos on social media, exercise photos, "they're passing through here right now" posts) is **not used, linked or geolocated, even if public.**
- ADS-B data of Turkish military aircraft and AIS data of Turkish naval vessels is **not tracked, recorded or shared.**
- Security details of military facilities on Turkish territory (including allied/NATO facilities) and of defence-industry facilities are out of scope. If a record must mention them, set `policy.involves_tur_forces: true` so it passes through the same gate.
- A foreign source's claim about Turkish forces (e.g. "Country X claimed Turkish drones flew over area Y") is also subject to these rules: attributed, coarse, delayed, and approved.

**Why?** Aggregating information scattered across open sources (the mosaic effect) can turn individually harmless pieces into a sensitive picture. We do not draw that picture.

## 2. Classified or leaked material — from any country

- Classified (e.g. GİZLİ, ÇOK GİZLİ, HİZMETE ÖZEL, SECRET, TOP SECRET, NOFORN, CONFIDENTIAL) or leaked documents, images or databases are **not used as sources, quoted, summarised, linked or analysed.**
- This applies even if the leak concerns another country and has been published in mainstream media.
- If an event is known only through a leak, it does not enter the dataset.
- At most, an official body's statement about a leak may be recorded, attributed, **without relaying the leak's content** (with maintainer approval).
- If such material is sent to you privately: do not open it, forward it or store it; notify the maintainers via [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md).

## 3. No field collection

We work **only with public, passive sources.**

- Photographing, filming, sketching or flying drones in military forbidden zones and security zones is prohibited (in Türkiye, **Law No. 2565 on Military Forbidden Zones and Security Zones**; many countries have similar laws). **Nobody visits or observes any facility** on behalf of or for the community.
- Nobody **contacts** military personnel, officials or witnesses to obtain information; no social engineering.
- No access to non-public systems: no password guessing, no use of leaked credentials, no port or vulnerability scanning, no infiltrating closed groups with fake accounts.
- Using field material collected by others ("we didn't take it") is also prohibited if it appears to have been obtained unlawfully.

## 4. Private individuals and personal data

- Names, faces, addresses, phone numbers, emails, ID numbers, licence plates or social media accounts of **private individuals** never enter a record (**KVKK, Law No. 6698**).
- **Enlisted/junior military personnel** of any country are not identified; their social media profiles are not researched or shared. Doxxing is prohibited.
- Senior figures acting publicly in an official capacity (ministers, chiefs of staff, spokespeople) may appear as actors **only in their official role and in the context of official statements.**
- Special categories of personal data (health, religion, ethnicity, political opinion, etc.) never enter a record under any circumstances.
- Nothing is shared from images or screenshots without removing faces, plates and usernames — and media is never committed to the repository anyway ([06](06-sourcing-archiving.md)).

## 5. No POW or casualty imagery

- Photos and videos of prisoners of war, detainees, the dead or the wounded are **not shared, linked or described.** (Protection of prisoners from public curiosity is also set out in Article 13 of the Third Geneva Convention.)
- Casualty figures are recorded **as text only, and attributed**: "According to the X Ministry of Defence, 4 soldiers were killed."
- Even where violent imagery is needed as evidence (e.g. to verify the location of a strike), the imagery itself is not published; only the verification result and the archive link (with maintainer approval and a content warning) go into the record.

## 6. No targeting language or incitement

- Records, posts and comments **never designate targets**: phrases like "this place should be hit", "these coordinates are a target", "find this person" are prohibited.
- No **operational advice** to any armed party (which weapon, from where, when).
- No calls to violence, revenge or lynching; no bounties, fundraising or "volunteer recruitment" announcements.
- Coordinates document **where an event happened**; they are never presented for a future action.

## 7. No hate speech

- No demeaning, generalising or dehumanising language against any people, ethnicity, religion, sect or nationality.
- **Organisations are distinguished from peoples.** An organisation's actions are attributed to that organisation, not to a people. For example, PKK actions belong to the PKK, not to Kurds; a state's actions belong to its government or forces, not to its people.
- Terrorist designations are attributed too: "the PKK, listed as a terrorist organisation by Türkiye, the US and the EU…".

## 8. Always attribute

- Every contested or unverified piece of information is attributed to whoever said it: **"according to…", "…claimed", "…said in a statement".**
- The project never makes contested characterisations in its own voice. Characterisations like "airspace violation", "provocation", "aggression", "occupation", "terrorist attack" are recorded in `claims[]`, attributed to their author.
- No information without a source. "I heard", "a friend told me" are not sources.

## 9. Copyright

- Articles, reports, images and videos are **not copied**, committed or republished.
- Summarise in your own words; give the link and an archive link.
- **Short quotations** are allowed only to relay a claim accurately (in quotation marks, with the source).
- Data from sources with `terms: restricted` or `no-redistribution` (e.g. ACLED) is never copied; such sources are used only as **leads** and can never be the **sole** source of a record.

---

## How violations are handled

| Situation | What happens |
|---|---|
| Violation in an unmerged PR | The PR is closed immediately; comments are hidden/deleted if needed. If sensitive content is involved, maintainers ask GitHub to purge cached views. |
| Violation in a merged record | The record is withdrawn with `schema: tombstone/1` (the ID is never reused). Channel posts are deleted; a correction note is published. |
| Personal data or classified material entered git history | A tombstone is not enough: maintainers purge history and request cache removal from GitHub Support. This is the only documented exception to the "files are never deleted" rule; the ID still remains as a tombstone. |
| Contributor conduct | Warning for a first, minor violation; temporary suspension on repetition; **immediate permanent ban** and removal of permissions for serious violations such as Turkish forces, classified material, doxxing, targeting or hate speech. |
| Deliberate poisoning (fake sources, fabricated records) | Permanent ban; all of the contributor's other records are re-reviewed. |

If you notice a violation: **do not draw attention to it in a public comment** (that makes the content more visible). Write to the private address in [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md).

## Quick checklist (before submitting a PR)

- [ ] No information on Turkish forces beyond official disclosures.
- [ ] No classified/leaked material.
- [ ] No field-collected material.
- [ ] No private individuals, personal data or identities of junior personnel.
- [ ] No POW/casualty imagery or links to it.
- [ ] No targeting, inciting or hateful language.
- [ ] Every contested characterisation is in `claims[]` and attributed.
- [ ] No copied text/images; no restricted source used as the sole source.
