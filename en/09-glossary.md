> translation_of: tr/09-glossary.md

# 09 · Glossary

Terms used in records, posts and discussions. Abbreviations are spelled out on first use in text ([08](08-style-guide.md)).

## Intelligence disciplines and method

| English | Turkish | Explanation |
|---|---|---|
| Open-source intelligence (OSINT) | Açık kaynak istihbaratı | Information collected and analysed from publicly available sources. Our community's only method. |
| Geospatial intelligence (GEOINT) | Coğrafi-uzamsal istihbarat | Analysis of maps, satellite imagery and location data. |
| Imagery intelligence (IMINT) | Görüntü istihbaratı | Intelligence derived from aerial and satellite imagery. |
| Signals intelligence (SIGINT) | Sinyal istihbaratı | Interception of electronic signals and communications. A state activity; **we don't do it.** |
| Human intelligence (HUMINT) | İnsan istihbaratı | Collecting information from people. **Out of scope** ([02 §3](02-red-lines.md)). |
| Social media intelligence (SOCMINT) | Sosyal medya istihbaratı | Analysis of public social media content. |
| Geolocation | Geolokasyon | Determining where an image was taken ([07](07-geo-time-disputed.md)). |
| Chronolocation | Kronolokasyon | Determining when an image was taken. |
| Admiralty scale | Admiralty ölçeği | Scale for source reliability (A–F) and information credibility (1–6) ([05](05-verification.md)). |
| Independent source | Bağımsız kaynak | A source that obtained the information through a path separate from another source. |
| Circular reporting | Dairesel raporlama | Sources citing each other so that one piece of information appears multi-sourced. |
| Mosaic effect | Mozaik etkisi | Individually harmless pieces of information combining into a sensitive picture. |
| Operational security (OPSEC) | Operasyon güvenliği | Measures to avoid exposing yourself and the community ([04](04-opsec.md)). |
| Disinformation | Dezenformasyon | False information spread deliberately. |
| Misinformation | Mezenformasyon | False information spread without intent. |
| Sock puppet | Kukla hesap | A fake account hiding its owner's identity. **Never** used to interact with targets. |

## Aviation and maritime

| English | Turkish | Explanation |
|---|---|---|
| ADS-B (Automatic Dependent Surveillance–Broadcast) | ADS-B | System by which aircraft broadcast their position; military aircraft often switch it off. Turkish military aircraft are **not tracked.** |
| AIS (Automatic Identification System) | AIS | Ships' identity and position broadcast; can be switched off or spoofed. Turkish warships are **not tracked.** |
| NOTAM (Notice to Air Missions) | NOTAM | Official notice to aviators (e.g. firing, exercises, closed airspace). |
| NAVTEX (Navigational Telex) | NAVTEX | Broadcast of navigational warnings to mariners (e.g. firing and exercise areas). |
| Flight Information Region (FIR) | Uçuş Bilgi Bölgesi | Airspace in which flight information and alerting services are provided; not a sovereignty zone. |
| Air Defence Identification Zone (ADIZ) | Hava Savunma Tanımlama Bölgesi | Airspace in which a state requests identification. |
| Territorial waters | Karasuları | Belt of sea under the coastal state's sovereignty. Its breadth is disputed in the Aegean. |
| Exclusive Economic Zone (EEZ) | Münhasır Ekonomik Bölge (MEB) | Sea area where the coastal state has sovereign rights over resources. |
| Continental shelf | Kıta sahanlığı | Area of the coastal state's rights over the seabed and subsoil resources. |
| Intercept | Önleme | An aircraft being met by another aircraft for identification/escort. |
| GNSS jamming / spoofing | GNSS karıştırma / aldatma | Suppressing satellite positioning signals / misleading them with fake signals. |

## Platforms and weapons

| English | Turkish | Explanation |
|---|---|---|
| Uncrewed aerial vehicle (UAV) | İnsansız hava aracı (İHA) | Aircraft without an onboard pilot. |
| Armed UAV / UCAV | Silahlı İHA (SİHA) | UAV able to carry munitions. |
| MALE (Medium-Altitude Long-Endurance) | MALE | Class of UAV. |
| HALE (High-Altitude Long-Endurance) | HALE | Class of UAV. |
| Loitering munition | Dolanan mühimmat | Single-use munition that loiters over an area and dives onto a target ("kamikaze drone"). |
| Uncrewed surface vessel (USV) | İnsansız deniz aracı (İDA) | Surface vessel without crew. |
| Ballistic missile | Balistik füze | Missile flying most of its path on a ballistic trajectory. |
| Cruise missile | Seyir füzesi | Guided missile flying within the atmosphere, usually at low altitude. |
| Surface-to-air missile (SAM) | Karadan havaya füze (KHF) | Air defence missile. |
| Electronic warfare (EW) | Elektronik harp (EH) | Use of the electromagnetic spectrum for attack, protection and support. |
| C4ISR | C4ISR | Command, control, communications, computers, intelligence, surveillance and reconnaissance systems. |

## Military activity and procurement

| English | Turkish | Explanation |
|---|---|---|
| Exercise | Tatbikat | Planned military training activity. |
| Deployment | Konuşlanma | Placing units or systems in an area. |
| Order of battle (ORBAT) | Muharebe düzeni | Structure, units and equipment of forces. **Never compiled** for Turkish forces. |
| Procurement | Tedarik | Process of acquiring weapons and equipment. |
| Foreign Military Sales (FMS) | Dış Askerî Satış | US government-to-government arms sales programme. |
| Non-state armed actor | Devlet dışı silahlı aktör | Armed group not part of a state's official forces. |

## Project terms

| English | Turkish | Explanation |
|---|---|---|
| Record | Kayıt | A single YAML file in the `datasets` repository (event, actor, site, equipment, source). |
| Tombstone | Mezar taşı | A `schema: tombstone/1` file replacing a withdrawn record; the ID is never reused. |
| TypeID | TypeID | Permanent record identifier of the form `<prefix>_<26 characters>` ([ADR 0003](../decisions/0003-identifiers.md)). |
| Claim | İddia | A characterisation attributed to a party in `claims[]`. |
| Source registry | Kaynak sicili | `src_` records defining sources with reliability grade and terms of use. |
| Turkish forces gate | Türk kuvvetleri kapısı | CI check for records involving Turkish security bodies ([02](02-red-lines.md)). |
| Bulletin | Bülten | Short, human-approved information post not yet turned into a record ([ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)). |
