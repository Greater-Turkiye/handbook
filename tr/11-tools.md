# 11 · Araçlar

Bu sayfa, topluluk çalışmasında kullanılabilecek **ücretsiz ve yasal** açık kaynak araçlarını listeler: ne işe yaradıklarını, kullanım koşullarını ve OPSEC notlarını.

> ⛔ **Kırmızı çizgi hatırlatması — okumadan geçmeyin**
>
> - Bu araçlar **Türk kuvvetlerini izlemek için ASLA kullanılmaz.** Türk askerî uçaklarının ADS-B'si, Türk savaş ve sahil güvenlik gemilerinin AIS'i aranmaz, kaydedilmez, paylaşılmaz; Türk birliklerinin, tesislerinin veya tatbikatlarının uydu görüntüsü ya da geolokasyonu yapılmaz ([02 §1](02-red-lines.md)).
> - Bu araçlar **özel kişileri** izlemek, bulmak veya kimliklendirmek için kullanılmaz: yüz araması yok, özel uçak/tekne sahiplerinin takibi yok, kişilerin ev ve iş yerlerinin geolokasyonu yok ([02 §4](02-red-lines.md)).
> - Araçlar yalnızca **pasif** kullanılır: hiçbir sisteme yetkisiz erişim, tarama veya koşulları aşan otomatik veri çekme yapılmaz ([02 §3](02-red-lines.md)).
> - Bir aracı kullanabiliyor olmanız, sonucu yayımlayabileceğiniz anlamına gelmez. Yayın kararı her zaman [Kırmızı Çizgiler](02-red-lines.md) ve [Doğrulama](05-verification.md) kurallarına göre verilir.

## Listeye alınma ölçütleri

- **Ücretsiz**: Ödeme yöntemi tanımlamadan kullanılabilir. Kredi kartı isteyen "ücretsiz deneme"ler listeye alınmaz ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)).
- **Yasal ve pasif**: Yalnızca kamuya açık bilgiyi gösterir; kullanımı hizmetin kendi koşullarına uygundur.
- **Koşulları okunmuş**: Her aracın kullanım koşulları veya lisans sayfası, listeye eklenirken okunmuş ve aşağıya bağlantısı konmuştur.

> **Son kontrol: 2026-09-13.** Hizmetler koşullarını, fiyatlarını ve adreslerini değiştirir. Bir aracı kullanmadan önce koşullarına kendiniz bakın; değişiklik fark ederseniz bu sayfayı bir PR ile güncelleyin.

### Genel OPSEC notları

