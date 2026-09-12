# 08 · Yazım Kılavuzu

Kayıtlarımız ve paylaşımlarımız **tarafsız, atıflı ve kısa** olmalıdır. Okuyucu bir kaydı okuduğunda ne olduğunu, kimin söylediğini ve ne kadar emin olduğumuzu hemen anlamalıdır.

> Bu sayfadaki örnekler **kurgusaldır**; gerçek olayları temsil etmez.

## Temel ilkeler

1. **Tarafsız**: Sıfat ve duygu yok. "Skandal", "küstah", "tarihî", "şok", "büyük tehdit" yazılmaz.
2. **Atıflı**: Doğrulanmamış veya tartışmalı her şey kaynağına bağlanır: "…'e göre", "…'nın açıklamasına göre", "…'nın iddiasına göre".
3. **Kısa**: Başlık tek cümle; özet 1–3 cümle. Arka plan gerekiyorsa ayrı bir alanda.
4. **Kesinlik derecesi doğru**: Doğrulanmışsa düz anlatım; doğrulanmamışsa atıf; analiz ise tahmin dili ([05](05-verification.md)).
5. **Sansasyon yok**: BÜYÜK HARF, ünlem, "SON DAKİKA", siren emojisi kullanılmaz.

## Projenin kendi sesiyle kullanmadığı ifadeler

Aşağıdaki nitelendirmeler yalnızca `claims[]` içinde, sahibine atfedilerek geçer:

ihlal · provokasyon · saldırganlık · işgal · kışkırtma · terör saldırısı · katliam · soykırım · savaş suçu · meşru müdafaa · misilleme · "sözde" · "hasım/düşman" (bir tarafın ağzından değilse)

Doğru: "Yunanistan Genelkurmayı, Türk uçaklarının hava sahasını ihlal ettiğini açıkladı." (Bu örnek Türk kuvvetlerini içerdiği için ayrıca [Türk kuvvetleri kapısından](02-red-lines.md) geçmek zorundadır.)
Yanlış: "Hava sahası ihlali yaşandı."

## Başlık kalıpları

Başlıklar **geçmiş zaman** ve etken çatıyla, **özne–yüklem–nesne–yer** sırasıyla yazılır. İngilizce başlıklar da geçmiş zamandadır.

| Tür | TR | EN |
|---|---|---|
| Doğrulanmış olay | Yunanistan, Girit açıklarında deniz tatbikatı başlattı | Greece began a naval exercise off Crete |
| Resmî açıklama | Rusya Savunma Bakanlığı: Karadeniz'de insansız deniz aracı imha edildi | Russian MoD said an uncrewed surface vessel was destroyed in the Black Sea |
| Doğrulanmamış iddia | Yerel kaynaklara göre Musul yakınlarında patlama | Explosion near Mosul, according to local sources |
| Yanlış çıkan iddia | İddia: Görüntü Halep'te yeni bir saldırıyı gösteriyor (yanlış — görüntü eski) | Claim: Footage shows new strike in Aleppo (false — footage is old) |
| Tedarik | Mısır, ek savaş uçağı alımı için sözleşme imzaladı | Egypt signed a contract for additional fighter aircraft |
| İhtilaflı | İsrail ve Hizbullah, güney Lübnan'daki çatışmaya dair çelişkili açıklamalar yaptı | Israel and Hezbollah gave conflicting accounts of clash in southern Lebanon |

## Özet kalıbı

Özet şu soruları sırayla cevaplar:
1. **Ne oldu?** (olgu)
2. **Kim?** (aktörler, resmî sıfatlarıyla)
3. **Nerede, ne zaman?** (UTC, hassasiyetiyle uyumlu)
4. **Kime göre?** (kaynak)
5. **Ne kadar eminiz?** (doğrulama durumu ne değilse onu belirtin)

Örnek (TR):
> Yunanistan Deniz Kuvvetleri, 11 Eylül 2026'da Girit'in güneyinde üç gün sürecek bir deniz tatbikatı başlattı. Tatbikat bölgesi, Yunanistan'ın yayımladığı NAVTEX ile duyuruldu. Katılan birlik sayısı açıklanmadı.

Example (EN):
> The Hellenic Navy began a three-day naval exercise south of Crete on 11 September 2026. The exercise area was announced in a NAVTEX issued by Greece. The number of participating units was not disclosed.

