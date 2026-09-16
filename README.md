# Greater Türkiye El Kitabı / Handbook

**TR** · [EN](#english)

## Türkçe

**Greater Türkiye**, Türkiye'nin **dış** güvenlik ortamını yalnızca açık kaynaklardan izleyen, gönüllülerle yürüyen, bütçesiz bir açık kaynak istihbaratı (OSINT) topluluğudur. Yabancı orduları, komşu bölgeleri, tedarik projelerini, tatbikatları, konuşlanmaları ve olayları kayıt altına alır; her kaydı kaynaklandırır, arşivler ve doğrulama derecesiyle birlikte yayımlarız. Türk kuvvetlerini izlemeyiz. Hiçbir devlet kurumuyla bağlantımız yoktur.

Bu depo topluluğun kurallarını, yöntemlerini ve kararlarını içerir. **Türkçe sayfalar esastır**; İngilizce sayfalar çeviridir ve her biri hangi Türkçe sayfanın çevirisi olduğunu ilk satırında belirtir.

> İlk kez mi geldiniz? Önce [Kırmızı Çizgiler](tr/02-red-lines.md), sonra [Katkı Rehberi](tr/10-contributing.md) sayfasını okuyun.

### Sayfalar

| # | Sayfa | Konu |
|---|---|---|
| 01 | [Misyon ve Kapsam](tr/01-mission-scope.md) | Ne yapıyoruz, ne yapmıyoruz, izlenen bölgeler |
| 02 | [Kırmızı Çizgiler](tr/02-red-lines.md) | Mutlak kurallar — **zorunlu okuma** |
| 03 | [Hukuk ve Etik](tr/03-legal-ethics.md) | İlgili mevzuata dair farkındalık, etik ilkeler |
| 04 | [Operasyonel Güvenlik (OPSEC)](tr/04-opsec.md) | Katkıcıların kendini koruması |
| 05 | [Doğrulama](tr/05-verification.md) | Admiralty ölçeği, durum değerleri, tahmin dili |
| 06 | [Kaynaklandırma ve Arşivleme](tr/06-sourcing-archiving.md) | Kaynak hiyerarşisi, kaynak sicili, arşiv bağlantıları |
| 07 | [Konum, Zaman ve İhtilaflı Bölgeler](tr/07-geo-time-disputed.md) | Geolokasyon, kronolokasyon, hassasiyet, terminoloji |
| 08 | [Yazım Kılavuzu](tr/08-style-guide.md) | Kayıt ve paylaşım yazımı, düzeltmeler |
| 09 | [Sözlük](tr/09-glossary.md) | OSINT ve savunma terimleri |
| 10 | [Katkı Rehberi](tr/10-contributing.md) | Adım adım katkı, roller ve terfi yolu |
| 11 | [Araçlar](tr/11-tools.md) | Ücretsiz ve yasal OSINT araçları, koşulları, OPSEC notları |

### Kararlar (ADR)

Mimari ve örgütsel kararlar [`decisions/`](decisions/README.md) klasöründedir.

| No | Karar |
|---|---|
| 0001 | [Depo sınırları](decisions/0001-repository-boundaries.md) |
| 0002 | [Tek doğruluk kaynağı olarak git](decisions/0002-git-as-source-of-truth.md) |
| 0003 | [Tanımlayıcılar](decisions/0003-identifiers.md) |
| 0004 | [Şema sürümleme](decisions/0004-schema-versioning.md) |
| 0005 | [Kontrollü sözlükler](decisions/0005-controlled-vocabularies.md) |
| 0006 | [Doğrulama ölçeği](decisions/0006-verification-scale.md) |
| 0007 | [İnsan onaylı yayın](decisions/0007-human-in-the-loop-publishing.md) |
| 0008 | [Sıfır bütçe altyapı](decisions/0008-zero-budget-infrastructure.md) |
| 0009 | [Lisanslama](decisions/0009-licensing.md) |
| 0010 | [İçerik güvenliği kapıları](decisions/0010-content-safety-gates.md) |
| 0011 | [Tehdit modeli](decisions/0011-threat-model.md) |
| 0012 | [Yönetişim](decisions/0012-governance.md) |

### Depolar

| Depo | İçerik |
|---|---|
| [`.github`](https://github.com/Greater-Turkiye/.github) | Organizasyon profili, şablonlar, davranış kuralları, `SECURITY.md` |
| [`handbook`](https://github.com/Greater-Turkiye/handbook) | Bu el kitabı ve kararlar |
| [`datasets`](https://github.com/Greater-Turkiye/datasets) | Doğrulanmış kayıtlar, şemalar, sözlükler, `tools/gt.py` |
| [`platform`](https://github.com/Greater-Turkiye/platform) | Toplayıcılar, yayıncılar, API, web (gelecekte) |

### Lisans

El kitabının içeriği [CC BY 4.0](LICENSE) lisanslıdır. Bu depoya çekme isteği (PR) açmak, katkınızın aynı lisansla yayımlanmasını kabul etmek anlamına gelir.

---

## English

**Greater Türkiye** is a volunteer-run, zero-budget open-source intelligence (OSINT) community that monitors Türkiye's **external** security environment from public sources only. We record foreign militaries, neighbouring regions, procurement, exercises, deployments and incidents; every record is sourced, archived and published with an explicit verification grade. We do not monitor Turkish forces. We are not affiliated with any state body.

This repository holds the community's rules, methods and decisions. **Turkish pages are canonical**; English pages are translations and each one names its Turkish original on its first line.

> New here? Read the [Red Lines](en/02-red-lines.md) first, then the [Contributing guide](en/10-contributing.md).

### Pages

| # | Page | Topic |
|---|---|---|
| 01 | [Mission and Scope](en/01-mission-scope.md) | What we do, what we don't, monitored regions |
| 02 | [Red Lines](en/02-red-lines.md) | Absolute rules — **mandatory reading** |
| 03 | [Law and Ethics](en/03-legal-ethics.md) | Awareness of relevant law, ethical principles |
| 04 | [Operational Security (OPSEC)](en/04-opsec.md) | Protecting yourself as a contributor |
| 05 | [Verification](en/05-verification.md) | Admiralty scale, status values, estimative language |
| 06 | [Sourcing and Archiving](en/06-sourcing-archiving.md) | Source hierarchy, source registry, archive links |
| 07 | [Geo, Time and Disputed Areas](en/07-geo-time-disputed.md) | Geolocation, chronolocation, precision, terminology |
| 08 | [Style Guide](en/08-style-guide.md) | Writing records and posts, corrections |
| 09 | [Glossary](en/09-glossary.md) | OSINT and defence terms |
| 10 | [Contributing](en/10-contributing.md) | Step-by-step contributing, roles and promotion |
| 11 | [Tools](en/11-tools.md) | Free, legal OSINT tools, their terms and OPSEC notes |

### Decisions (ADRs)

Architecture and organisation decisions live in [`decisions/`](decisions/README.md) (written in Turkish, each with a one-line English summary). See the table in the Turkish section above for the full list.

### Licence

Handbook content is licensed under [CC BY 4.0](LICENSE). Opening a pull request means you agree to publish your contribution under the same licence.

## Depo kurallari / Repository rules

Yapay zeka araclari ve yeni katkicilar icin kisa calisma kurallari: [CLAUDE.md](CLAUDE.md). Bu kurallarin ilki, her degisiklikte README dosyasini ayni PR icinde guncel tutmaktir.
Short working rules for AI agents and new contributors: [CLAUDE.md](CLAUDE.md). The first of them is keeping the README true in the same pull request as the change.