- Araçları topluluk işleri için ayırdığınız **ayrı tarayıcı profilinde** kullanın ([04 §4](04-opsec.md)). Kişisel Google, Microsoft veya Yandex hesabınızla oturum açıkken arama yapmayın: aramalarınız o hesaba bağlanır.
- Bir hizmete yüklediğiniz her görsel, girdiğiniz her koordinat ve arama sözcüğü **hizmet sağlayıcının kayıtlarına** girer. Hassas olabilecek hiçbir şeyi yüklemeyin.
- Hesap gerektiren araçlarda takma ad hesabınıza bağlı e-postayı kullanın; ancak **koşulları gerçek kimlik isteyen** hizmetlerde (ör. OpenSky'da hesap açmak) takma adla kayıt olmayın, o özellikleri kullanmayın.
- Araçlardan alınan ekran görüntüleri, veri dosyaları ve dışa aktarımlar **depoya konmaz** ([06](06-sourcing-archiving.md)). Kayda bağlantı, arşiv bağlantısı ve yöntemin metin açıklaması girer.
- Bir araçtan elde edilen bilgiyi kaynak olarak kullanırken, kaynak sicilindeki `terms` değerini aracın koşullarına göre seçin ([06](06-sourcing-archiving.md)). Aşağıdaki `terms` önerileri başlangıç noktasıdır; emin değilseniz daha kısıtlayıcı değeri seçin.

---

## 1. Uydu görüntüsü

### Copernicus Browser
- **Adres:** https://browser.dataspace.copernicus.eu/
- **Ne işe yarar:** Avrupa Birliği'nin Copernicus programına ait Sentinel uydularının görüntülerini tarayıcıda gösterir, tarihler arasında karşılaştırmaya ve indirmeye izin verir. Sentinel-2 optik görüntü, Sentinel-1 ise buluttan ve geceden etkilenmeyen radar (SAR) görüntüsü sağlar. Bir yapının belli bir tarih aralığında hasar görüp görmediğini veya büyük bir konuşlanma alanının değişimini izlemek için kullanışlıdır.
- **Maliyet ve koşullar:** Ücretsiz; tüm özellikler için ücretsiz bir hesap gerekir. [Copernicus Data Space Ecosystem koşulları](https://dataspace.copernicus.eu/terms-and-conditions) Sentinel verisine "ücretsiz, tam ve açık" erişim tanır; portalın kendi içeriği (Sentinel verisi dışındaki metin, görsel) yeniden dağıtılamaz. [Sentinel veri yasal bildirimi](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice) çoğaltma, dağıtma ve değiştirmeye izin verir; atıf zorunludur: `Copernicus Sentinel data [Yıl]`, değiştirilmiş görüntüde `Contains modified Copernicus Sentinel data [Yıl]`. **`terms` önerisi:** `open`.
- **OPSEC ve sınırlar:** Sentinel-2'nin en iyi çözünürlüğü 10 m'dir: araç, bina veya uçak tipi ayırt edilemez; görüntüden bunu çıkardığınızı iddia etmeyin. SAR görüntüsü fotoğraf gibi okunmaz; yorumunuzu deneyimli birine kontrol ettirin.

### NASA Worldview
- **Adres:** https://worldview.earthdata.nasa.gov/
- **Ne işe yarar:** NASA uydularının (MODIS, VIIRS vb.) günlük, küresel ve düşük çözünürlüklü görüntülerini ve yangın/ısıl anomali katmanlarını gösterir. Büyük yangınları, duman bulutlarını ve geniş alanlı olayların zamanlamasını kaba biçimde doğrulamak için kullanılır.
- **Maliyet ve koşullar:** Ücretsiz; görüntülemek için hesap gerekmez. [NASA Yer bilimleri veri politikası](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies) verinin tam ve açık paylaşımını öngörür, kullanım veya yeniden dağıtımı kısıtlamaz; atıf teşvik edilir. **`terms` önerisi:** `open`.
- **OPSEC ve sınırlar:** Çözünürlük yüzlerce metre düzeyindedir. Bir ısıl anomali tek başına "saldırı oldu" demek değildir; yangın, sanayi tesisi veya tarım yakması olabilir. Kaydı yalnızca bu kanıtla `verified` yapmayın.

## 2. Uçuş takibi

> ⛔ Türk askerî uçakları bu araçlarda **aranmaz, izlenmez, kaydedilmez, ekran görüntüsü alınmaz** ([02 §1](02-red-lines.md)). Özel ve iş jetleri özel kişilere ait olabilir; bunlar takip edilmez ([02 §4](02-red-lines.md)).

### adsb.lol
- **Adres:** https://adsb.lol/
- **Ne işe yarar:** Gönüllü alıcılardan beslenen, askerî uçakları filtrelemeyen bir ADS-B/MLAT harita ve API hizmeti. Yabancı keşif, tanker ve nakliye uçaklarının kamuya açık yayınlarını görmek için kullanılır.
- **Maliyet ve koşullar:** Ücretsiz; hesap gerekmez. adsb.lol'un yayımladığı geçmiş veri setleri [Open Database License (ODbL) 1.0 ve CC0](https://github.com/adsblol/globe_history_2025) ile lisanslıdır. **`terms` önerisi:** `attribution` (ODbL atıf ister; türetilmiş veri tabanları aynı lisansla paylaşılır).
- **OPSEC ve sınırlar:** ADS-B'yi askerî uçaklar çoğu zaman kapatır, sinyal sahtelenebilir; haritada görünmemek "uçmadı" demek değildir. MLAT konumları yaklaşıktır. Kendi alıcınızla ağı beslemek, alıcınızın konumunu hizmetle paylaşmak demektir; topluluk çalışması için gerekli değildir.

### OpenSky Network
- **Adres:** https://opensky-network.org/
- **Ne işe yarar:** İsviçre merkezli, kâr amacı gütmeyen bir araştırma ağı. Canlı harita, geçmiş veri tabanı ve API sunar; akademik çalışmalarda sık atıf yapılan bir kaynaktır.
- **Maliyet ve koşullar:** Haritayı görüntülemek ücretsizdir. [Kullanım koşulları ve veri lisans sözleşmesi](https://opensky-network.org/about/terms-of-use) veri lisansını **yalnızca kâr amacı gütmeyen araştırma ve eğitim** amacıyla verir. Ticari kuruluşlar (hükümet ve askerî yükleniciler dahil) yazılı lisans almak zorundadır. REST API'nin canlı bir üründe veya **otomatik bir sistemde** kullanılması, kâr amacı gütmeyen kuruluşlar için bile önceden yazılı anlaşma gerektirir. Veri setleri üçüncü kişilere dağıtılamaz. Anonimleştirilmemiş veriye dayanan yayınlarda uçak tanımlayıcılarının anonimleştirilmesi istenir. **`terms` önerisi:** `restricted`. Bu nedenle `platform` toplayıcıları OpenSky API'sini yazılı anlaşma olmadan **kullanmaz**.
- **OPSEC:** Koşullar, kayıt olan kişinin kimliğini gizlememesini ve OpenSky'ın kayıtlı talep sahibinin adını açıklayabileceğini söyler. Bu, takma adla katkı modelimizle bağdaşmaz: **Takma adla hesap açmayın**; hesap gerektiren özellikleri topluluk çalışması için kullanmayın.

## 3. Gemi takibi

> ⛔ Türk savaş gemileri ve Sahil Güvenlik gemileri bu araçlarda **aranmaz, izlenmez, kaydedilmez** ([02 §1](02-red-lines.md)). Mürettebat ve gemi sahibi kişiler kimliklendirilmez ([02 §4](02-red-lines.md)).

AIS sitelerinin büyük çoğunluğu verilerinin ve ekran görüntülerinin **yeniden kullanımını kısıtlar**. Bu yüzden AIS siteleri genellikle `restricted` veya `no-redistribution` kaynaktır: **yalnızca ipucu** olarak kullanılır, veri kopyalanmaz ve hiçbir kaydın tek kaynağı olamaz ([02 §9](02-red-lines.md)). AIS kapatılabilir ve sahtelenebilir; savaş gemileri çoğu zaman yayın yapmaz.

### VesselFinder
- **Adres:** https://www.vesselfinder.com/
- **Ne işe yarar:** AIS verisine dayalı canlı gemi haritası. Ticari gemilerin, tankerlerin ve yardımcı gemilerin kamuya açık konum yayınlarını görmek için kullanılır.
- **Maliyet ve koşullar:** Sınırlı özelliklerle ücretsiz web erişimi vardır; ek özellikler ücretlidir. [Kullanım koşulları](https://www.vesselfinder.com/terms) otomatik veri çekmeyi (bot, kazıyıcı) yetkili API dışında yasaklar. Ücretsiz kullanıcılar içerikten yalnızca "iç kullanım için, yeniden dağıtılamayan makul alıntılar" yapabilir. Zaman damgası, tanımlayıcı ve filigranların silinmesini ve içeriğin yapay zekâ modeli eğitiminde kullanılmasını da yasaklar. **`terms` önerisi:** `no-redistribution`.
- **OPSEC:** Ekran görüntüsü paylaşmayın ve depoya koymayın. Bir gözlemi kayda dönüştürmek için bağımsız bir kaynak (resmî açıklama, NAVTEX, uydu görüntüsü) bulun.

## 4. Arşivleme

Arşivleme kuralları [06 · Kaynaklandırma ve Arşivleme](06-sourcing-archiving.md) sayfasındadır; burada yalnızca araçların koşulları ve OPSEC notları var.

> ⛔ Kişisel veri, esir/kayıp görüntüsü veya Türk kuvvetlerine dair resmî olmayan içerik barındıran sayfaları **arşivlemeyin**. Arşivlemek, o içeriğin kalıcı ve herkese açık bir kopyasını oluşturur ([02](02-red-lines.md)).

### Wayback Machine — Save Page Now
- **Adres:** https://web.archive.org/save
- **Ne işe yarar:** Internet Archive'ın Wayback Machine'ine tek bir sayfanın o anki kopyasını kaydeder.
- **Maliyet ve koşullar:** Ücretsiz. [Yardım sayfasına](https://help.archive.org/help/using-the-wayback-machine/) göre Save Page Now bir sayfayı bir kez kaydeder, siteyi taramaya eklemez. Site sahipleri arşivlenmiş kopyaların hariç tutulmasını isteyebilir; yani bir arşiv kopyası ileride erişilemez hâle gelebilir. Genel koşullar: [Internet Archive kullanım koşulları](https://archive.org/about/terms.php). **`terms` önerisi:** arşiv, özgün kaynağın `terms` değerini devralır.
- **OPSEC:** Bu yüzden mümkünse archive.today'e de kaydedin ([06](06-sourcing-archiving.md)). Arşivlenen kopyanın giriş sayfası veya çerez duvarı değil, gerçekten içerik olduğunu kontrol edin.

### archive.today
- **Adres:** https://archive.ph/ (aynı hizmet archive.today, archive.is, archive.md gibi alan adlarıyla da çalışır)
- **Ne işe yarar:** Sosyal medya gibi dinamik sayfaları çoğu zaman Wayback'ten daha iyi kaydeder; sayfanın ekran görüntüsünü de saklar.
- **Maliyet ve koşullar:** Ücretsiz, hesap yok. [SSS sayfası](https://archive.ph/faq) sayfaların "neredeyse sonsuza dek" saklandığını, hizmetin özel olarak finanse edildiğini, video ve sesin kaydedilmediğini belirtir. Barındırma kurallarını ihlal eden sayfalar silinebilir. **`terms` önerisi:** arşiv, özgün kaynağın `terms` değerini devralır.
- **OPSEC — önemli:** SSS'ye göre bir sayfayı arşivlediğinizde **IP adresiniz, arşivlenen siteye `X-Forwarded-For` başlığıyla iletilir.** Arşivlediğiniz site (ör. taraflardan birinin sitesi) IP adresinizi görebilir. Hassas bir sayfayı arşivlerken bunu hesaba katın; gerekirse Wayback'i tercih edin. Hizmetin işletmecisi anonimdir ve kalıcılığı garanti edilmez; tek arşiv olarak kullanmayın.

## 5. Geolokasyon ve kronolokasyon

Yöntem için [07 · Konum, Zaman ve İhtilaflı Bölgeler](07-geo-time-disputed.md).

> ⛔ Türkiye'deki askerî tesisler ve Türk birlikleri geolokasyon konusu **olmaz**. Özel kişilerin evleri ve iş yerleri geolokasyonu yapılmaz ([02](02-red-lines.md)).

### Google Earth (web)
- **Adres:** https://earth.google.com/web/
- **Ne işe yarar:** Yüksek çözünürlüklü uydu ve hava görüntüsü, 3B arazi ve binalar, mesafe/alan ölçümü. Görüntüdeki yol düzeni, bina ve arazi silüetiyle eşleştirme için temel araçtır.
- **Maliyet ve koşullar:** Ücretsiz. [Google Earth ek hizmet şartları](https://www.google.com/help/terms_maps-earth/) içeriğin kopyalanmasını ve yeniden dağıtılmasını (izin sayfası ve adil kullanım dışında), toplu indirmeyi ve koordinat dahil içerikten veri seti oluşturmayı yasaklar. İçeriğin **uygun atıfla** çevrimiçi, videoda ve basılı olarak gösterilmesine izin verir. **`terms` önerisi:** `attribution`.
- **OPSEC ve sınırlar:** Kişisel Google hesabınızla oturum açıkken kullanmayın. Görüntüler farklı tarihlerden mozaiktir; eşleştirmede kullandığınız görüntünün tarihini yöntem açıklamasına yazın. Ekran görüntüsü depoya konmaz.

### OpenStreetMap
- **Adres:** https://www.openstreetmap.org/
- **Ne işe yarar:** Topluluk tarafından üretilen açık harita. Yol, bina, cami, su kulesi, elektrik hattı gibi nesnelerin adları ve etiketleri geolokasyonda aday bölgeyi daraltmaya yarar; yer adlarının yerel yazımını bulmak için de kullanılır.
- **Maliyet ve koşullar:** Ücretsiz. [Telif ve lisans sayfasına](https://www.openstreetmap.org/copyright) göre veri Open Database License (ODbL) ile lisanslıdır: "© OpenStreetMap katkıcıları" atfıyla kopyalanabilir, dağıtılabilir, uyarlanabilir. Veriyi değiştirerek dağıtırsanız aynı lisansla dağıtmanız gerekir. **`terms` önerisi:** `open` (atıfla).
- **OPSEC:** OSM düzenlemeleri kullanıcı adı ve zaman damgasıyla **herkese açık** kaydedilir. Topluluk çalışması sırasında OSM'ye askerî tesis eklemeyin veya düzenleme yapmayın; yalnızca okuyun.

### Overpass Turbo
- **Adres:** https://overpass-turbo.eu/
- **Ne işe yarar:** OpenStreetMap verisini sorgulayan web arayüzü. Örneğin "bu ilçede birbirine 200 m'den yakın bir cami ve bir su kulesi" gibi sorgularla aday konumları listeler.
- **Maliyet ve koşullar:** Ücretsiz, hesap yok. Sorgular kamuya açık Overpass API sunucularına gider. [Overpass API kullanım politikasına](https://wiki.openstreetmap.org/wiki/Overpass_API) göre günde 10.000 sorgu ve 1 GB veri altı kabul edilebilir kullanımdır. Ticari kullanım kendi sunucusunu kurmalıdır; aynı anda birden fazla betik çalıştırılmaz. Sonuçlar OSM verisidir (ODbL). **`terms` önerisi:** `open` (atıfla).
- **OPSEC:** Sunucular yoğundur; gereksiz büyük sorgular çalıştırmayın. Otomatik toplayıcılarda kullanılacaksa önce bakımcılarla konuşun.

### SunCalc
- **Adres:** https://www.suncalc.org/
- **Ne işe yarar:** Seçilen yer ve tarih için güneşin konumunu (yükseklik, azimut), gün doğumu/batımını ve gölge uzunluğunu hesaplar. Güneş yükseklik ve azimutundan saati geriye doğru hesaplayabilir. Gölgelerden kronolokasyon için kullanılır ([07](07-geo-time-disputed.md)).
- **Maliyet ve koşullar:** Ücretsiz, hesap yok; bağışla desteklenen, Almanya'da bir kişi tarafından işletilen bir sitedir. Ayrı bir kullanım koşulları sayfası bulunmuyor. Sitenin alt kısmındaki yasal bildirim ve gizlilik politikasına bakın. Hesap sonuçları olgudur; kayda yöntem olarak yazılır.
- **OPSEC:** SunCalc bağlantıları koordinat ve tarihi adreste taşır. Bir bağlantıyı paylaşmak, incelediğiniz yeri de paylaşmak demektir.

### PeakVisor
- **Adres:** https://peakvisor.com/
- **Ne işe yarar:** 3B dağ panoramaları ve zirve tanımlama. Bir görüntüdeki dağ silüetini (ufuk çizgisini) belirli bir bakış noktasından görünen araziyle eşleştirmek için kullanılır.
- **Maliyet ve koşullar:** Temel özellikler ücretsizdir; PRO aboneliği ücretlidir. Topluluk çalışması için **yalnızca ücretsiz özellikler** kullanılır, ödeme yöntemi tanımlanmaz ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)). [Kullanım koşulları](https://peakvisor.com/en/terms.html) hizmetin kötüye veya aşırı kullanımını ve başkalarının fikrî haklarının ihlalini yasaklar. **`terms` önerisi:** `attribution`.
- **OPSEC:** Hesap gerektiren özellikler için takma ad e-postası kullanın. Konum izni isteyen mobil uygulama yerine web sürümünü tercih edin.

## 6. Meta veri

### ExifTool
- **Adres:** https://exiftool.org/
- **Ne işe yarar:** Görsel, video, PDF ve diğer dosyalardaki meta veriyi (EXIF, XMP, GPS, cihaz modeli, zaman) okur, düzenler ve siler. Bir dosyayı bakımcılara göndermeden önce meta veriyi temizlemek için kullanılır ([04 §5](04-opsec.md)):

  ```bash
  exiftool dosya.jpg          # meta veriyi göster
  exiftool -all= dosya.jpg    # tüm meta veriyi sil (dosya.jpg_original yedeği kalır; onu da silin)
  ```

- **Maliyet ve koşullar:** Ücretsiz, açık kaynak. [Lisans](https://exiftool.org/#license): Perl ile aynı koşullarda dağıtılabilen ve değiştirilebilen özgür yazılım.
- **OPSEC:** Bilgisayarınızda **çevrimdışı** çalışır. Dosyaları çevrimiçi "EXIF görüntüleyici" sitelerine yüklemeyin. İndirdiğiniz paketin sağlama toplamını sitede yayımlanan değerle karşılaştırın. Meta veri kolayca değiştirilebilir; kronolokasyonda tek başına kanıt değildir ([07](07-geo-time-disputed.md)).

## 7. Doğrulama

> ⛔ Tersine görsel arama **yüz araması için kullanılmaz.** Bir kişinin yüzünü aratmak, onu kimliklendirmeye çalışmaktır ve özel kişiler kuralını ihlal eder ([02 §4](02-red-lines.md)). Yüz tanıma hizmetleri (ör. PimEyes) bu nedenle listede yoktur.

### InVID-WeVerify doğrulama eklentisi
- **Adres:** https://weverify.eu/verification-plugin/
- **Ne işe yarar:** Video ve görsel doğrulama için tarayıcı eklentisi: videodan anahtar kare çıkarma, bu karelerle birden çok motorda tersine arama, meta veri okuma, büyüteç ve adli analiz filtreleri. AFP Medialab tarafından geliştirilir ve sürdürülür.
- **Maliyet ve koşullar:** Ücretsiz. Chrome için; Edge ve Opera'ya Chrome mağazasından kurulabilir. Yazılım, [eklenti sayfasında](https://weverify.eu/verification-plugin/) belirtildiği üzere "olduğu gibi", garantisiz sunulur.
- **OPSEC:** Tarayıcı eklentileri geniş izinlere sahiptir: Yalnızca resmî mağazadan ve yalnızca topluluk için ayırdığınız tarayıcı profiline kurun. Tersine arama kısayolları görseli seçtiğiniz arama motoruna gönderir.

### Tersine görsel arama motorları

Eski görüntünün yeni olay gibi sunulmasını yakalamanın ilk adımıdır ([05](05-verification.md)). Motorların dizinleri farklıdır; **birden fazlasını** deneyin.

| Motor | Adres | Koşullar | OPSEC notu |
|---|---|---|---|
| TinEye | https://tineye.com/ | [Ticari olmayan kullanım için ücretsiz](https://help.tineye.com/article/239-is-tineye-free-to-use); ticari kullanım ücretli API ile. [Yüklenen görseller saklanmaz](https://help.tineye.com/article/244-does-tineye-keep-images-i-upload-during-a-search). Genel koşullar: [tineye.com/terms](https://tineye.com/terms) | Hesap gerekmez; yükleme sonrası görselin silindiğini açıkça belirten tek motor. Bir görüntünün **en eski kopyasını** bulmak için tarih sıralaması kullanışlıdır. |
| Google Lens / Google Görseller | https://lens.google.com/ | [Google Hizmet Şartları](https://policies.google.com/terms) | Kişisel Google hesabınızla oturum açıkken kullanmayın; aramalar hesabınıza bağlanır. |
| Bing Görsel Arama | https://www.bing.com/images/feed | [Microsoft Hizmet Sözleşmesi](https://www.microsoft.com/en-us/servicesagreement) | Kişisel Microsoft hesabınızla oturum açmayın. |
| Yandex Görseller | https://yandex.com/images/ | [Yandex Kullanıcı Sözleşmesi](https://yandex.com/legal/rules/en/): YANDEX LLC, Rusya Federasyonu hukukuna tabi | Rusya ve eski Sovyet coğrafyasındaki görüntülerde çoğu zaman güçlüdür. Yüklediğiniz görsel Rus hukukuna tabi bir şirkette işlenir: Hassas olabilecek hiçbir şey yüklemeyin, oturum açmayın. |

## 8. NOTAM ve NAVTEX kaynakları

NOTAM ve NAVTEX, tatbikat ve atış alanlarını duyuran **birincil resmî kaynaklardır** ([06](06-sourcing-archiving.md), seviye 1).

> ⛔ **Türk kuvvetlerine ait tatbikat ve atış duyuruları** (Türk NAVTEX ve NOTAM'ları dahil) resmî açıklama sayılır, ama **Türk kuvvetleri kapısından** geçer: Koordinat yazılmaz, NAVTEX'teki alan koordinatları kayda kopyalanmaz. Konum hassasiyeti yalnızca `admin1`, `country` veya `sea-area` olur. Kayıt en az 24 saat bekletilir ve bakımcı onayı alır ([02 §1](02-red-lines.md)).
>
> Ege ve Doğu Akdeniz'de karşılıklı yayımlanan NAVTEX'ler sıklıkla tartışmalı iddialar içerir (yetki alanı, askerden arındırılmış statü vb.). Bu nitelendirmeler `claims[]` içinde yayımlayana atfedilir ([07](07-geo-time-disputed.md)).

### EUROCONTROL EAD Basic (NOTAM)
- **Adres:** https://www.ead.eurocontrol.int/
- **Ne işe yarar:** Avrupa Havacılık Bilgi Veri Tabanı'nın (EAD) herkese açık sürümü. NOTAM'lardan uçuş öncesi bilgi bülteni (PIB) oluşturma ve AIP yayınlarına göz atma imkânı verir.
- **Maliyet ve koşullar:** [Ücretsiz kayıt formuyla](https://www.ead.eurocontrol.int/cms-eadbasic/opencms/en/ead-solutions/ead-basic/) erişilir. Sayfaya göre EAD Basic, operasyonel veri tabanına bağlı değildir, her zaman en güncel bilgiyi göstermez ve **operasyonel amaçla kullanılmamalıdır**. **`terms` önerisi:** `attribution`.
- **OPSEC ve sınırlar:** Güncel olmayabileceği için bir NOTAM'ı kayda koymadan önce ilgili ülkenin resmî havacılık bilgi yayınıyla veya başka bir kaynakla karşılaştırın. Kayıt formunda yalnızca gerekli bilgileri verin.

### NGA Maritime Safety Information — seyir uyarıları
- **Adres:** https://msi.nga.mil/NavWarnings
- **Ne işe yarar:** ABD Ulusal Coğrafi-Uzamsal İstihbarat Ajansı'nın (NGA) yayımladığı seyir uyarıları. HYDROLANT uyarıları Doğu Akdeniz ve Karadeniz'i de kapsar (ör. mayın, atış, tehlikeli faaliyet uyarıları). Uyarılar tarihleri ve numaralarıyla listelenir.
- **Maliyet ve koşullar:** Ücretsiz, hesap gerekmez. Ayrı bir kullanım koşulları sayfası doğrulayamadık. **`terms` önerisi:** `attribution` ile başlayın.
- **OPSEC ve sınırlar:** Kıyı devletlerinin NAVTEX'lerini derleyen ikincil bir yayındır. Mümkünse duyuruyu yapan kıyı devletinin özgün yayınına da bağlantı verin.

### Kıyı Emniyeti Genel Müdürlüğü — Türk Radyo Yayınları (NAVTEX)
- **Adres:** https://www.kiyiemniyeti.gov.tr/turk_radyo_yayinlari
- **Ne işe yarar:** Türkiye kıyı radyo istasyonlarının (İstanbul, İzmir, Antalya, Samsun) NAVTEX yayınları. Tarih, istasyon ve dile (Türkçe/İngilizce) göre aranabilir. Yayın kodu, ilk ve son yayın zamanı ile mesaj metnini içerir.
- **Maliyet ve koşullar:** Ücretsiz, hesap gerekmez; resmî kamu kaynağı. **`terms` önerisi:** `attribution`.
- **OPSEC:** Türk kuvvetlerine ait tatbikat/atış duyuruları için yukarıdaki kapı kuralları geçerlidir.

### Seyir, Hidrografi ve Oşinografi Dairesi (ŞNHD) — Seyir duyuruları
- **Adres:** https://www.shodb.gov.tr/BasinveYayin/SeyirDuyurulari?lang=tr-TR
- **Ne işe yarar:** Deniz Kuvvetleri Komutanlığına bağlı ŞNHD'nin NAVTEX ve seyir duyuruları. İstasyonlara göre (Samsun, İstanbul, İzmir, Antalya) ve yerel duyurular olarak listelenir; İngilizce seçeneği vardır.
- **Maliyet ve koşullar:** Ücretsiz, hesap gerekmez. Sitenin uyarısına göre internet, Deniz Emniyet Bilgisi veri akışının parçası değildir. En güncel ve bağlayıcı kaynak NAVTEX ve SafetyNET yayınlarıdır. **`terms` önerisi:** `attribution`.
- **OPSEC:** Bu duyuruların önemli bir kısmı Türk kuvvetlerinin faaliyetleriyle ilgilidir: Yukarıdaki kapı kuralları **istisnasız** uygulanır.

### Yunanistan Deniz Kuvvetleri Hidrografi Dairesi (HNHS) — NAVTEX
- **Adres:** https://hnhs.gr/category/minimata-navtex/
- **Ne işe yarar:** Yunanistan'ın Heraklion (Girit), Kerkyra (Korfu) ve Limnos istasyonlarından yayımlanan NAVTEX mesajları; Yunan tatbikat ve atış duyurularının birincil kaynağıdır.
- **Maliyet ve koşullar:** Ücretsiz, hesap gerekmez. Site Yunanca; İngilizce arayüz sınırlıdır. Site, gösterilen haritaların yalnızca görsel yardım olduğunu ve seyir amacıyla kullanılmaması gerektiğini belirtir. **`terms` önerisi:** `attribution`.
- **OPSEC:** Yunanca metni makine çevirisiyle okuyorsanız, kayıtta `i18n.machine` kuralını uygulayın ([08](08-style-guide.md)). Tartışmalı ifadeler atfedilir.

---

## Listede neden yok?

Aşağıdaki araçlar incelendi, ama listeye alınmadı:

| Araç | Neden |
|---|---|
| Sentinel Hub EO Browser | Hizmet kullanımdan kaldırıldı. Sayfası kullanıcıları Planet Insights Platform'a, yalnızca açık veri için Copernicus Browser'a yönlendiriyor. Copernicus Browser yukarıda. |
| MarineTraffic | Kullanım koşulları sayfasını doğrulayamadık (erişim engellendi). Koşulları okunmadan listeye alınmaz. |
| FAA NOTAM Search | Sayfaya erişimimiz engellendi (HTTP 403); çalıştığını ve koşullarını doğrulayamadık. |
| Yüz tanıma / yüz arama hizmetleri | Özel kişileri kimliklendirmeye yarar; kırmızı çizgi ([02 §4](02-red-lines.md)). |
| Ücretli veya kredi kartı isteyen deneme sürümleri | Sıfır bütçe ilkesi ([ADR 0008](../decisions/0008-zero-budget-infrastructure.md)). |

## Yeni araç önermek

1. Aracın ücretsiz (ödeme yöntemi tanımlamadan), yasal ve pasif olduğunu kontrol edin.
2. Kullanım koşullarını veya lisansını **okuyun**; bağlantısını ve özetini yazın.
3. Aracın kırmızı çizgilerle ilişkisini düşünün: Türk kuvvetlerini veya özel kişileri izlemeye yarayan bir özelliği varsa OPSEC notunda açıkça yasaklayın.
4. `tr/11-tools.md` ve `en/11-tools.md` sayfalarını **aynı PR'da** güncelleyin ve "Son kontrol" tarihini değiştirin.
