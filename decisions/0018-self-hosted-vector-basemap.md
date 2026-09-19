# 0018 · Vektör altlık: karoları kendimiz üretir, kendimiz sunarız

> **EN:** The dashboard's basemap is ours: an OpenStreetMap extract of the panel's region (z0–11), cut with go-pmtiles from the Protomaps planet build, published as a release asset and served by the `gt-tiles` Worker. It is on by default; no visitor request goes to a third-party map service. Boundary and country-name layers are dropped from the style before the map is created (0013 stands): the basemap carries geography, we carry meaning. The archive lives in a release asset only because R2 is not enabled on the account; moving it there is a binding and one line, and needs no new decision.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-19
- **Önerenler:** @nukIeer
- **İlgili:** [0008](0008-zero-budget-infrastructure.md), [0009](0009-licensing.md), [0013](0013-map-layers-turkiye-perspective.md)

## Bağlam

Panel bugüne kadar haritayı yalnızca depoda duran 1:50m Natural Earth dosyasından çizdi. O dosya ülke ölçeğinde doğrudur ama kıyı çizgisi genelleştirilmiştir, yol yoktur, yerleşim yoktur: harita yakınlaştırıldığında elde edilen şey büyütülmüş bir taslaktır. Bir OSINT panelinde bir olayın "Münbiç'in kuzeyi" mi "Fırat'ın doğusu" mu olduğu, altlıkta o coğrafya çizilmiyorsa gösterilemez.

Üç seçenek vardı:

1. **Üçüncü taraf karo servisi** (OpenFreeMap gibi): hemen çalışır, bedava, anahtarsız — ama her ziyaretçinin harita isteği başkasının sunucusuna gider, SLA yoktur ve servis kapanırsa harita kaybolur.
2. **Ticari servis** (Mapbox vb.): sıfır bütçeyle ([0008](0008-zero-budget-infrastructure.md)) bağdaşmaz; ücretsiz katman bir kredi kartına ve kotaya bağlıdır.
3. **Karoları kendimiz üretip sunmak:** OpenStreetMap verisinden bölgesel bir kesit alıp kendi altyapımızdan sunmak.

Ölçüm, üçüncü seçeneğin sanıldığı kadar pahalı olmadığını gösterdi: paneldeki dikdörtgenin z0–11 kesiti 709 MB'dır ve PMTiles biçimi, karoların tek bir dosyadan HTTP bayt aralıklarıyla okunmasını sağlar; yani "sunucu" tek bir dosya ve önünde küçük bir Worker demektir.

## Karar

### 1. Altlık bizimdir ve varsayılan açıktır

Panel, haritayı kendi ürettiğimiz vektör karolar üzerine çizer. Karolar `gt-tiles` Cloudflare Worker'ından gelir ([`platform/apps/tiles`](https://github.com/Greater-Turkiye/platform/tree/main/apps/tiles)); ziyaretçinin hiçbir harita isteği üçüncü tarafa gitmez. `?basemap=0` altlığı kapatır, `?basemap=ofm` karşılaştırma için OpenFreeMap'i açar.

### 2. Anlam bizde kalır — 0013 aynen geçerlidir

Altlık yalnızca **coğrafya** taşır: kıyı, su, arazi, yol, yerleşim adı. Sınır katmanları ve ülke/bölge adları, harita kurulmadan **önce** stilden çıkarılır; ekranda görünen her sınır, ülke adı, deniz adı ve her tematik alan bizim kaynaklı verimizden D3 ile üstte çizilir ([0013](0013-map-layers-turkiye-perspective.md)). Yerleşim adları kalır — bir şehir adı egemenlik iddiası değildir — ve önce Türkçe sorulur.

Harita belirli bir yakınlıktan sonra (k ≥ 6) 50m dosyadan gelen kara dolgularını ve kıyı çizgisini söndürür: altta sokak sokak ölçülmüş bir kıyı, üstte genelleştirilmiş bir kıyı varken ikisinin çakışması haritayı yanlış gösterir.

### 3. Kaynak ve künye

Karolar OpenStreetMap verisinin türetilmiş çalışmasıdır: **© OpenStreetMap contributors, ODbL 1.0.** Künye TileJSON'da sunulur ve haritanın üzerinde görünür kalır; kaldırılması bir hata değil, lisans ihlalidir ([0009](0009-licensing.md)). Kesit, Protomaps'in günlük gezegen derlemesinden `go-pmtiles` ile alınır; hiçbir geometri bizim tarafımızdan yeniden çizilmez.

### 4. Arşiv nerede durur

Arşiv bugün `platform` deposunun bir **sürüm varlığıdır** (`basemap-<YYYYMMDD>`): ücretsizdir, HTTP Range destekler, dosya başına 2 GB sınırı bu arşiv için fazlasıyla yeterlidir. Tercih edilen yer R2'dir; R2 hesapta açık olmadığı için (panelden açılması ve kart gerektirir) bugün kullanılamıyor. Worker her iki kökeni de okur: `ARCHIVES` içindeki değer `https://…` ise sürüm varlığı, `r2:<anahtar>` ise bucket. **Taşıma yeni bir karar gerektirmez**; istemci URL'leri değişmez.

### 5. Yenileme elle yapılır

Arşiv, OSM verisi eskidiğinde elle yeniden üretilir ([`tools/geo/build_basemap.md`](https://github.com/Greater-Turkiye/platform/blob/main/tools/geo/build_basemap.md)). Arşiv kimliği derleme tarihini taşır, yani her yenileme yeni bir URL kümesidir: hiçbir önbellek geçersiz kılınmaz, eski arşiv silinene kadar çalışmaya devam eder. Otomatik bir cron yoktur; 700 MB'lık bir varlığı gece yarısı sessizce değiştirmek, kazanılan tazelikten daha büyük bir risktir.

### 6. Altlık yoksa harita yine çalışır

Karolar erişilemezse panel altlığı düşürür ve haritayı depodaki 50m dosyadan çizmeye döner; şehir adlarını da kendi tablomuzdan (`places-10m.geojson`, Türkçe adlar bizim) gösterir. Altlık bir bağımlılık değil, bir iyileştirmedir.

## Sonuçlar

- Harita, kayıtların geçtiği coğrafyayı gösterebilecek derinliğe kavuşur; panelin zum aralığı 16×'ten 192×'e açılır.
- İlk açılışın ağırlığı değişmez: altlık ilk zumla gelir, yani "harita derinleşti" ile "sayfa yavaşladı" birlikte olmaz.
- Ziyaretçi verisi üçüncü taraf harita servisine gitmez.
- Maliyet sıfır kalır, ama iki tavan izlenmelidir: Workers ücretsiz katmanında günde 100k istek ve sürüm varlığı başına 2 GB.
- Yenilemenin elle olması, altlığın eskimesi anlamına gelebilir; OSM verisinin tarihi TileJSON'da ve `apps/tiles/README.md` içinde yazılıdır, böylece "ne kadar eski" sorusu ölçülebilir kalır.
- Vendor'daki `pmtiles.js` gerekmez ve kaldırılmıştır: arşivi tarayıcı değil, Worker okur.
