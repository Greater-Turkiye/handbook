# 0017 · `osint-ai` deposu ve görüntü yapay zekâsı kuralları

> **EN:** Creates `Greater-Turkiye/osint-ai` for imagery-based OSINT candidate detection, and sets its rules: model output is a proposal that enters the **existing** `gt-ops.reviews` queue and is never published (0007); imagery analysis is gated by its own Türkiye geofence at 15 nm and refuses rather than crops; only openly licensed, redistributable-as-derived-features imagery is used, and only derived features and hashes are stored, never imagery; zero budget means open-weight models on free GPUs only, and training a foundation model from scratch or running a 32B+ model is recorded as impossible rather than deferred.

- **Durum:** Önerildi
- **Tarih:** 2026-09-18
- **Önerenler:** @nukIeer
- **İlgili:** [0001](0001-repository-boundaries.md), [0007](0007-human-in-the-loop-publishing.md), [0008](0008-zero-budget-infrastructure.md), [0009](0009-licensing.md), [0010](0010-content-safety-gates.md), [0011](0011-threat-model.md), [0013](0013-map-layers-turkiye-perspective.md), [0015](0015-announced-operation-areas.md)

## Bağlam

Topluluğun hedefi, açık uydu görüntülerinden OSINT adayları çıkarabilen bir hattın kurulmasıdır: "milyonlarca harita/uydu görüntüsünü tarayan" bir yapay zekâ. Bu hedef bugünkü depoların hiçbirine tam oturmuyor. `platform` metin sinyallerini toplar ve inceleme kuyruğunu işletir; `datasets` doğrulanmış kayıtları tutar; görüntü işleme her ikisinden de farklı bir bağımlılık kümesi (model ağırlıkları, GPU oturumu, gigabaytlık okuma) ve farklı bir risk profili getirir. [0001](0001-repository-boundaries.md)'in depo sınırları gerekçesi burada da geçerlidir: ayrı bir sorumluluk, ayrı bir depo.

Karar verilmesi gereken asıl mesele depo adı değil, **kurallardır.** Görüntü analizi üç yerde metin toplayıcılarından ayrılır:

1. **Coğrafi çit.** Bir metin sinyali bir noktadır; bir uydu sahnesi bir alandır. Nokta bazlı süzgeç, alan tabanlı bir girdi için yeterli değildir.
2. **Lisans.** Ticari görüntü ve web harita altlıkları (Google, Bing, Yandex) hem ücretlidir hem de türetilmiş ürünün yeniden dağıtımını yasaklar. "Kamuya açık" ile "yeniden dağıtılabilir" aynı şey değildir.
3. **Maliyet.** Görüntü işleme, [0008](0008-zero-budget-infrastructure.md)'in ücretsiz katman tavanlarına metin toplamadan çok daha hızlı çarpar. Bir mimari önerisinin, nerede tükendiğini sayıyla söylemesi gerekir.

Karar verilmezse, bu iş ya yanlış depoda büyür ya da kuralları sonradan, ilk ihlalden sonra yazılır.

## Karar

### 1. Depo

`Greater-Turkiye/osint-ai` açık bir depo olarak kurulur. Kod MIT, belge ve veri CC BY 4.0 ([0009](0009-licensing.md)). Depo bugün **tasarım aşamasındadır**: eğitilmiş model, model çıkarımı ve indirilmiş görüntü içermez; belgeleri ile kırmızı çizgi kapısını ve ücretsiz katalog aramasını çalıştıran küçük bir Python iskeleti içerir.

### 2. İnsan onayı — yeni kuyruk açılmaz

Model **önerir**, insan **karar verir** ([0007](0007-human-in-the-loop-publishing.md)). Model çıktısı hiçbir kanala yayımlanmaz, hiçbir kayıt otomatik oluşturmaz.

Adaylar, **mevcut** inceleme hattına girer: Cloudflare D1'deki `gt-ops.reviews` tablosu, Telegram inceleme botu ve `collect.yml`'ın açtığı `inceleme-kuyrugu` konusu. `osint-ai` **ikinci bir kuyruk, ikinci bir bot veya ikinci bir veritabanı kurmaz.** Bir görüntü adayı, inceleyici için bir metin adayından farksız bir satırdır.

Bir aday satırı; karo (tile) kimliğini, STAC sahne kimliğini ve tarihini, değişim skorunu, modelin etiketini ve tek cümlelik gerekçesini, güvenini ve **kaynaktaki orijinal sahneye bir bağlantı** taşır. **Görüntü eklenmez**; inceleyici orijinali Copernicus veya USGS'ten kendisi açar.

İnceleyici emeği hattın en kıt kaynağıdır. Bir koşuda insana ulaşan aday sayısı **en fazla 20** ile sınırlıdır ve bu sınır yapılandırma dosyasında değil, kodda durur.

