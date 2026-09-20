# 0020 · Site: Cloudflare Worker'ından da sunulur, GitHub Pages kanonik kalır

> **EN:** The static site is now also served by a Cloudflare Worker (`gt-site`) that sends our own headers (CSP, referrer policy, per-type cache lifetimes) and proxies the dataset export onto the same origin as the page that reads it. This is not a migration: GitHub Pages remains the canonical address and both serve the same files from the same commit, so either can carry the site alone. The reason to have the second path at all is control, not capacity — Pages cannot send a header we choose, and a project whose whole claim is "check us" should be able to set its own content security policy.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-20
- **Önerenler:** @nukIeer
- **İlgili:** [0008](0008-zero-budget-infrastructure.md), [0011](0011-threat-model.md), [0018](0018-self-hosted-vector-basemap.md)

## Bağlam

Site bugüne kadar yalnızca GitHub Pages'te durdu ve iyi durdu: ücretsiz, hızlı, bakımsız. Ancak
proje büyüdükçe üç sınır göründü.

1. **Başlıklar bizim değil.** Pages, içerik güvenliği politikası (CSP), `referrer-policy` veya
   dosya türüne göre önbellek süresi göndermemize izin vermez. "Bize bakın, denetleyin" diyen bir
   projenin, sayfasının ne yükleyip ne yükleyemeyeceğini kendisinin söyleyememesi tuhaftır.
2. **Veri başka bir kökende.** Panel, veri dışa aktarımını `../datasets/` üzerinden ister; bu, her
   ziyaretçi için ikinci bir kökene çapraz istek demektir ve önbellek davranışı bizim elimizde
   değildir.
3. **Sistem dağıldı.** Karolar ([0018](0018-self-hosted-vector-basemap.md)) ve veri hattı Worker'ları
   Cloudflare hesabında; sayfa Pages'te. Üç adres, tek sistem.

Aynı anda, Pages'i bırakmak için bir sebep yok: ücretsiz, güvenilir ve deponun kendisinden yayımlanır.
Bir dağıtım yolunu kapatmak, dayanıklılığı azaltmak demektir.

## Karar

### 1. İki yol, tek kaynak

Site hem GitHub Pages'ten hem `gt-site` Worker'ından sunulur
([`platform/apps/site`](https://github.com/Greater-Turkiye/platform/tree/main/apps/site)). İkisi de
`apps/web` dizinini **aynı commit'ten** yayımlar; farklı bir derleme, farklı bir içerik veya farklı
bir sürüm yoktur. Biri düşerse diğeri siteyi tek başına taşır.

### 2. Kanonik adres Pages'te kalır

Paylaşılan bağlantı, atıf verilen adres ve arama motorlarının göreceği yer
`greater-turkiye.github.io` olmayı sürdürür. `*.workers.dev` adresi kanonik değildir. Bir alan adı
alınır ve Cloudflare'e yönlendirilirse bu karar yeniden yazılır; o zamana kadar ikinci yol bir
yedek ve bir kontrol noktasıdır.

### 3. Worker'ın yaptığı üç şey

- **Kendi başlıklarımız:** CSP (`script-src 'self'`, `connect-src` yalnızca kendi kökeni, karo
  Worker'ı ve veri kökeni, `frame-ancestors 'none'`), `referrer-policy: no-referrer`, `nosniff` ve
  dosya türüne göre `cache-control` (yazı tipi/kütüphane bir hafta, diğer varlıklar bir saat, sayfa
  beş dakika).
- **Aynı kökende veri:** `/datasets/<dosya>` isteği Worker tarafından veri kökeninden çekilir ve
  kenarda önbelleklenir; tarayıcı çapraz istek yapmaz.
- **Başka hiçbir şey.** Sırrı yoktur, yazmaz, veritabanı okumaz.

### 4. Vekil beyaz listeyle çalışır

Veri vekili yalnızca adı bilinen dışa aktarım dosyalarını geçirir (`manifest.json`, `*.jsonl`,
`events.csv`, `events.geojson`, `vocab.json`, `feed.xml|json|md`). Ziyaretçinin verdiği hiçbir URL
getirilmez; bu, açık bir vekilin başkasının içeriğini bizim adımıza sunmasını en baştan imkânsız
kılar ([0011](0011-threat-model.md)).

## Sonuçlar

- Site artık kendi içerik güvenliği politikasını gönderiyor: sayfaya sonradan bir analitik betiği ya
  da üçüncü taraf yazı tipi sızsa bile tarayıcı onu yüklemez.
- Panel veriyi kendi kökeninden okur; çapraz istek ve ona bağlı önbellek belirsizliği kalkar.
- İki dağıtım yolu, iki farklı arıza modu demektir: Pages'in durması ya da Cloudflare hesabının
  askıya alınması siteyi tek başına yere sermez.
- Maliyet değişmez: statik varlık istekleri Workers ücretsiz katman sayacına girmez, vekil ise dosya
  başına kenar başına bir kez üst kaynağa gider.
- İki yolu **aynı commit'ten** yayımlamak bir disiplindir: `apps/web` dışında bir "canlı düzenleme"
  yapılırsa iki adres birbirinden ayrılır. Bu yüzden dağıtım tek komuttur ve elle dosya kopyalanmaz.
