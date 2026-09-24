# Kararlar (ADR)

> **EN:** Architecture/organisation decision records for Greater Türkiye. Written in Turkish; each file starts with a one-line English summary. Propose a new one by PR using the template.

Bu klasör, topluluğun **mimari ve örgütsel kararlarını** (Architecture Decision Records, ADR) içerir. Her karar; bağlamı, verilen kararı, sonuçlarını ve değerlendirilen alternatifleri kısa ve kalıcı biçimde kaydeder. Amaç, "bunu neden böyle yaptık?" sorusunun cevabının bir yerde yazılı olmasıdır.

## Dizin

| No | Başlık | Durum | Tarih |
|---|---|---|---|
| [0000](0000-template.md) | Şablon | — | — |
| [0001](0001-repository-boundaries.md) | Depo sınırları | Kabul edildi | 2026-09-12 |
| [0002](0002-git-as-source-of-truth.md) | Tek doğruluk kaynağı olarak git | Kabul edildi | 2026-09-12 |
| [0003](0003-identifiers.md) | Tanımlayıcılar | Kabul edildi | 2026-09-12 |
| [0004](0004-schema-versioning.md) | Şema sürümleme | Kabul edildi | 2026-09-12 |
| [0005](0005-controlled-vocabularies.md) | Kontrollü sözlükler | Kabul edildi | 2026-09-12 |
| [0006](0006-verification-scale.md) | Doğrulama ölçeği | Kabul edildi | 2026-09-12 |
| [0007](0007-human-in-the-loop-publishing.md) | İnsan onaylı yayın | Kabul edildi | 2026-09-12 |
| [0008](0008-zero-budget-infrastructure.md) | Sıfır bütçe altyapı | Kabul edildi (toplayıcı tetikleyicisi: 0016) | 2026-09-12 |
| [0009](0009-licensing.md) | Lisanslama | Kabul edildi | 2026-09-12 |
| [0010](0010-content-safety-gates.md) | İçerik güvenliği kapıları | Kabul edildi | 2026-09-12 |
| [0011](0011-threat-model.md) | Tehdit modeli | Kabul edildi | 2026-09-12 |
| [0012](0012-governance.md) | Yönetişim | Kabul edildi | 2026-09-12 |
| [0013](0013-map-layers-turkiye-perspective.md) | Harita katmanları: Türkiye perspektifi | Kabul edildi | 2026-09-13 |
| [0014](0014-occupied-territory-and-human-rights-markers.md) | Harita: işgal altındaki topraklar, insan hakları işaretleri, tampon bölgeler | Kabul edildi (§3 yerine geçildi: 0015) | 2026-09-13 |
| [0015](0015-announced-operation-areas.md) | Harita: Türkiye'nin resmî olarak ilan ettiği harekât bölgeleri | Kabul edildi | 2026-09-13 |
| [0016](0016-collector-schedule-until-worker.md) | Toplayıcılar: Worker gelene kadar GitHub Actions `schedule:` | Kabul edildi | 2026-09-16 |
| [0017](0017-osint-ai-repository.md) | `osint-ai` deposu ve görüntü yapay zekâsı kuralları | Önerildi | 2026-09-18 |
| [0018](0018-self-hosted-vector-basemap.md) | Vektör altlık: karoları kendimiz üretir, kendimiz sunarız | Kabul edildi | 2026-09-19 |
| [0019](0019-foreign-installations-register.md) | Yabancı askerî tesis sicili: antlaşma çerçevesi, kanıt standardı ve dışlamalar | Kabul edildi | 2026-09-19 |
| [0020](0020-site-on-cloudflare-alongside-pages.md) | Site: Cloudflare Worker'ından da sunulur, GitHub Pages kanonik kalır | Kabul edildi | 2026-09-20 |
| [0021](0021-coordinates-with-provenance.md) | Koordinat, kaynağı ve hata payıyla birlikte kaydedilir | Kabul edildi | 2026-09-20 |
| [0022](0022-trade-compliance-not-vessel-tracking.md) | Ticaret uyumu izlenir, sivil gemi takip edilmez | Kabul edildi | 2026-09-20 |
| [0023](0023-automatic-unverified-records.md) | Doğrulanmamış kayıtların otomatik yayını | Kabul edildi | 2026-09-24 |
| [0024](0024-automatic-records-without-a-language-model.md) | Dil modeli olmadan otomatik kayıt | Kabul edildi | 2026-09-24 |

## Yeni bir ADR nasıl önerilir?

1. [`0000-template.md`](0000-template.md) dosyasını kopyalayın; bir sonraki boş numarayı ve kısa, İngilizce ASCII kebab-case bir ad verin: `NNNN-kisa-ad.md`.
2. Durumu **Önerildi** olarak yazın. Bağlamı, kararı, sonuçları ve alternatifleri doldurun. En üste tek satırlık İngilizce özet ekleyin.
3. Bu depoya bir PR açın; yukarıdaki dizine satır ekleyin.
4. Tartışma PR üzerinde yürür. Bakımcılar oydaşmayla karar verir ([0012](0012-governance.md)); kabul edilirse durum **Kabul edildi** ve tarih birleştirme günü olur.
5. Gizli bilgi, kişisel veri veya güvenlik açığı içeren konular PR'da değil, [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) kanalıyla önce bakımcılara iletilir.

## Kurallar

- Kabul edilmiş bir ADR **düzenlenmez** (yazım hatası hariç). Karar değişirse yeni bir ADR yazılır; eskisinin durumu **"Yerine geçildi: NNNN"** olarak güncellenir.
- Durum değerleri: `Önerildi` · `Kabul edildi` · `Reddedildi` · `Kullanımdan kalktı` · `Yerine geçildi: NNNN`.
- "Temel değişiklikler" (depo yapısı, veri modeli, doğrulama kuralları, kırmızı çizgiler, lisans, yönetişim, altyapı maliyeti) **mutlaka** ADR gerektirir.