### 3. Görüntü kırmızı çizgisi

[Kırmızı çizgiler](../tr/02-red-lines.md) §1, [0013](0013-map-layers-turkiye-perspective.md) ve [0015](0015-announced-operation-areas.md) aynen geçerlidir. Görüntü tarafındaki karşılığı şudur:

1. Türkiye'nin **karası, iç suları ve karasuları + 15 deniz mili** emniyet payı içine giren hiçbir ilgi alanı taranmaz: katalog sorgulanmaz, karo kesilmez, gömme üretilmez, skor hesaplanmaz.
2. Bu bir **süzgeç değil, kapıdır**: alan kırpılmaz, uyarı verilmez; istek reddedilir ve çıkış kodu `2` olur — "sonuç bulunamadı" ile karıştırılamayacak biçimde ayrı.
3. 15 deniz mili = 12 deniz mili karasuyu + bir karonun kendi 2,56 km'lik genişliğini fazlasıyla karşılayan ~3 deniz millik pay. Çit, `platform/collectors/src/gt_collectors/geo.py` referans uygulamasından ve aynı `gt-geofence/1` dosyasından üretilir; `osint-ai` bu kodu değiştirmeden kopyalar ve düzeltmeler önce `platform`'da yapılır.
4. **Bu kuralın bedeli kayda geçirilir:** 15 deniz milinde kapı, görev kapsamında olan İdlib, Lazkiye ve Türkiye kıyısına yakın Yunan adalarını da reddeder. Bu, "vaka vaka tartışılamayan bir kural"ın bilinçli bedelidir. Böyle bir yeri kapsaması gereken bir alan, bir bayrak veya ayarla değil, **yeni bir ADR ile** açılır.
5. Kural **yapısaldır**: modelin bir görüntüde Türk kuvveti olup olmadığına karar vermesi istenmez. Türkiye görüntüsü hiç elde tutulmadığı için o analiz kazara da üretilemez.
6. Bu kuralı sınayan testler zorunludur; atlanamaz, `xfail` işaretlenemez, "geçici olarak" gevşetilemez. CI ayrıca Ankara üzerindeki bir alanın gerçekten `2` ile reddedildiğini doğrular.

### 4. Lisans ve saklama

1. Yalnızca **açık lisanslı ve türetilmiş öznitelik olarak yeniden dağıtılabilir** görüntü kullanılır: Copernicus Sentinel-1/2, USGS/NASA Landsat, Copernicus DEM. NASA FIRMS, OpenStreetMap ve Natural Earth künye ile kullanılabilir.
2. Her kaynağın lisansı, **kullanılmadan önce** belgeye ve koddaki koleksiyon tablosuna yazılır. Lisansı kayıtlı olmayan koleksiyon testleri düşürür.
3. **Ticari görüntü (Maxar, Planet, Airbus) ve web harita altlıkları (Google, Bing, Yandex) kapsam dışıdır** — bütçe *ve* lisans gerekçesiyle, ikisi birbirinden bağımsız. Bu, "bütçe olunca" değişecek bir madde değildir.
4. **Görüntü yeniden dağıtılmaz.** Depoya ve yayına yalnızca **türetilmiş öznitelikler** girer: karo kimliği, kaynak karması, gömme vektörü, değişim skoru, kısa metin ve kaynağa bağlantı. Küçük resim, önizleme, kırpılmış görsel dahil hiçbir piksel yayımlanmaz.
5. OpenStreetMap **ODbL**'dir: çalışma anında bakılabilir, ancak CC BY 4.0 bir veri setine katılamaz. Gerekirse OSM türevi katman ayrı ve ODbL olarak yayımlanır.
6. Gömme vektörleri D1'e yazılmaz; D1 ücretsiz planı (veritabanı başına 500 MB) inceleme kuyruğunun operasyonel deposudur. Vektörler için açık bir Hugging Face veri seti deposu önerilir. **R2 kullanılmaz**, çünkü hesapta ödeme yöntemi ister ([0008](0008-zero-budget-infrastructure.md)).

### 5. Sıfır bütçe ve dürüstlük kuralı

