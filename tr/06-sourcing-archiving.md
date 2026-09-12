# 06 · Kaynaklandırma ve Arşivleme

Kaynağı olmayan bilgi kayda girmez; arşivlenmemiş kaynak kalıcı değildir. Bu sayfa hangi kaynakları nasıl kullandığımızı ve nasıl arşivlediğimizi anlatır.

## Kaynak hiyerarşisi

Aşağıdaki sıralama bir **başlangıç noktasıdır**, otomatik güvenilirlik notu değildir. Her kaynak kendi geçmişine göre değerlendirilir ([05](05-verification.md)).

| Seviye | Tür | Örnekler | Not |
|---|---|---|---|
| 1 | Birincil resmî belge ve duyurular | Bakanlık açıklamaları, resmî gazeteler, NOTAM, NAVTEX, ihale ve sözleşme duyuruları, parlamento kayıtları, BM belgeleri | Olgusal duyurular için güçlü; tartışmalı konularda taraf |
| 2 | Birincil veri ve görüntü | Açık lisanslı uydu görüntüleri (ör. Copernicus Sentinel), kamuya açık ADS-B/AIS kayıtları (hizmet koşullarına uygun olarak), şirket bilançoları | Yorum gerektirir; yöntem belgelenir |
| 3 | Kendi haberini yapan medya | Sahada muhabiri olan ajans ve gazeteler | Kaynak zincirini kontrol edin |
| 4 | Uzman araştırmacılar ve düşünce kuruluşları | Yöntemini açıklayan OSINT araştırmacıları, akademik çalışmalar | Yöntem görünür olmalı |
| 5 | Sosyal medya ve Telegram kanalları | Tarafların resmî hesapları, savaş muhabirleri, yerel kanallar | Çoğunlukla **ipucu**; taraflı ve hızlı, sık yanılır |

**Kural:** Seviye 5 bir kaynak tek başına bir kaydı `verified` yapamaz; doğrulama için bağımsız bir kaynak veya geolokasyon/kronolokasyon gerekir.

## Kaynak sicili (`src_`)

Her kaynak `datasets` deposunda bir `source` kaydı olarak **bir kez** tanımlanır; kayıtlar ona ID ile atıf yapar.

Bir kaynak kaydında tipik olarak şunlar bulunur (kesin alanlar `datasets` şemalarındadır):
- ad (TR/EN), tür (resmî, medya, araştırmacı, sosyal medya kanalı…), dil,
- bağlı olduğu devlet/kurum (varsa; ör. devlet medyası),
- **güvenilirlik notu (A–F)** ve gerekçesi,
- **kullanım koşulları (`terms`)**.

### Kullanım koşulları (`terms`)

| Değer | Anlamı | Nasıl kullanılır? |
|---|---|---|
| `open` | Açık lisanslı veya kamu malı | Atıf yaparak özetlenebilir, bağlantı verilebilir |
| `attribution` | Serbestçe bağlantı verilebilir, atıf şart | Kendi cümlelerinizle özet + bağlantı + arşiv; kısa alıntı |
| `restricted` | Lisansı yeniden dağıtımı veya türev çalışmayı kısıtlıyor (ör. ACLED) | **Yalnızca ipucu.** Veri kopyalanmaz; kaydın tek kaynağı olamaz; asıl doğrulama başka kaynaklarla yapılır |
| `no-redistribution` | Hiçbir biçimde yeniden dağıtılamaz | Yalnızca ipucu; içerik aktarılmaz |

Yeni bir kaynağı sicile eklerken, sitenin kullanım koşullarını okuyun ve `terms` değerini gerekçesiyle yazın. Emin değilseniz daha kısıtlayıcı değeri seçin.

## Arşivleme

**Her kaynak bağlantısının bir arşiv kopyası olmalıdır.** Web sayfaları değişir, silinir, erişime kapatılır; Telegram gönderileri kaldırılır. Arşiv, iddianın **o anda** öyle yapıldığının kanıtıdır. `verified` bir kayıtta arşivsiz kaynak bulunamaz.

### Wayback Machine (Internet Archive) — Save Page Now

Tarayıcıda şu adrese gidin:

```
https://web.archive.org/save/<url>
```

veya https://web.archive.org/ adresindeki "Save Page Now" kutusunu kullanın. Oluşan bağlantı `https://web.archive.org/web/<zaman-damgası>/<url>` biçimindedir; bunu kaynağın arşiv alanına yazın.

### archive.today

