# 0021 · Koordinat, kaynağı ve hata payıyla birlikte kaydedilir

> **EN:** Amends [0019](0019-foreign-installations-register.md) §3, which left the foreign-installations register deliberately without coordinates until a separate review. This is that review. A coordinate is open-source intelligence like any other field: where an open, citable source publishes one, it is recorded — together with **who published it, how it was obtained, and how wrong it can be** (`method`, `precision`, `uncertainty_m`, and the source in `sources[]`). What stays forbidden is not the coordinate but the things that turn a register into a target file: geometry we traced ourselves, precision the source does not support, installation footprints, field collection, and anything at all about Turkish forces. The validator changes accordingly: it no longer refuses coordinates on register records, it refuses **unsourced** coordinates on every record.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-20
- **Önerenler:** @nukIeer
- **İlgili:** [0002](0002-git-as-source-of-truth.md), [0006](0006-verification-scale.md), [0009](0009-licensing.md), [0010](0010-content-safety-gates.md), [0011](0011-threat-model.md), [0013](0013-map-layers-turkiye-perspective.md), [0019](0019-foreign-installations-register.md)

## Bağlam

[0019](0019-foreign-installations-register.md) §3 sicili bilerek koordinatsız açtı: "koordinat, kaynağıyla doğrulanmadan yazılmaz" ve gösterim "ayrı bir gözden geçirmeye" bırakıldı. Bu ADR o gözden geçirmedir.

Aradan geçen sürede iki şey netleşti.

**Birincisi, kural yanlış yere konmuştu.** `datasets` doğrulayıcısına konan kapı, belirli etiketleri taşıyan kayıtlarda koordinatı **yasaklıyordu**. Oysa sorun koordinatın varlığı değil, koordinatın **nereden geldiğinin yazılı olmamasıydı**. Aynı depoda, aynı gün, başka bir kayıt (Suda Deniz Üssü) koordinat taşıyordu ve kimse itiraz etmedi; çünkü o koordinat kamuya açık, atıfı verilebilir bir kaynaktan geliyordu. Kapı, kaynaklı koordinatı da kaynaksız koordinatı da aynı şekilde reddediyordu ve bu, doğru olanı da cezalandırıyordu.

**İkincisi, koordinatsız sicil işini yapmıyor.** Sicilin iddiası şudur: bir antlaşma "bu adada istihkâm olmayacak" diyor; açık kaynaklar aksini gösteriyor. Bu iddianın muhatabı — gazeteci, hukukçu, bölge uzmanı, uluslararası kurum — "adada bir şey var" cümlesiyle bir şey yapamaz. "Şu açık kaynağa göre şu noktada, ±şu kadar hatayla, şu tarihten beri" cümlesiyle bir şey yapabilir. Kaynağı ve hata payı yazılı bir koordinat, iddiayı zayıflatmaz; **çürütülebilir**, dolayısıyla ciddiye alınabilir kılar.

Açık kaynak istihbaratının tanımı da budur: açık olan, sistemde olur. OpenStreetMap'in ODbL altında yayımladığı bir koordinat, Yunan Resmî Gazetesi'nin bir ihale ilanındaki adres kadar açıktır; ikisini de kaydetmemek için hiçbir gerekçe yoktur. Kaydetmemek, bilgiyi yok etmez — yalnızca bizim onu göremediğimiz anlamına gelir.

Tehlike başka yerdedir ve yerini şaşırmamak gerekir. Bir sicili hedef dosyasına çeviren şey koordinatın **varlığı** değil, koordinatın **kullanım için üretilmesidir**: kendi ölçtüğümüz ayak izi, kaynağın vermediği hassasiyet, tesis içi yerleşim, yaklaşma güzergâhı, zafiyet sıralaması. [0019](0019-foreign-installations-register.md) §4 bunları zaten kalıcı olarak yasaklar ve bu ADR o yasakların hiçbirine dokunmaz.

## Karar

### 1. Koordinat, açık kaynak verdiği her yerde kaydedilir

Açık ve atıfı verilebilir bir kaynak bir konum yayımlıyorsa, o konum kayda girer. Kaynak sınıfı fark etmez: resmî belge, resmî gazete, antlaşma eki, parlamento cevabı, kurum duyurusu, açık lisanslı harita verisi (OpenStreetMap, ODbL — künyesiyle), açık lisanslı uydu verisi (Copernicus Sentinel), veya bunları aktaran haber kaynağı.

### 2. Her koordinat dört şeyi birlikte taşır

| Alan | Ne söyler |
|---|---|
| `location.geometry` | Konumun kendisi (WGS84, ≤5 ondalık — [0002](0002-git-as-source-of-truth.md)) |
| `location.method` | Nasıl elde edildi — şemanın sözlüğüyle: `geolocated` (kaynak koordinatın kendisini veriyor: koordinat listesi, açık harita verisi, uydu verisi), `reported` (kaynak yeri söylüyor, koordinatı yerin kendisinden alıyoruz), `inferred` (kaynaktan çıkarım yaptık) |
| `location.precision` | Hangi düzeyde: `exact`, `site`, `locality`, `admin2`, `admin1`, `country`, `sea-area` |
| `location.uncertainty_m` | Ne kadar yanlış olabilir, metre cinsinden |

