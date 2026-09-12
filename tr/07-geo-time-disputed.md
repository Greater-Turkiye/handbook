# 07 · Konum, Zaman ve İhtilaflı Bölgeler

## Geolokasyon (konum belirleme)

Geolokasyon, bir görüntünün **nerede** çekildiğini görüntüdeki ayrıntıları harita ve uydu görüntüleriyle karşılaştırarak belirlemektir.

Temel adımlar:
1. **Görüntüyü inceleyin**: yol düzeni, binalar, minareler, su kuleleri, elektrik hatları, dağ silüetleri, kıyı çizgisi, tabelalar, plakalar (plaka yalnızca ülke/bölge tespiti için; kayda girmez), bitki örtüsü.
2. **Aday bölgeyi daraltın**: kaynağın iddia ettiği yer, dil ve yazı, bilinen olay bölgesi.
3. **Karşılaştırın**: açık uydu görüntüleri (ör. Copernicus Sentinel verisi), ticari haritaların uydu katmanları, OpenStreetMap, sokak düzeyi görüntüler.
4. **En az üç bağımsız eşleşen ayrıntı** bulun (tek bir bina yetmez).
5. **Yöntemi belgeleyin**: hangi ayrıntının neyle eşleştiğini, kullanılan kaynağı ve tarihini yazın. Başka biri adımlarınızı izleyerek aynı sonuca varabilmelidir.

Başka birinin geolokasyonunu kullanıyorsanız, kaynak olarak ona atıf yapın ve sonucu kendiniz kontrol edin.

## Kronolokasyon (zaman belirleme)

Kronolokasyon, bir görüntünün **ne zaman** çekildiğini belirlemektir.

- **Gölgeler**: Gölge yönü ve uzunluğu, konum biliniyorsa güneşin açısından yaklaşık saati verir (güneş konumu hesaplayıcıları).
- **Hava durumu**: Bulut, yağmur, kar — geçmiş hava kayıtlarıyla karşılaştırın.
- **Uydu görüntüsü zaman aralığı**: Bir yapının hasarlı/hasarsız görüldüğü iki uydu geçişi arası.
- **İlk ortaya çıkış**: Görüntünün internette ilk göründüğü an üst sınırdır. Ters görsel aramayla daha eski kopyaları arayın (eski görüntünün yeni olay gibi sunulması en yaygın dezenformasyon türüdür).
- **Dosya meta verisi güvenilmez**: Platformlar çoğu zaman siler; kalanlar da değiştirilebilir.

## Zaman kuralları

- Tüm zamanlar **UTC** ve ISO 8601 biçiminde yazılır: `2026-09-12T14:30:00Z`.
- Yerel saati UTC'ye çevirirken saat dilimi veritabanını kontrol edin; yaz saati uygulamaları ülkeden ülkeye değişir ve zamanla değişebilir. (Örnek: Türkiye yıl boyu UTC+3, İran yıl boyu UTC+3.30'dur.)
- Her zamanın bir **hassasiyet** alanı vardır (ör. dakika, saat, gün, ay). Sadece tarihi biliyorsanız hassasiyeti **gün** olarak işaretleyin; saati `00:00` diye uydurmayın.
- **Olay zamanı** ile **yayın zamanı** farklıdır. Kayıt olay zamanını tutar. Yalnızca yayın zamanı biliniyorsa bunu belirtin ve hassasiyeti düşürün.
- Süren olaylar (tatbikat, konuşlanma) için başlangıç ve bitiş ayrı kaydedilir; bitiş bilinmiyorsa boş bırakılır.

## Konum kuralları

- Koordinatlar **WGS 84** ondalık derece (enlem, boylam) olarak yazılır.
- **En fazla 5 ondalık basamak** (yaklaşık 1 metre). Daha fazlası sahte bir kesinlik izlenimi verir; CI reddeder.
- Koordinat, gerçek hassasiyetten daha kesin olamaz. Bir kasabada olduğu bilinen bir olay için bina koordinatı vermeyin.

### Konum hassasiyeti (`precision`)

| Değer | Anlamı | Koordinat |
|---|---|---|
| `exact` | Geolokasyonla belirlenmiş nokta (yaklaşık 100 m içinde) | Evet |
| `site` | Bilinen bir tesis (üs, liman, havaalanı) | Tesisin merkezi |
| `locality` | Yerleşim yeri (köy, kasaba, şehir) | Yerleşimin merkezi |
| `admin2` | İlçe düzeyi idari birim | İdari birimin merkezi veya yok |
| `admin1` | İl/eyalet/vilayet düzeyi | Koordinat verilmez |
| `country` | Yalnızca ülke biliniyor | Koordinat verilmez |
| `sea-area` | Deniz alanı (ör. "Doğu Akdeniz", "Kuzey Ege") | Koordinat verilmez |

