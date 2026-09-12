# 05 · Doğrulama

Her kayıt, ne kadar güvenilir olduğunu **açıkça** söyler. Okuyucu, bir bilginin "doğrulandı" mı yoksa "bir tarafın iddiası" mı olduğunu tek bakışta anlayabilmelidir. Bu sayfa kullandığımız ölçekleri ve kuralları anlatır. Karar gerekçesi için bkz. [ADR 0006](../decisions/0006-verification-scale.md).

Doğrulama iki ayrı soruya cevap verir:

1. **Kaynak ne kadar güvenilir?** → Kaynak güvenilirliği (A–F), **kaynak sicilinde** (`src_` kaydı) tutulur.
2. **Bu bilgi ne kadar inandırıcı?** → Bilgi inandırıcılığı (1–6), **kaydın kendisinde** (`assessment.credibility`) tutulur.

Bu ikisi birbirinden bağımsızdır: Güvenilir bir kaynak yanlış bir bilgi aktarabilir; güvenilmez bir kaynak doğru bir bilgi verebilir.

## Admiralty (NATO) ölçeği

### Kaynak güvenilirliği (source reliability)

| Kod | Türkçe | English | Ne zaman? |
|---|---|---|---|
| **A** | Tamamen güvenilir | Completely reliable | Özgünlüğü, güvenilirliği ve yetkinliği konusunda hiç şüphe yok. Pratikte **çok nadir** verilir. |
| **B** | Genellikle güvenilir | Usually reliable | Küçük şüpheler var; geçmişte büyük çoğunlukla doğru bilgi vermiş. |
| **C** | Oldukça güvenilir | Fairly reliable | Şüpheler var; geçmişte zaman zaman doğru bilgi vermiş. |
| **D** | Genellikle güvenilir değil | Not usually reliable | Ciddi şüpheler var; geçmişte zaman zaman doğru bilgi vermiş. |
| **E** | Güvenilmez | Unreliable | Özgünlük, güvenilirlik ve yetkinlikten yoksun; geçmişte yanlış bilgi vermiş. |
| **F** | Güvenilirliği değerlendirilemez | Reliability cannot be judged | Değerlendirme için yeterli temel yok. **Yeni kaynaklar için varsayılan.** |

**Notlar:**
- Resmî kaynaklar otomatik olarak A değildir. Bir savunma bakanlığı kendi kayıpları, düşman kayıpları veya tartışmalı olaylar hakkında taraftır. Bir devletin **kendi faaliyetine dair olgusal duyurusu** (ör. "tatbikat başladı") ile **tartışmalı iddiası** (ör. "düşman uçağı düşürüldü") farklıdır; ikincisi her durumda `claims[]` içinde atfedilir.
- Kaynak güvenilirliği bir bakımcı veya inceleyici tarafından, sicil PR'ı ile değiştirilir; gerekçe yazılır.

### Bilgi inandırıcılığı (information credibility)

| Kod | Türkçe | English | Ne zaman? |
|---|---|---|---|
| **1** | Başka kaynaklarca doğrulanmış | Confirmed by other sources | Bağımsız kaynaklar veya görsel/uzaysal kanıtla doğrulanmış; mantıklı ve tutarlı. |
| **2** | Muhtemelen doğru | Probably true | Doğrulanmamış ama mantıklı, tutarlı, bilinen tabloya uygun. |
| **3** | Belki doğru | Possibly true | Doğrulanmamış; makul ama bazı yönleriyle tutarsız veya eksik. |
| **4** | Şüpheli | Doubtful | Doğrulanmamış; mümkün ama mantıklı değil, karşı bilgi var. |
| **5** | Olası değil | Improbable | Mantıksız, başka bilgilerle çelişiyor. |
| **6** | Doğruluğu değerlendirilemez | Truth cannot be judged | Değerlendirme için temel yok. **Yeni kayıtlar için varsayılan.** |

## Durum değerleri (`assessment.status`)

| Değer | Türkçe | Anlamı |
|---|---|---|
| `unverified` | Doğrulanmamış | Kaynaklıdır, arşivlidir, ama doğrulama kurallarını henüz karşılamaz. **Varsayılan.** |
| `partially_verified` | Kısmen doğrulanmış | Olayın bir kısmı (ör. yer ve zaman) doğrulandı, diğer kısmı (ör. fail, sonuç) doğrulanmadı. Hangi kısmın doğrulandığı özette belirtilir. |
| `verified` | Doğrulanmış | Aşağıdaki **tüm** koşulları karşılar. |
| `disputed` | İhtilaflı | Güvenilir kaynaklar birbiriyle çelişiyor; proje taraf tutmaz, iddiaları atfeder. |
| `false` | Yanlış | İddianın yanlış olduğu gösterildi. Kayıt **silinmez**; yanlış olduğu bilgisi kalıcıdır. |

## `verified` kuralları

Bir kayıt ancak şu koşulların **hepsini** sağlıyorsa `verified` olabilir (CI denetler):

1. `assessment.credibility` **1 veya 2**.
2. **İngilizce metin** (başlık ve özet) mevcut.
3. **Her kaynağın** bir arşiv bağlantısı var ([06](06-sourcing-archiving.md)).
4. Şunlardan biri:
   - **En az iki bağımsız kaynak**, veya
   - **Geolokasyon**, **kronolokasyon** veya **uydu görüntüsü** ile doğrulama — yöntem ve kanıt bağlantısı kayıtta belirtilir ([07](07-geo-time-disputed.md)).