Dördü de zorunludur ve kaynak `sources[]` içinde bulunur. Kaynağın **kim** olduğu `method` alanında değil, `sources[]` içinde durur: yöntem nasıl bilindiğini, kaynak kimin söylediğini söyler. `uncertainty_m`, kaynağın desteklediği hassasiyeti aşamaz: bir ada merkezi için kilometrelerdir, OpenStreetMap'te çizilmiş bir alanın merkezi için yüzlerce metredir, resmî bir koordinat listesinden alınan nokta için on metrelerdir. **Şüphe hâlinde büyük yazılır**; küçük bir `uncertainty_m`, sahip olmadığımız bir kesinliğin iddiasıdır.

### 3. Yasak olan, koordinat değil, kaynağın vermediği kesinliktir

Şunlar üretilmez, kaydedilmez, yayımlanmaz:

1. **Kendi çizdiğimiz geometri.** Uydu görüntüsünden ayak izi çıkarmak, yapı yapı sınır çizmek yoktur. Kayıt bir **nokta ve hata payı** taşır; tesisin şekli değil.
2. **Kaynağın vermediği hassasiyet.** Ada düzeyinde bir bilgiden metre düzeyinde bir koordinat türetilmez; ondalık basamak eklemek bilgi eklemez.
3. **Tesis içi ayrıntı.** Yerleşim planı, giriş noktaları, mühimmat/yakıt tesisleri, yaklaşma güzergâhı, zafiyet veya öncelik değerlendirmesi ([0019](0019-foreign-installations-register.md) §4.3).
4. **Saha toplama** ve **yeniden dağıtımı yasak ticari görüntü** ([0019](0019-foreign-installations-register.md) §4.4, §4.5; [0009](0009-licensing.md)).
5. **Türk kuvvetlerine ait hiçbir konum.** Asimetri kalıcıdır ([0013](0013-map-layers-turkiye-perspective.md); `datasets` coğrafi çit kapısı yürürlükte kalır).

### 4. Doğrulayıcı kapısı değişir

- **Kaldırılan:** `policy.yaml` içindeki `no_coordinate_tags` — belirli etiketli kayıtlarda koordinatı yasaklayan kural.
- **Gelen:** `coordinate_provenance` — `location.geometry` taşıyan **her** kayıtta `method`, `precision`, `uncertainty_m` ve en az bir kaynak zorunludur; `uncertainty_m`, `precision` için tanımlanmış alt sınırın (`coordinate_provenance.min_uncertainty_m`) altına inemez. Alt sınırlar: `exact` 0, `site` 50, `locality` 500, `admin2` 5.000, `admin1` 25.000, `country` 100.000, `sea-area` 10.000 metre.
- **Değişmeyen:** Türk kuvvetleri coğrafi çiti ([0010](0010-content-safety-gates.md)) ve [0019](0019-foreign-installations-register.md) §4'ün tamamı.

### 5. Haritada gösterim

Koordinat taşıyan sicil kayıtları panelde **tesis işareti** olarak çizilir ve tıklanınca kaynağı, yöntemi ve hata payı okunur. Hata payı gösterimin bir parçasıdır: bir nokta, hata payı kilometrelerle ölçülüyorsa nokta gibi değil, **belirsizlik dairesi** gibi çizilir. Kullanıcıya sahip olmadığımız bir kesinliği gösteren bir işaret, yanlış koordinat kadar zararlıdır.

## Sonuçlar

- Sicil ilk kez haritada görünür ve iddiası denetlenebilir hâle gelir: her nokta, kaynağına ve hata payına kadar açılır.
- Kural artık doğru şeyi ödüllendirir: kaynaklı koordinat girer, kaynaksız koordinat — etiketi ne olursa olsun — CI'da düşer. Kapı, sicilden **bütün depoya** genişler.
- `uncertainty_m` zorunluluğu, kaydı yazanı kaynağının ne söylediğini düşünmeye zorlar. Bu, koordinatın kendisinden daha değerli bir disiplindir.
- [0019](0019-foreign-installations-register.md) §3'ün "ilk sürümde koordinatsız" hükmü yürürlükten kalkar; o ADR'nin geri kalanı, özellikle §4 dışlamaları ve §5 dil sınırı, aynen yürürlüktedir.
- Risk dürüstçe: koordinat yayımlamak, yayımlamamaktan daha fazla dikkat çeker. Karşılığı, ciddiye alınabilecek tek türden belge üretmektir. Bir kaydın yanlış çıkması hâlinde düzeltme yolu ([0019](0019-foreign-installations-register.md) sonuçlar, `corrections[]`) zaten kuruludur ve bu ADR onu daha sık kullanacağımızı varsayar.
