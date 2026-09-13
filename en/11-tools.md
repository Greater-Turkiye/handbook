> translation_of: tr/11-tools.md

# 11 · Tools

This page lists **free and legal** open-source tools for community work: what each one does, its terms of use, and OPSEC notes.

> ⛔ **Red-line reminder — do not skip**
>
> - These tools are **NEVER used to track Turkish forces.** ADS-B from Turkish military aircraft and AIS from Turkish naval and coast guard vessels is not searched, recorded or shared. No satellite imagery analysis or geolocation of Turkish units, facilities or exercises ([02 §1](02-red-lines.md)).
> - These tools are never used to track, locate or identify **private individuals**: no face searches, no tracking of private aircraft or boat owners, no geolocating people's homes or workplaces ([02 §4](02-red-lines.md)).
> - Tools are used **passively** only: no unauthorised access, no scanning, no automated collection beyond what the terms allow ([02 §3](02-red-lines.md)).
> - Being able to use a tool does not mean you may publish the result. Publication is always decided under the [Red Lines](02-red-lines.md) and [Verification](05-verification.md) rules.

## Inclusion criteria

- **Free**: usable without registering a payment method. "Free trials" that ask for a credit card are excluded ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)).
- **Legal and passive**: shows only publicly available information; use complies with the service's own terms.
- **Terms read**: each tool's terms of use or licence page was read when it was added and is linked below.

> **Last checked: 2026-09-13.** Services change their terms, prices and addresses. Check a tool's terms yourself before using it; if you notice a change, update this page with a PR.

### General OPSEC notes

- Use the tools in the **separate browser profile** you keep for community work ([04 §4](04-opsec.md)). Don't search while logged in to your personal Google, Microsoft or Yandex account: your searches get linked to that account.
- Every image you upload, every coordinate and search term you enter ends up in the **service provider's logs**. Don't upload anything that could be sensitive.
- For tools that need an account, use the email tied to your pseudonymous account. On services whose **terms require your real identity** (e.g. an OpenSky account), don't register under a pseudonym and don't use those features.
- Screenshots, data files and exports from these tools are **never committed** ([06](06-sourcing-archiving.md)). A record gets the link, the archive link and a text description of the method.
- When information from a tool is used as a source, choose the `terms` value in the source registry according to the tool's terms ([06](06-sourcing-archiving.md)). The `terms` suggestions below are a starting point; if unsure, choose the more restrictive value.

---

## 1. Satellite imagery