1. Yalnızca **açık ağırlıklı** modeller, yalnızca **ücretsiz** GPU'larda (Kaggle haftalık kotası; Colab yalnızca deney için — zamanlanmış bir iş için güvenilir değildir). Hiçbir hesaba ödeme yöntemi tanımlanmaz.
2. Kullanılan modelin lisansı, boyutu ve VRAM ihtiyacı yazılır. Meta Llama 3.2 görüntü modelleri, çok kipli haklarının AB'de yerleşik kişi ve şirketlere tanınmaması ve kabul edilebilir kullanım politikasının "askerî, savaş, casusluk" kullanımını yasaklaması nedeniyle **kullanılmaz**.
3. **Para veya elimizde olmayan bir GPU gerektiren her öneri, bunu önerildiği cümlede söyler.** Belgelerde abartma bir üslup sorunu değil, bir kusurdur.
4. Şunlar **mümkün değildir** ve ertelenmiş değil, imkânsız olarak kaydedilir:
   - sıfırdan temel model eğitmek (yüzlerce–binlerce GPU-günü; ücretsiz kotayla yüzyıllar),
   - 32B ve üzeri bir görsel-dil modelini çalıştırmak (4 bitte ~20 GB VRAM; ücretsiz kartlar 16 GB),
   - metre altı analiz (araç sayımı, uçak teşhisi) — açık görüntünün çözünürlüğü buna yetmez,
   - gerçek zamanlılık — tekrar geçiş süresi (Sentinel-2'de 5 gün) her bulgunun tazeliğini sınırlar.

### 6. Değerlendirme kapısı

Görüntü hattı, yalnızca **kamuya açık ve önceden raporlanmış** olaylardan kurulmuş küçük bir etiketli ölçüt kümesiyle ölçülür. Bir model, `platform`'daki mevcut anahtar kelime süzgecini **inceleyici başına kabul edilen aday oranında** geçemiyorsa yayına girmez; ölçüm, adayların aynı kuyruğa girdiği ve inceleyicilerin kaynağı görmediği 30 günlük bir gölge koşuyla yapılır.

## Sonuçlar

- Görüntü işleme, kendi bağımlılıkları ve kendi riskiyle, `platform`'u ağırlaştırmadan kendi deposunda gelişir.
- İnsan onayı tek kapıdır ve **tek kuyruktur**; ikinci bir inceleme yüzeyi oluşmaz.
- Kırmızı çizgi, bir politika ayarı değil, bir kod kapısıdır: Türkiye görüntüsü hiç elde tutulmaz.
- 15 deniz millik pay, görev kapsamındaki bazı bölgeleri (İdlib, Lazkiye, kıyıya yakın adalar) da dışarıda bırakır. Bu kabul edilmiş bir kayıptır.
- Lisans kısıtı, en yüksek çözünürlüklü görüntüyü kalıcı olarak kapsam dışı bırakır; bu, hattın ne söyleyebileceğinin üst sınırını belirler (10 m'de araç görülmez).
- Belgelerin abartmama yükümlülüğü, bakım yükü getirir: bir aşama gerçekten çalışmaya başlayana kadar cümleler koşullu kipte kalır.
- Yapılacak işler: `platform`'un `gt-ops.reviews` şemasına görüntü adayı alanlarının nasıl oturacağının netleştirilmesi; ölçüt kümesinin kurulması; `osint-ai` README'sinin bu ADR'ye bağlanması (yapıldı).

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Görüntü işlemeyi `platform`'a eklemek | Model ağırlıkları, GPU oturumu ve gigabaytlık okuma, metin toplayıcıların hafif ve bağımlılıksız yapısını bozardı ([0001](0001-repository-boundaries.md), [0011](0011-threat-model.md)). |
| Ayrı bir inceleme kuyruğu ve ayrı bir bot | İnceleyici emeğini böler, iki farklı onay geçmişi üretir ve [0007](0007-human-in-the-loop-publishing.md)'nin tek kapı ilkesini zayıflatır. |
| Türkiye için nokta bazlı süzgeç (toplayıcılarla aynı 12 dnm) | Bir sahne alandır; nokta testi bir karonun sınırı aşmasını yakalamaz. Ayrıca kırpma, "ne kadarı kırpıldı" tartışmasını her vakada yeniden açar. |
| Emniyet payını 25 dnm yapmak | Kuzey Suriye'nin büyük bölümünü ve Halep'i de dışarıda bırakırdı; görevin kalanını anlamsızlaştıracak kadar geniş. |
| Ticari görüntüyü "bütçe bulunursa" diye açık bırakmak | Asıl engel bütçe değil lisanstır: türetilmiş ürünün yeniden dağıtımı yasaktır. Kapıyı aralık bırakmak yanlış bir beklenti üretir. |
| Web harita altlıklarını (Google/Bing/Yandex) kullanmak | Kullanım koşulları toplu erişimi ve türetilmiş analizi yasaklar; hem depoyu hem çıktımızı yeniden yayımlayan herkesi riske sokar. |
| Modeli her karoda çalıştırmak | Yılda ~900.000 karo; ücretsiz kotayı, değişim tespitinin bedava yaptığı bir işi tekrarlamak için tüketirdi. |
| Kararı ertelemek, önce kod yazmak | Kurallar ilk ihlalden sonra yazılırsa geç kalmış olur; kırmızı çizgi kapısı ilk satırdan önce tanımlanmalıdır. |
