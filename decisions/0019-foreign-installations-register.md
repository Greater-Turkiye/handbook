# 0019 · Yabancı askerî tesis sicili: antlaşma çerçevesi, kanıt standardı ve dışlamalar

> **EN:** Opens a register of foreign military installations, starting with the Aegean islands that the 1923 Treaty of Lausanne (Art. 13) and the 1947 Treaty of Paris (Art. 14) place under a demilitarised regime. Every entry is anchored to a treaty article and to sources, and answers one question: what is there, since when, and which obligation does it bear on. It is a compliance register, not a target list — so it carries no real-time movements, no personnel, no vulnerability or aimpoint analysis, no field collection, and no commercial imagery we may not redistribute. Coordinates are deliberately left empty until each one is verified against a primary source, and the register ships with no map geometry until then. The asymmetry is deliberate and permanent: we document other states' treaty obligations, never the positions of Turkish forces (0013 §red lines stand).

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-19
- **Önerenler:** @nukIeer
- **İlgili:** [0006](0006-verification-scale.md), [0007](0007-human-in-the-loop-publishing.md), [0009](0009-licensing.md), [0010](0010-content-safety-gates.md), [0011](0011-threat-model.md), [0013](0013-map-layers-turkiye-perspective.md), [0014](0014-occupied-territory-and-human-rights-markers.md)

## Bağlam

Projenin bugüne kadarki verisi olaylar ve anlaşmalardır: olan biteni kaydeder, duran şeyi kaydetmez. Oysa Türkiye'nin güvenlik ortamını belirleyen şeylerin bir kısmı olay değil, **durum**dur: Ege adalarındaki kalıcı askerî varlık bunun en belirgin örneğidir.

Bu konunun ayırt edici yanı, tartışmanın öncelikle **hukuki** olmasıdır. Doğu Ege adaları ve Oniki Ada, antlaşmalarla askerden arındırılmış bir rejime tabidir:

- **Lozan Barış Antlaşması (1923), md. 13** — Midilli, Sakız, Sisam ve Ahikerya için: "No naval base and no fortification will be established in the said islands"; Yunan askerî uçaklarının Anadolu kıyısı üzerinde uçuş yasağı (karşılıklı); adalardaki Yunan kuvvetlerinin "normal contingent called up for military service" ile sınırlanması.
- **Lozan md. 12** — Limni, Semadirek, Midilli, Sakız, Sisam ve Ahikerya üzerindeki Yunan egemenliği teyit edilir (İmroz, Bozcaada ve Tavşan Adaları hariç).
- **Paris Barış Antlaşması (1947), md. 14(2)** — İtalya'nın Yunanistan'a bıraktığı Oniki Ada için: "These islands shall be and shall remain demilitarised."

Türkiye'nin resmî tutumu, bu statünün objektif hukuki niteliği bakımından tartışmaya açık olmadığı ve 1960'lardan bu yana ihlal edildiği yönündedir (Dışişleri Bakanlığı Sözcüsü açıklaması SC-4, 5 Mart 2026).

Böyle bir sicilin iki yoldan biriyle yürütülmesi mümkündür ve ikisi arasındaki fark hem etik hem de varoluşsaldır:

1. **Uyum sicili:** neyin, ne zamandan beri, hangi yükümlülüğe karşı orada olduğunu kanıtıyla kaydetmek. Yaptığı iş, IAEA'nın nükleer tesis doğrulamasına benzer: belge üretir, iddiayı değil.
2. **Hedef dosyası:** aynı bilgiyi operasyonel kullanım için toplamak — güncel konum, zafiyet, isabet noktası. Bunu yapan sivil yapı silahlı çatışma hukuku bakımından kendini korumasız bırakır, katkıcısını hukuki ve fiziki riske atar ve ilk hatada bütün sicilini kaybeder.

Bu ADR, birinciyi kurar ve ikinciyi kalıcı olarak yasaklar.

## Karar

### 1. Kapsam

Sicil, **Türkiye dışındaki devletlerin kalıcı askerî tesislerini** kaydeder; ilk aşaması Lozan md. 13 ve Paris md. 14 kapsamındaki adalardır. Kayıtlar `datasets` deposunda `site/1` şemasıyla tutulur.

Her kayıt şu soruları yanıtlar: **ne var, ne zamandan beri var, hangi antlaşma maddesini ilgilendiriyor, kanıtı ne.**

### 2. Kanıt standardı