### Copernicus Browser
- **Address:** https://browser.dataspace.copernicus.eu/
- **What it does:** Shows imagery from the European Union's Copernicus Sentinel satellites in the browser and lets you compare dates and download. Sentinel-2 provides optical imagery; Sentinel-1 provides radar (SAR) imagery that works through cloud and at night. Useful for checking whether a structure was damaged within a date range, or how a large deployment area changed.
- **Cost and terms:** Free; a free account is needed for all features. The [Copernicus Data Space Ecosystem terms](https://dataspace.copernicus.eu/terms-and-conditions) grant "free, full and open" access to Sentinel data; the portal's own content (text and images other than Sentinel data) may not be redistributed. The [Sentinel data legal notice](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice) allows reproduction, distribution and modification, with mandatory attribution: `Copernicus Sentinel data [Year]`, or `Contains modified Copernicus Sentinel data [Year]` for modified imagery. **Suggested `terms`:** `open`.
- **OPSEC and limits:** Sentinel-2's best resolution is 10 m, too coarse to tell vehicles, buildings or aircraft types apart; don't claim you derived that from it. SAR imagery doesn't read like a photograph; have someone experienced check your interpretation.

### NASA Worldview
- **Address:** https://worldview.earthdata.nasa.gov/
- **What it does:** Shows daily, global, low-resolution imagery from NASA satellites (MODIS, VIIRS, etc.) and fire/thermal anomaly layers. Used for coarse checks of large fires, smoke plumes and the timing of wide-area events.
- **Cost and terms:** Free; no account needed to view. The [NASA Earth science data policy](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies) provides for full and open sharing of data, with no restrictions on use or redistribution; attribution is encouraged. **Suggested `terms`:** `open`.
- **OPSEC and limits:** Resolution is in the hundreds of metres. A thermal anomaly alone doesn't mean "a strike happened"; it could be a fire, an industrial site or agricultural burning. Don't make a record `verified` on this evidence alone.

## 2. Flight tracking

> ⛔ Turkish military aircraft are **never searched for, tracked, recorded or screenshotted** in these tools ([02 §1](02-red-lines.md)). Private and business jets may belong to private individuals; they are not tracked ([02 §4](02-red-lines.md)).

### adsb.lol
- **Address:** https://adsb.lol/
- **What it does:** An ADS-B/MLAT map and API fed by volunteer receivers that doesn't filter out military aircraft. Used to see the public broadcasts of foreign reconnaissance, tanker and transport aircraft.
- **Cost and terms:** Free; no account needed. The historical datasets adsb.lol publishes are licensed under the [Open Database License (ODbL) 1.0 and CC0](https://github.com/adsblol/globe_history_2025). **Suggested `terms`:** `attribution` (ODbL requires attribution; derived databases must be shared under the same licence).
- **OPSEC and limits:** Military aircraft often switch ADS-B off, and signals can be spoofed; not appearing on the map doesn't mean "didn't fly". MLAT positions are approximate. Feeding the network with your own receiver means sharing your receiver's location with the service; it isn't needed for community work.

### OpenSky Network
- **Address:** https://opensky-network.org/
- **What it does:** A Swiss-based non-profit research network offering a live map, a historical database and an API; widely cited in academic work.
- **Cost and terms:** Viewing the map is free. The [terms of use and data licence agreement](https://opensky-network.org/about/terms-of-use) license the data **solely for non-profit research and non-profit education**. Commercial entities (including government and military contractors) need a written licence. Using the REST API in a live product or **any automated system** requires a prior written agreement, even for non-profits. Datasets may not be passed on to third parties. Publications based on non-anonymised data must anonymise aircraft identifiers. **Suggested `terms`:** `restricted`. For this reason, `platform` collectors do **not** use the OpenSky API without a written agreement.
- **OPSEC:** The terms say registrants must not conceal their identity and that OpenSky may disclose the name of the registered requester. That is incompatible with our pseudonymous model: **don't register under a pseudonym**, and don't use account-only features for community work.

## 3. Ship tracking

> ⛔ Turkish naval and Coast Guard vessels are **never searched for, tracked or recorded** in these tools ([02 §1](02-red-lines.md)). Crew members and owners are not identified ([02 §4](02-red-lines.md)).

Most AIS sites **restrict reuse** of their data and screenshots. AIS sites are therefore usually `restricted` or `no-redistribution` sources: **leads only**, data is never copied, and they can never be a record's sole source ([02 §9](02-red-lines.md)). AIS can be switched off or spoofed, and warships often don't broadcast.

### VesselFinder
- **Address:** https://www.vesselfinder.com/
- **What it does:** A live ship map based on AIS data. Used to see the public position broadcasts of merchant ships, tankers and auxiliaries.
- **Cost and terms:** Free web access with limited features; extra features are paid. The [terms of use](https://www.vesselfinder.com/terms) prohibit automated extraction (bots, scrapers) outside the authorised API. Free users may only keep "reasonable excerpts" for internal, non-redistributable use. The terms also forbid removing timestamps, identifiers or watermarks, and using the content to train AI models. **Suggested `terms`:** `no-redistribution`.
- **OPSEC:** Don't share screenshots or commit them. To turn an observation into a record, find an independent source (official statement, NAVTEX, satellite imagery).

## 4. Archiving

The archiving rules are on [06 · Sourcing and Archiving](06-sourcing-archiving.md); this section only covers the tools' terms and OPSEC.

> ⛔ **Don't archive** pages containing personal data, POW/casualty imagery or unofficial content about Turkish forces. Archiving creates a permanent public copy of that content ([02](02-red-lines.md)).

### Wayback Machine — Save Page Now
- **Address:** https://web.archive.org/save
- **What it does:** Saves a snapshot of a single page to the Internet Archive's Wayback Machine.
- **Cost and terms:** Free. According to the [help page](https://help.archive.org/help/using-the-wayback-machine/), Save Page Now saves a page once and doesn't add the site to future crawls. Site owners can request exclusion of archived copies, so a snapshot can become unavailable later. General terms: [Internet Archive terms of use](https://archive.org/about/terms.php). **Suggested `terms`:** an archive inherits the `terms` value of the original source.
- **OPSEC:** Because snapshots can be excluded later, also save to archive.today where possible ([06](06-sourcing-archiving.md)). Check that the snapshot shows the actual content, not a login page or cookie wall.

### archive.today
- **Address:** https://archive.ph/ (the same service also runs under domains such as archive.today, archive.is and archive.md)
- **What it does:** Often captures dynamic pages such as social media better than Wayback, and also stores a screenshot of the page.
- **Cost and terms:** Free, no accounts. The [FAQ](https://archive.ph/faq) says pages are stored "virtually forever", the service is privately funded, and video and audio are not saved. Pages that break the hosting provider's rules may be deleted. **Suggested `terms`:** an archive inherits the `terms` value of the original source.
- **OPSEC — important:** According to the FAQ, when you archive a page **your IP address is passed to the archived site in an `X-Forwarded-For` header.** The site you archive (e.g. a party to a conflict) may see your IP address. Keep this in mind when archiving a sensitive page, and prefer Wayback if needed. The operator is anonymous and permanence isn't guaranteed; don't use it as your only archive.

## 5. Geolocation and chronolocation

For method, see [07 · Geo, Time and Disputed Areas](07-geo-time-disputed.md).

> ⛔ Military facilities in Türkiye and Turkish units are **never** geolocated. Private individuals' homes and workplaces are not geolocated ([02](02-red-lines.md)).

### Google Earth (web)
- **Address:** https://earth.google.com/web/
- **What it does:** High-resolution satellite and aerial imagery, 3D terrain and buildings, distance and area measurement. The basic tool for matching road layouts, buildings and terrain silhouettes in footage.
- **Cost and terms:** Free. The [Google Earth Additional Terms of Service](https://www.google.com/help/terms_maps-earth/) prohibit copying and redistributing content (outside the permissions page and fair use), bulk downloads, and building datasets from the content, including coordinates. They allow content to be displayed publicly online, in video and in print **with proper attribution**. **Suggested `terms`:** `attribution`.
- **OPSEC and limits:** Don't use it while logged in to your personal Google account. Imagery is a mosaic of different dates; write the date of the imagery you matched against into your method description. Screenshots are never committed.

### OpenStreetMap
- **Address:** https://www.openstreetmap.org/
- **What it does:** A community-built open map. Names and tags of roads, buildings, mosques, water towers, power lines and so on help narrow down candidate areas in geolocation, and help find local spellings of place names.
- **Cost and terms:** Free. According to the [copyright and licence page](https://www.openstreetmap.org/copyright), the data is licensed under the Open Database License (ODbL): it may be copied, distributed and adapted with the credit "© OpenStreetMap contributors". If you distribute altered data, it must be under the same licence. **Suggested `terms`:** `open` (with attribution).
- **OPSEC:** OSM edits are recorded **publicly** with username and timestamp. Don't add military facilities to OSM or make edits as part of community work; read only.

### Overpass Turbo
- **Address:** https://overpass-turbo.eu/
- **What it does:** A web interface for querying OpenStreetMap data. It lists candidate locations with queries such as "a mosque and a water tower within 200 m of each other in this district".
- **Cost and terms:** Free, no account. Queries go to the public Overpass API servers. Under the [Overpass API usage policy](https://wiki.openstreetmap.org/wiki/Overpass_API), fewer than 10,000 queries and less than 1 GB of data per day is acceptable use. Commercial users should run their own server, and multiple scripts must not run in parallel. Results are OSM data (ODbL). **Suggested `terms`:** `open` (with attribution).
- **OPSEC:** The servers are busy; don't run needlessly large queries. If you plan to use it in automated collectors, talk to the maintainers first.

### SunCalc
- **Address:** https://www.suncalc.org/
- **What it does:** Calculates the sun's position (altitude, azimuth), sunrise/sunset and shadow length for a chosen place and date, and can work backwards from sun altitude and azimuth to a time. Used for chronolocation from shadows ([07](07-geo-time-disputed.md)).
- **Cost and terms:** Free, no account; a donation-supported site run by an individual in Germany. There is no separate terms-of-use page; see the legal disclosure and privacy policy at the bottom of the site. Its results are facts and are written into the record as method.
- **OPSEC:** SunCalc links carry the coordinates and date in the URL. Sharing a link also shares the location you are studying.

### PeakVisor
- **Address:** https://peakvisor.com/
- **What it does:** 3D mountain panoramas and peak identification. Used to match a mountain skyline in footage against the terrain visible from a given viewpoint.
- **Cost and terms:** Basic features are free; the PRO subscription is paid. Community work uses **free features only**, and no payment method is registered ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)). The [terms of use](https://peakvisor.com/en/terms.html) prohibit abusive or excessive use of the service and infringing others' intellectual property rights. **Suggested `terms`:** `attribution`.
- **OPSEC:** Use a pseudonymous email for features that need an account. Prefer the web version over the mobile app, which asks for location permission.

## 6. Metadata

### ExifTool
- **Address:** https://exiftool.org/
- **What it does:** Reads, edits and removes metadata (EXIF, XMP, GPS, device model, time) in images, videos, PDFs and other files. Used to strip metadata before sending a file to the maintainers ([04 §5](04-opsec.md)):

  ```bash
  exiftool file.jpg          # show metadata
  exiftool -all= file.jpg    # remove all metadata (a file.jpg_original backup remains; delete it too)
  ```

- **Cost and terms:** Free, open source. [Licence](https://exiftool.org/#license): free software that may be redistributed and modified under the same terms as Perl.
- **OPSEC:** Runs **offline** on your computer. Don't upload files to online "EXIF viewer" sites. Compare the checksum of the package you download with the value published on the site. Metadata is easy to alter; it is not proof on its own in chronolocation ([07](07-geo-time-disputed.md)).

## 7. Verification

> ⛔ Reverse image search is **never used for face searches.** Searching for a person's face is an attempt to identify them and breaks the private-individuals rule ([02 §4](02-red-lines.md)). Face recognition services (e.g. PimEyes) are left off this list for that reason.

### InVID-WeVerify verification plugin
- **Address:** https://weverify.eu/verification-plugin/
- **What it does:** A browser extension for video and image verification: keyframe extraction from video, reverse searches on those keyframes across several engines, metadata reading, a magnifier and forensic filters. Developed and maintained by AFP Medialab.
- **Cost and terms:** Free. Built for Chrome; it can be installed in Edge and Opera from the Chrome store. As stated on the [plugin page](https://weverify.eu/verification-plugin/), the software is provided "as is", without warranty.
- **OPSEC:** Browser extensions have broad permissions: install it only from the official store and only in the browser profile you keep for community work. The reverse-search shortcuts send the image to the search engine you choose.

### Reverse image search engines

The first step in catching old footage presented as a new event ([05](05-verification.md)). Engines index different things; try **more than one**.

| Engine | Address | Terms | OPSEC note |
|---|---|---|---|
| TinEye | https://tineye.com/ | [Free for non-commercial use](https://help.tineye.com/article/239-is-tineye-free-to-use); commercial use via a paid API. [Uploaded images are not kept](https://help.tineye.com/article/244-does-tineye-keep-images-i-upload-during-a-search). General terms: [tineye.com/terms](https://tineye.com/terms) | No account needed; the only engine here that explicitly states uploads are deleted after the search. Sorting by date helps find the **oldest copy** of an image. |
| Google Lens / Google Images | https://lens.google.com/ | [Google Terms of Service](https://policies.google.com/terms) | Don't use it while logged in to your personal Google account; searches are linked to your account. |
| Bing Visual Search | https://www.bing.com/images/feed | [Microsoft Services Agreement](https://www.microsoft.com/en-us/servicesagreement) | Don't log in with your personal Microsoft account. |
| Yandex Images | https://yandex.com/images/ | [Yandex User Agreement](https://yandex.com/legal/rules/en/): YANDEX LLC, governed by the law of the Russian Federation | Often strong for imagery from Russia and the former Soviet space. Uploaded images are processed by a company subject to Russian law: don't upload anything that could be sensitive, and don't log in. |

## 8. NOTAM and NAVTEX sources

NOTAMs and NAVTEX messages are **primary official sources** announcing exercise and firing areas ([06](06-sourcing-archiving.md), level 1).

> ⛔ **Exercise and firing notices concerning Turkish forces** (including Turkish NAVTEX messages and NOTAMs) count as official disclosures, but they go through the **Turkish forces gate**. No coordinates are written, and area coordinates from the NAVTEX are never copied into a record. Location precision is `admin1`, `country` or `sea-area` only. The record is held for at least 24 hours and needs maintainer approval ([02 §1](02-red-lines.md)).
>
> NAVTEX messages issued back and forth in the Aegean and Eastern Mediterranean often contain contested claims (jurisdiction, demilitarised status, etc.). Such characterisations go in `claims[]`, attributed to the issuer ([07](07-geo-time-disputed.md)).

### EUROCONTROL EAD Basic (NOTAM)
- **Address:** https://www.ead.eurocontrol.int/
- **What it does:** The public version of the European AIS Database (EAD). Lets you build pre-flight information bulletins (PIBs) from NOTAMs and browse AIP publications.
- **Cost and terms:** Access is through a [free registration form](https://www.ead.eurocontrol.int/cms-eadbasic/opencms/en/ead-solutions/ead-basic/). According to that page, EAD Basic is not connected to the operational database, may not show the latest information, and **must not be used for operational purposes**. **Suggested `terms`:** `attribution`.
- **OPSEC and limits:** Because it may be out of date, check a NOTAM against the relevant country's official aeronautical information publication or another source before putting it in a record. Give only the information the registration form requires.

### NGA Maritime Safety Information — navigational warnings
- **Address:** https://msi.nga.mil/NavWarnings
- **What it does:** Navigational warnings published by the US National Geospatial-Intelligence Agency (NGA). HYDROLANT warnings also cover the Eastern Mediterranean and the Black Sea (e.g. mine, firing and hazardous-operations warnings). Warnings are listed with dates and numbers.
- **Cost and terms:** Free, no account needed. We could not confirm a separate terms-of-use page. **Suggested `terms`:** start with `attribution`.
- **OPSEC and limits:** A secondary compilation of coastal states' warnings. Where possible, also link the issuing coastal state's original broadcast.

### Directorate General of Coastal Safety (Kıyı Emniyeti) — Turkish radio broadcasts (NAVTEX)
- **Address:** https://www.kiyiemniyeti.gov.tr/turk_radyo_yayinlari
- **What it does:** NAVTEX broadcasts from Türkiye's coastal radio stations (İstanbul, İzmir, Antalya, Samsun). Searchable by date, station and language (Turkish/English), with broadcast code, first and last broadcast time, and message text.
- **Cost and terms:** Free, no account needed; an official public source. **Suggested `terms`:** `attribution`.
- **OPSEC:** The gate rules above apply to exercise/firing notices concerning Turkish forces.

### Office of Navigation, Hydrography and Oceanography (ŞNHD) — navigational notices
- **Address:** https://www.shodb.gov.tr/BasinveYayin/SeyirDuyurulari?lang=tr-TR
- **What it does:** NAVTEX and navigational notices from ŞNHD, part of the Turkish Naval Forces Command. Listed by station (Samsun, İstanbul, İzmir, Antalya) and as local notices; an English option is available.
- **Cost and terms:** Free, no account needed. The site notes that the internet is not part of the Maritime Safety Information data flow. The latest, authoritative sources are the NAVTEX and SafetyNET broadcasts. **Suggested `terms`:** `attribution`.
- **OPSEC:** Many of these notices concern Turkish forces' activities: the gate rules above apply **without exception**.

### Hellenic Navy Hydrographic Service (HNHS) — NAVTEX
- **Address:** https://hnhs.gr/category/minimata-navtex/
- **What it does:** NAVTEX messages broadcast from Greece's Heraklion (Crete), Kerkyra (Corfu) and Limnos stations; the primary source for Greek exercise and firing notices.
- **Cost and terms:** Free, no account needed. The site is in Greek; the English interface is limited. The site states that the charts it displays are visual aids only and are not for navigation. **Suggested `terms`:** `attribution`.
- **OPSEC:** If you read the Greek text through machine translation, apply the `i18n.machine` rule in the record ([08](08-style-guide.md)). Contested wording is attributed.

---

## Why isn't it listed?

The following tools were reviewed but not included:

| Tool | Reason |
|---|---|
| Sentinel Hub EO Browser | The service has been deprecated. Its page sends users to the Planet Insights Platform, or to the Copernicus Browser for public data only. The Copernicus Browser is listed above. |
| MarineTraffic | We could not verify its terms-of-use page (access was blocked). Nothing is listed without its terms having been read. |
| FAA NOTAM Search | Our access to the page was blocked (HTTP 403); we could not confirm that it works or check its terms. |
| Face recognition / face search services | Used to identify private individuals; a red line ([02 §4](02-red-lines.md)). |
| Paid tools or trials that require a credit card | Zero-budget principle ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)). |

## Proposing a new tool

1. Check that the tool is free (no payment method registered), legal and passive.
2. **Read** its terms of use or licence; add the link and a summary.
3. Consider how the tool relates to the red lines: if it has a feature that could track Turkish forces or private individuals, prohibit that explicitly in the OPSEC note.
4. Update `tr/11-tools.md` and `en/11-tools.md` **in the same PR**, and change the "Last checked" date.