5. Kısıtlı (`restricted` / `no-redistribution`) bir kaynak **tek** dayanak olamaz.

`verified`, "olay gerçekleşti" demektir; **tartışmalı nitelendirmelerin doğru olduğu anlamına gelmez**. Örneğin bir uçağın belli bir bölgede uçtuğu doğrulanabilir; bunun "ihlal" olup olmadığı `claims[]` içinde taraflara atfedilir.

## Bağımsız kaynak nedir?

İki kaynak, **bilgiyi birbirinden ayrı yollarla** elde etmişse bağımsızdır.

| Durum | Bağımsız mı? |
|---|---|
| İki haber sitesi aynı ajans haberini (ör. AA, Reuters, AFP) yayımlıyor | **Hayır** — tek kaynak |
| Bir gazete, bir bakanlık açıklamasını aktarıyor | **Hayır** — kaynak bakanlıktır |
| Aynı hükümete bağlı iki devlet medyası | **Hayır** |
| Bir Telegram kanalı, başka bir kanalın paylaşımını yeniden paylaşıyor | **Hayır** |
| Çatışmanın iki karşıt tarafı aynı olguyu doğruluyor | **Evet** — ve güçlü bir doğrulama (çıkarları çatışan tarafların örtüştüğü nokta) |
| Resmî açıklama + kendi muhabiriyle yerinde haber yapan bir yayın organı | **Evet** |
| Resmî açıklama + bağımsız uydu görüntüsü | **Evet** |
| İki farklı kişinin farklı açılardan çektiği ve geolokasyonu yapılmış videolar | **Evet** (ancak videoların kendisi depoya konmaz) |

Şüpheli durumlarda bağımsızlığı **varsaymayın**; kaynakların bilgiyi nereden aldığını takip edin (dairesel raporlama tuzağı).

## Dezenformasyonla başa çıkma

- Yanlış bir iddia yaygın dolaşıma girdiyse, bu **kayda değer bir olaydır**. Kayıt açılır, iddia atfedilir, `status: false` yapılır ve yalanlayan kaynaklar eklenir.
- `false` kayıtlar **silinmez**: Aynı iddia tekrar ortaya çıktığında referans olurlar.
- Başlık, iddiayı gerçekmiş gibi sunmaz: "İddia: …" / "Claim: …" kalıbı kullanılır ([08](08-style-guide.md)).
- Bir iddiayı yalanlarken yanlış bilgiyi tekrar yaymamaya dikkat edin: Önce doğruyu söyleyin, sonra iddiayı, sonra neden yanlış olduğunu.
- Eski görüntülerin yeni olay gibi sunulması, başka ülkeden görüntüler, video oyunu görüntüleri, yapay zekâ ürünü görseller en sık karşılaşılan türlerdir. Ters görsel arama ve kronolokasyon ilk adımdır.
- Koordineli davranış (aynı metnin çok sayıda hesapta aynı anda paylaşılması) fark ederseniz bakımcılara bildirin; bu tür ağlar özel kişilere dair bilgi içerebileceğinden kayda girmeden önce değerlendirilir.

## Tahmin dili

Değerlendirme ve analiz metinlerinde olasılık ifadeleri **tutarlı** kullanılır. ABD İstihbarat Topluluğu Direktifi 203 (ICD 203) ölçeğini temel alıyoruz:

| Türkçe | English | Yaklaşık olasılık |
|---|---|---|
| Neredeyse hiç | Almost no chance | %1–5 |
| Çok düşük ihtimal | Very unlikely | %5–20 |
| Düşük ihtimal | Unlikely | %20–45 |
| Yaklaşık eşit | Roughly even chance | %45–55 |
| Muhtemel | Likely | %55–80 |
| Çok muhtemel | Very likely | %80–95 |
| Neredeyse kesin | Almost certain | %95–99 |

Kurallar:
- Bu ifadeleri **yalnızca** bu anlamlarda kullanın. "Büyük ihtimalle", "belki", "kuvvetle muhtemel" gibi ölçek dışı ifadelerden kaçının.
- Olasılık (ne kadar muhtemel) ile güveni (değerlendirmenin dayandığı bilginin kalitesi) karıştırmayın. Gerekirse ayrıca "düşük/orta/yüksek güven" belirtin.
- Tahmin dili **analiz** içindir. Olgusal kayıtlarda olay ya doğrulanmıştır ya da iddia olarak atfedilir.

## İnceleyici için doğrulama kontrol listesi

- [ ] Her kaynak sicilde kayıtlı ve güvenilirlik notu var.
- [ ] Her kaynağın arşiv bağlantısı çalışıyor.
- [ ] Kaynakların bağımsızlığı gerçekten kontrol edildi.
- [ ] `credibility` ve `status` birbiriyle ve kurallarla tutarlı.
- [ ] Tartışmalı nitelendirmeler `claims[]` içinde ve atfedilmiş.
- [ ] Geolokasyon/kronolokasyon varsa yöntem açıklanmış ve tekrarlanabilir.
- [ ] Kısıtlı kaynak tek dayanak değil.