https://archive.ph/ adresinde bağlantıyı girip kaydedin. Oluşan kısa bağlantıyı (`https://archive.ph/xxxxx`) kaynağın arşiv alanına yazın. Dinamik sayfalarda (sosyal medya) archive.today çoğu zaman Wayback'ten daha iyi sonuç verir.

### Pratik kurallar
- Mümkünse **her iki** arşive de kaydedin.
- Arşivin gerçekten içeriği gösterdiğini kontrol edin (giriş sayfası, çerez duvarı, "sayfa bulunamadı" arşivlenmiş olabilir).
- Arşivleme başarısız olursa bunu PR açıklamasında belirtin; kayıt `verified` olamaz ama `unverified` olarak girebilir.
- Otomatik toplayıcılar ileride arşivlemeyi kendileri tetikleyecek; yine de insan kontrolü şarttır.

## Medya dosyaları git'e konmaz

- Fotoğraf, video, ses, PDF, ekran görüntüsü **hiçbir koşulda** `datasets` veya `handbook` depolarına commit edilmez.
- Neden: telif hakkı, kişisel veri riski, depo boyutu ve geri alınamazlık (git geçmişinden silmek zordur).
- Bunun yerine: özgün bağlantı + arşiv bağlantısı. Gerekirse görüntünün ne gösterdiğini metinle anlatın ("videonun 0:14'ünde görülen su kulesi…").

## URL kuralları

### İzleme parametrelerini silin
Bağlantıları kanonik hâlde yazın. Aşağıdaki gibi parametreleri kaldırın:

`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `fbclid`, `gclid`, `igshid`, `si`, `mc_cid`, `mc_eid`, `ref`, `ref_src`, `s` / `t` (X paylaşım parametreleri) vb.

İçeriği belirleyen parametreler (ör. `?id=123`, `?p=456`) kalır. Emin değilseniz, parametreyi silip sayfanın hâlâ aynı içeriği gösterdiğini kontrol edin.

### Kısaltılmış bağlantı yok
`bit.ly`, `t.co`, `tinyurl.com`, `goo.gl`, `ow.ly`, `buff.ly`, `is.gd`, `cutt.ly` gibi kısaltıcılar **kabul edilmez** (CI engeller; tam liste `policy.yaml` içindedir). Kısaltılmış bağlantının açıldığı gerçek adresi bulun (tercihen tıklamadan, bir bağlantı genişletici ile) ve onu kullanın. Kısaltıcılar hem izleme hem de yönlendirme saldırısı riski taşır.

## Sosyal medya ve Telegram kaynakları

- Gönderinin **kalıcı bağlantısını** kullanın (profil veya ana sayfa değil).
  - Telegram: `https://t.me/<kanal>/<gönderi-no>`
  - Telegram açık web önizlemesi (hesap açmadan okumak ve arşivlemek için): `https://t.me/s/<kanal>`
- Yalnızca **açık, herkese açık** kanal ve hesaplar kaynak olabilir. Kapalı gruplar, özel mesajlar, davetle girilen kanallar kaynak değildir.
- Kanalın kime ait olduğunu (resmî hesap mı, taraftar kanalı mı, bir devletin medyası mı) sicilde belirtin.
- Gönderi silinebilir: **hemen arşivleyin**.
- Özel kişilerin hesapları kaynak olarak kullanılmaz ([02 §4](02-red-lines.md)). Bir tanığın paylaşımı olayı gösteriyorsa bile, kişinin hesabı kayda girmez; bilgi başka kaynakla doğrulanmaya çalışılır.
- Terör örgütlerine ait kanalların içeriği aktarılmaz; iddiaları gerekirse metin olarak ve atfedilerek kaydedilir ([03](03-legal-ethics.md)).

## Dil kodları

Kaynakların ve metinlerin dili **BCP 47** koduyla belirtilir:

| Kod | Dil |
|---|---|
| `tr` | Türkçe |
| `en` | İngilizce |
| `ar` | Arapça |
| `fa` | Farsça |
| `ku` / `kmr` / `ckb` | Kürtçe (genel) / Kurmanci / Sorani |
| `el` | Yunanca |
| `ru` | Rusça |
| `uk` | Ukraynaca |
| `hy` | Ermenice |
| `az` | Azerbaycan Türkçesi |
| `ka` | Gürcüce |
| `he` | İbranice |
| `fr` | Fransızca |

Gerekirse bölge alt etiketi eklenebilir (ör. `ar-SY`). Yazı sistemi farkı önemliyse betik alt etiketi kullanılır (ör. `az-Latn`, `az-Arab`).
