> translation_of: tr/03-legal-ethics.md

# 03 · Law and Ethics

> **This page is not legal advice.** Its purpose is to make contributors aware of which laws are relevant to this work. Check the current text of laws on mevzuat.gov.tr; consult a lawyer about any concrete situation.

## The basic fact: responsibility is personal

- Greater Türkiye has **no legal entity**. It is not an association, foundation or company; there is no institution to represent you, defend you or take responsibility.
- The legal responsibility for every contribution you make is **yours**.
- A pseudonym does not protect you legally; platforms comply with legal requests ([04 · OPSEC](04-opsec.md)).
- Contributors outside Türkiye must also respect the laws of the country they are in (and of their citizenship). Many countries have strict rules on photographing military facilities, classified information, espionage and personal data.

## Relevant Turkish law

### Turkish Penal Code (TCK, Law 5237) Arts. 326–339 — Offences against state secrets and espionage

This chapter covers acts such as **obtaining or disclosing** information that, by its nature, must remain secret for the security or the internal or external political interests of the state; destroying or falsifying such documents; **political or military espionage**; and obtaining and disclosing information whose disclosure has been **prohibited** by the competent authorities. Penalties are severe.

**What it means for us:**
- Public information can become sensitive when aggregated (the mosaic effect). This is the main reason we compile nothing about Turkish forces ([02 · Red lines §1](02-red-lines.md)).
- Classified or leaked material is never used ([02 §2](02-red-lines.md)).
- Where a publication ban is in force on a topic, no content is produced for the duration; maintainers announce such bans.

### TCK Art. 217/A — Public dissemination of misleading information

Criminalises **publicly disseminating false information** concerning the country's internal and external security, public order or public health, with the motive of creating anxiety, fear or panic among the public and in a manner capable of disturbing public peace. Committing the offence **by concealing the offender's real identity**, or within the activities of an organisation, is an aggravating circumstance.

**What it means for us:**
- Unverified information is marked unverified (`unverified`) and written **with attribution**; it is never presented as fact ([05 · Verification](05-verification.md)).
- No sensationalist, panic-inducing language ([08 · Style guide](08-style-guide.md)).
- Claims that turn out false are marked with a correction, and corrections are posted on the channels too.
- Be aware that working under a pseudonym may be an aggravating factor under this article; this is one more reason accuracy and attribution rules are vital.

### Law No. 2565 on Military Forbidden Zones and Security Zones

Prohibits and penalises unauthorised entry into military forbidden zones and security zones, and taking photographs or film, drawing sketches, pictures or plans, taking notes and similar activities there.

**What it means for us:** we do no field collection. No contributor visits a facility, films or flies drones for the community ([02 §3](02-red-lines.md)).

### Law No. 6698 on the Protection of Personal Data (KVKK)

Governs the processing of any information relating to an identified or identifiable natural person, with stricter rules for **special categories of personal data** such as health, religion, ethnicity and political opinion.

**What it means for us:** we do not collect, store or publish data about private individuals. Officials are referred to only in their official capacity. CI scans for patterns such as Turkish ID numbers (TC Kimlik), phone numbers, emails and IBANs ([ADR 0010](../decisions/0010-content-safety-gates.md)).

### Law No. 5651 — Internet publications

Defines the responsibilities of content, hosting and access providers, and the procedures for content removal and **access blocking**. There are also fast-track blocking procedures on national security and public order grounds.

**What it means for us:**
- A contributor who writes a record is its **content provider**.
- Against the possibility of the project or our channels being blocked in Türkiye, data is protected through mirrors such as Zenodo and clones ([ADR 0011](../decisions/0011-threat-model.md)).
- If an official removal request arrives, maintainers assess it; the request and the action taken are recorded as transparently as the law allows.

### Also keep in mind

- **Anti-Terror Law No. 3713**: terrorist propaganda is an offence. Propaganda imagery, statements and symbols of terrorist organisations are not shared; their claims are recorded only as text, attributed, and only where necessary.
- **Law No. 5846 on Intellectual and Artistic Works**: copyright. No copying; summaries and links only.

## Ethical principles

### 1. Accuracy
- Don't overstate verification. Write down what you don't know.
- Don't use certain language where certainty isn't warranted; use estimative language correctly ([05](05-verification.md)).
- Two independent sources means **two independent chains of information**, not "two news sites".

### 2. Attribution
- The project never makes contested characterisations in its own voice. Claims are attributed to their authors.
- If you use someone else's verification work (e.g. a geolocation), credit them.

### 3. Harm minimisation
- Ask for every record: "Whom could publishing this harm?"
- Protect the dignity of civilians, prisoners, the wounded and families.
- For sensitive information, delay and coarse location are always worth more than speed.
- If public interest and harm conflict, maintainers decide; the default answer is "don't publish".

### 4. Corrections
- Making mistakes is normal; hiding them is not.
- Corrections are added to `corrections[]` with a date and explanation; the previous state remains visible in git history.
- Significant corrections are automatically announced on the channels where the original was posted ([ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)).

### 5. Independence and conflicts of interest
- We work for no one. If you work for a defence company, state body or related organisation, don't review records about it (abstain during review).
- No donations, sponsorships or payments are accepted on behalf of the community.

## Official requests and your rights

- If you receive an official request concerning the community, get legal support in your own name and (where legally possible) inform the maintainers.
- Maintainers cannot give legal advice either; community rules are no substitute for legal protection.
