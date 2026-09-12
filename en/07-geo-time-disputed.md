> translation_of: tr/07-geo-time-disputed.md

# 07 · Geo, Time and Disputed Areas

## Geolocation

Geolocation means determining **where** an image was taken by comparing details in it with maps and satellite imagery.

Basic steps:
1. **Study the image**: road layout, buildings, minarets, water towers, power lines, mountain silhouettes, coastline, signs, licence plates (plates only to identify country/region; they never enter a record), vegetation.
2. **Narrow down the candidate area**: the location claimed by the source, language and script, known area of events.
3. **Compare**: open satellite imagery (e.g. Copernicus Sentinel data), satellite layers of commercial maps, OpenStreetMap, street-level imagery.
4. Find **at least three independent matching features** (a single building is not enough).
5. **Document the method**: write which feature matched what, the reference used and its date. Someone else must be able to follow your steps and reach the same result.

If you use someone else's geolocation, cite them as a source and check the result yourself.

## Chronolocation

Chronolocation means determining **when** an image was taken.

- **Shadows**: shadow direction and length give an approximate time from the sun's angle, if the location is known (sun-position calculators).
- **Weather**: clouds, rain, snow — compare with historical weather records.
- **Satellite imagery window**: between two satellite passes showing a structure intact/damaged.
- **First appearance**: the moment the image first appeared online is an upper bound. Use reverse image search for older copies (old footage presented as a new event is the most common disinformation).
- **File metadata is unreliable**: platforms often strip it; what remains can be altered.

## Time rules

- All times are **UTC** in ISO 8601: `2026-09-12T14:30:00Z`.
- When converting local time to UTC, check the time-zone database; daylight saving rules differ by country and can change over time. (Example: Türkiye is UTC+3 year-round, Iran UTC+3:30 year-round.)
- Every time has a **precision** field (e.g. minute, hour, day, month). If you only know the date, mark precision as **day**; don't invent `00:00`.
- **Event time** differs from **publication time**. Records store event time. If only publication time is known, say so and lower the precision.
- For ongoing events (exercises, deployments), start and end are recorded separately; unknown end is left empty.

## Location rules

- Coordinates are written in **WGS 84** decimal degrees (latitude, longitude).
- **Maximum 5 decimal places** (about 1 metre). More gives a false impression of precision; CI rejects it.
- Coordinates must never be more precise than the actual precision. Don't give a building's coordinates for an event only known to be in a town.

### Location precision (`precision`)

| Value | Meaning | Coordinates |
|---|---|---|
| `exact` | Point determined by geolocation (within about 100 m) | Yes |
| `site` | Known facility (base, port, airfield) | Facility centre |
| `locality` | Settlement (village, town, city) | Settlement centre |
| `admin2` | District-level administrative unit | Unit centroid or none |
| `admin1` | Province/state level | No coordinates |
| `country` | Only the country is known | No coordinates |
| `sea-area` | Sea area (e.g. "Eastern Mediterranean", "Northern Aegean") | No coordinates |

> **Turkish forces gate:** records involving Turkish security bodies may only use `admin1`, `country` or `sea-area` and must have no coordinates ([02](02-red-lines.md)).

Lowering precision is always allowed; raising it requires evidence.

## The `countries` field

`countries` lists **states whose actors are involved in the event**, **not** who the location belongs to.

- A Greek warship's exercise in the Eastern Mediterranean → `countries: [GRC]` (plus any other participating states).
- An incident between Russian and Ukrainian forces in the Black Sea → `countries: [RUS, UKR]`.
- Place information is in the `location` field and carries no sovereignty claim.

Country codes are **ISO 3166-1 alpha-3**. Exceptions:

| Code | Label (TR) | Label (EN) |
|---|---|---|
| `XNC` | KKTC (Kuzey Kıbrıs Türk Cumhuriyeti) | TRNC (Turkish Republic of Northern Cyprus) |
| `CYP` | GKRY (Güney Kıbrıs Rum Yönetimi) | GKRY / Greek Cypriot Administration of Southern Cyprus |

`XNC` is a project code, not part of the ISO standard.

## Disputed territories policy

1. **Records never assert sovereignty.** The project does not say in its own voice who a place belongs to, where a border runs, or whose jurisdiction a sea area falls under.
2. **Claims are attributed.** "X stated the incident took place in its exclusive economic zone; Y says the area lies on its continental shelf." Such statements go in `claims[]`.
3. **Labels use Türkiye's official terminology.** This is the project's publication language, not a sovereignty claim: KKTC/TRNC, GKRY, Aegean islands, Kardak Rocks, etc. Where Türkiye has no official term, the common neutral name is used.
4. **No border or maritime boundary lines are published.** Our map layers contain no contested borders, EEZ or continental shelf lines.
5. **Place names have three layers:**
   - `tr`: Turkish name (Turkish exonym where one exists),
   - `en`: English name (Türkiye's official English usage where one exists),
   - `local`: name in the local language and script.

### Examples

| `tr` | `en` | `local` |
|---|---|---|
| Halep | Aleppo | حلب |
| Musul | Mosul | الموصل |
| Kerkük | Kirkuk | كركوك |
| Trablus (Libya) | Tripoli (Libya) | طرابلس |
| Trablusşam (Lübnan) | Tripoli (Lebanon) | طرابلس |
| Bingazi | Benghazi | بنغازي |
| Tebriz | Tabriz | تبریز |
| Batum | Batumi | ბათუმი |
| Midilli | Lesbos | Λέσβος |
| Sakız | Chios | Χίος |
| Rodos | Rhodes | Ρόδος |
| İstanköy | Kos | Κως |
| Kardak Kayalıkları | Kardak Rocks | Ίμια |

To avoid confusing different places with the same name (like the two Tripolis), add the country in parentheses where needed.

### Special cases

- **Cyprus**: the KKTC/TRNC and GKRY labels are used. Local names may be Turkish or Greek; for places in the TRNC, `local` is Turkish.
- **Aegean**: Türkiye and Greece disagree on issues including territorial-water breadth, airspace, FIR responsibility, the continental shelf, the demilitarised status of islands, and islands, islets and rocks whose sovereignty was not ceded by treaty (EGAYDAAK). Every characterisation on these issues (e.g. "airspace violation", "FIR violation") is attributed.
- **Eastern Mediterranean and Black Sea**: maritime jurisdiction claims are attributed; the location is given as a `sea-area` or coordinates.
- **Disputes between other countries** (e.g. Crimea, Golan, West Bank): labels use names consistent with Türkiye's official position; the parties' claims are attributed.