> **Türk kuvvetleri kapısı:** Türk güvenlik unsurlarının dahil olduğu kayıtlarda yalnızca `admin1`, `country` veya `sea-area` kullanılabilir ve koordinat bulunamaz ([02](02-red-lines.md)).

Hassasiyeti düşürmek her zaman serbesttir; yükseltmek kanıt gerektirir.

## `countries` alanı

`countries`, **aktörleri olaya dahil olan devletleri** listeler; olayın yerinin kime ait olduğunu **değil**.

- Yunan savaş gemisinin Doğu Akdeniz'deki bir tatbikatı → `countries: [GRC]` (tatbikata katılan başka devletler varsa onlar da).
- Rus ve Ukrayna kuvvetleri arasında Karadeniz'de bir olay → `countries: [RUS, UKR]`.
- Yer bilgisi `location` alanındadır ve egemenlik iddiası taşımaz.

Ülke kodları **ISO 3166-1 alpha-3**'tür. İstisnalar:

| Kod | Etiket (TR) | Etiket (EN) |
|---|---|---|
| `XNC` | KKTC (Kuzey Kıbrıs Türk Cumhuriyeti) | TRNC (Turkish Republic of Northern Cyprus) |
| `CYP` | GKRY (Güney Kıbrıs Rum Yönetimi) | GKRY / Greek Cypriot Administration of Southern Cyprus |

`XNC`, ISO standardında olmayan bir proje kodudur.

## İhtilaflı bölgeler politikası

1. **Kayıt egemenlik iddia etmez.** Bir yerin kime ait olduğunu, sınırın nereden geçtiğini, bir deniz alanının kimin yetki alanında olduğunu proje kendi sesiyle söylemez.
2. **İddialar atfedilir.** "X, olayın kendi münhasır ekonomik bölgesinde gerçekleştiğini açıkladı; Y bu alanın kendi kıta sahanlığında olduğunu belirtiyor." Bu tür ifadeler `claims[]` içindedir.
3. **Etiketlerde Türkiye'nin resmî terminolojisi kullanılır.** Bu, bir egemenlik iddiası değil, projenin yayın dilidir: KKTC, GKRY, Ege adaları, Kardak Kayalıkları vb. Türkiye'nin resmî bir terimi olmayan yerlerde, yaygın ve tarafsız ad kullanılır.
4. **Sınır veya deniz yetki alanı çizgisi yayımlanmaz.** Harita katmanlarımız tartışmalı sınır, MEB veya kıta sahanlığı çizgisi içermez.
5. **Yer adları üç katmanlıdır:**
   - `tr`: Türkçe ad (varsa Türkçe exonym),
   - `en`: İngilizce ad (Türkiye'nin resmî İngilizce kullanımı varsa o),
   - `local`: yerel dilde ve yazıda ad.

### Örnekler

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

Aynı adı taşıyan farklı yerleri (Trablus/Trablusşam gibi) karıştırmamak için gerektiğinde ülke adını parantez içinde ekleyin.

### Özel durumlar

- **Kıbrıs**: KKTC ve GKRY etiketleri kullanılır. Yerel adlar hem Türkçe hem Rumca olabilir; KKTC'deki yerler için `local` Türkçedir.
- **Ege**: Türkiye ile Yunanistan arasında karasuları genişliği, hava sahası, FIR sorumluluğu, kıta sahanlığı, adaların askerden arındırılmış statüsü ve egemenliği antlaşmalarla devredilmemiş ada, adacık ve kayalıklar (EGAYDAAK) gibi konularda anlaşmazlıklar vardır. Bu konulardaki her nitelendirme (ör. "hava sahası ihlali", "FIR ihlali") atfedilir.
- **Doğu Akdeniz ve Karadeniz**: Deniz yetki alanı iddiaları atfedilir; olay yeri `sea-area` veya koordinat ile verilir.
- **Başka ülkeler arasındaki ihtilaflar** (ör. Kırım, Golan, Batı Şeria): Etiketlerde Türkiye'nin resmî tutumuyla uyumlu ad kullanılır; tarafların iddiaları atfedilir.