- Her kayıtta en az bir kaynak zorunludur ([0002](0002-git-as-source-of-truth.md), şema gereği); **antlaşma yükümlülüğü daima antlaşma metninden** alıntılanır, ikincil yorumdan değil.
- Kullanılabilir kanıt: resmî belgeler (Yunan Resmî Gazetesi ΦΕΚ, bakanlık ve genelkurmay duyuruları, parlamento soru-cevapları, ihale ve altyapı belgeleri), NATO/ABD resmî belgeleri, **Copernicus Sentinel** gibi açık lisanslı uydu verisi, OpenStreetMap (ODbL, künyeyle), ve bunları aktaran haber kaynakları kendi güvenilirlik notlarıyla.
- Bir tesisin varlığı ikincil kaynaklara dayanıyorsa kayıt `unverified` kalır ve eksik olan şey kaydın içinde açıkça yazılır. "Doğrulandı" demek için [0006](0006-verification-scale.md)'nın eşiği geçerlidir: en az iki bağımsız kaynak ve güçlü yöntem.
- **Tarih, koordinattan önemlidir.** Sicilin gücü "şu noktada şu var" değil, "1947'de olmaması gereken yerde 19XX'ten beri var" diyebilmektir; bu yüzden ilk görülme ve değişim tarihleri zorunlu alan gibi ele alınır.

### 3. Koordinatlar ve harita

- **Koordinat, kaynağıyla doğrulanmadan yazılmaz.** Doğrulanmamış koordinat, kaydın geri kalanı doğru olsa bile sicili çürütülebilir kılar.
- Bu nedenle sicil **ilk sürümünde koordinatsızdır**: `location.precision` ada/idari birim düzeyinde kalır, `geometry` yoktur, dolayısıyla panelde hiçbir işaret çizilmez. Kayıtların geri kalanı (ad, tür, antlaşma maddesi, tarih, kanıt) doldurulur.
- Koordinat ve geometri, ayrı bir gözden geçirmeden sonra, **tesis ayak izi düzeyinde değil**, yayımlanma biçimi o gözden geçirmede kararlaştırılarak eklenir. Haritada gösterim, o karar verilene kadar kapalıdır.

### 4. Dışlamalar — kalıcı

Sicil hiçbir koşulda şunları içermez:

1. **Gerçek zamanlı hareket.** Birlik, gemi, uçak veya konvoy takibi yoktur. Faaliyet yalnızca **toplulaştırılmış ve gecikmeli** olarak ölçülür (ilan edilmiş tatbikat günleri, NAVTEX/NOTAM kapalı saha günleri, dönemsel sayımlar).
2. **Kişi verisi.** Personel adı, rütbe listesi, görev çizelgesi, iletişim bilgisi yoktur ([0010](0010-content-safety-gates.md)).
3. **Zafiyet ve isabet analizi.** Tesisin savunma açıkları, yaklaşma güzergâhı, mühimmat etkisi, öncelik sıralaması gibi hiçbir operasyonel değerlendirme üretilmez.
4. **Saha toplama.** Hiç kimseden tesis yakınında fotoğraf, ölçüm veya gözlem istenmez; böyle bir katkı geldiğinde kabul edilmez. Katkıcı güvenliği ve hukuki risk buna izin vermez ([0011](0011-threat-model.md)).
5. **Yeniden dağıtımı yasak ticari görüntü** ve lisansı elvermeyen üçüncü taraf veri ([0009](0009-licensing.md)).
6. **Türk kuvvetlerine ait hiçbir şey.** Sicil asimetriktir ve öyle kalacaktır: başkalarının antlaşma yükümlülüklerini belgeler, kendi kuvvetlerimizin konumunu, hareketini veya tertibatını asla yayımlamaz ([0013](0013-map-layers-turkiye-perspective.md)).

### 5. Dil ve iddia sınırı

Sicil **yetenek ve duruş** belgeler; **niyet** iddiası kurmaz. "Şu hazırlık şuna yöneliktir" türü sonuçlar kaydın kendisinde yer almaz; böyle bir değerlendirme yapılacaksa kaynağa atfedilir (doktrin belgesi, resmî açıklama, tedarik örüntüsü) ve ayrı bir analiz metni olarak yayımlanır. Gerekçe pratiktir: sicilin ikna etmesi gereken kitle — gazeteci, hukukçu, bölge uzmanı — abartılmış tek bir cümle yüzünden tabloyu bir bütün olarak reddeder. Tablo kendi sonucunu kendisi söyler.

## Sonuçlar

- Proje ilk kez **kendi ürettiği, başka yerde bu biçimde bulunmayan** bir veri kümesine sahip olur: antlaşma maddesine bağlanmış, tarihlendirilmiş, kaynaklı bir tesis sicili.
- Sicil, hedefleme verisi üretmediği için topluluğu ve katkıcıları hukuki/fiziki riske sokmaz; aynı nedenle kurumsal muhataplar (üniversite, basın, hukukçu) tarafından kullanılabilir olur.
- İlk sürümde harita gösterimi yoktur; bu bilinçli bir eksikliktir ve koordinat doğrulaması ayrı bir iş kalemidir.
- Sicilin bakımı süreklilik ister: tesis eklendiğinde değil, **değiştiğinde** değer üretir. Değişim tespiti (Sentinel karşılaştırması, ΦΕΚ taraması) düzenli bir iş hâline gelmelidir.
- Yanlış tek bir kayıt, doğru yüz kaydı geçersiz kılar. Bu yüzden `unverified` etiketi bir zayıflık değil, sicilin dürüstlüğünün kanıtıdır ve kayıtlarda açıkça taşınır.