## Sayılar, birimler, tarih

| Konu | TR | EN |
|---|---|---|
| Binlik ayırıcı / ondalık | 1.250 · 3,5 | 1,250 · 3.5 |
| Tarih (metinde) | 12 Eylül 2026 | 12 September 2026 |
| Saat (metinde) | 14.30 UTC | 14:30 UTC |
| Veri alanlarında | ISO 8601 (`2026-09-12T14:30:00Z`), ondalık nokta | aynı |

- **Metrik sistem** kullanılır. Denizcilik ve havacılıkta kaynakta kullanılan birim korunur: deniz mili (nmi), knot, uçuş seviyesi (FL). Gerekirse metrik karşılığı parantez içinde verilir: "12 deniz mili (yaklaşık 22 km)".
- Para: kaynaktaki para birimi ve ISO kodu ("2,1 milyar USD"). Kaynak vermedikçe çeviri yapılmaz.
- Kayıp ve sayı iddiaları **her zaman** atfedilir ve kaynağın verdiği biçimde yazılır: "en az 12", "yaklaşık 300". Kaynaklar farklı sayılar veriyorsa hepsi atfedilerek yazılır.
- Kısaltmaları ilk kullanımda açın: "Münhasır Ekonomik Bölge (MEB)". Yaygın kısaltmalar için [Sözlük](09-glossary.md).

## Aktör adları

- Resmî adlar kullanılır; ilk geçişte tam, sonra kısa ad.
- Devlet dışı silahlı gruplar için Türkiye'nin resmî nitelendirmesi, kimin listelediği belirtilerek verilir ([02 §7](02-red-lines.md)).
- Kişiler yalnızca resmî sıfatıyla anılır: "İran Dışişleri Bakanlığı Sözcüsü", ad gerekiyorsa sıfatla birlikte.

## Makine çevirisi

- Makine çevirisiyle üretilmiş metinler `i18n.machine: true` ile işaretlenir (alan, çevrilmiş dili belirtir; kesin yapı `datasets` şemasındadır).
- İşaret, iki dili de bilen bir insan metni gözden geçirip düzelttikten sonra kaldırılır.
- Makine çevirisi özellikle **yer adlarında, rütbelerde, silah sistemi adlarında ve olumsuzluk eklerinde** hata yapar; bunları özellikle kontrol edin.
- Kaynağın özgün dilindeki kısa alıntılar çevrilirken özgün metin de korunur.

## Paylaşımlar (Telegram, Bluesky, X)

- Her paylaşım bir kayda bağlantı verir; kayıt yoksa paylaşım yoktur (bültenler hariç, bkz. [ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)).
- Paylaşımın başında durum etiketi: `[DOĞRULANDI]`, `[DOĞRULANMADI]`, `[İHTİLAFLI]`, `[YANLIŞ]` / `[VERIFIED]`, `[UNVERIFIED]`, `[DISPUTED]`, `[FALSE]`.
- Kısa: başlık + tek cümle bağlam + bağlantı.
- Görsel eklenmez (telif ve kırmızı çizgiler); gerekirse projenin kendi ürettiği harita veya grafik.
- Etiketlemeler (mention) ve kışkırtıcı hashtag'ler kullanılmaz.

## Düzeltmeler nasıl yazılır?

Her düzeltme kaydın `corrections[]` alanına eklenir ve şunları içerir: **tarih (UTC)**, **ne değişti**, **neden**.

Örnek:
```yaml
corrections:
  - date: 2026-09-13T08:00:00Z
    text:
      tr: "Konum hassasiyeti locality'den admin2'ye düşürüldü; ilk geolokasyondaki eşleşme hatalıydı."
      en: "Location precision lowered from locality to admin2; the initial geolocation match was incorrect."
```

Kurallar:
- Düzeltme **açık yüreklilikle** yazılır: hatayı küçültmeden, gereksiz özür metni olmadan.
- Durum değişikliği (ör. `unverified` → `false`) mutlaka bir düzeltme girdisiyle birlikte yapılır.
- Yazım hatası gibi anlamı değiştirmeyen düzeltmeler için girdi gerekmez; git geçmişi yeterlidir.
- Önemli düzeltmeler ilk paylaşımın yapıldığı kanallarda da duyurulur: "DÜZELTME: …" / "CORRECTION: …".
