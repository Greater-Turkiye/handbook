# 02 · Kırmızı Çizgiler

Bu sayfadaki kurallar **mutlaktır**. İstisnası, pazarlığı, "ama herkes paylaşıyor" gerekçesi yoktur. Bir kuralın uygulanıp uygulanmayacağından emin değilseniz, **uygulanıyor sayın ve yayımlamayın**; bakımcılara özel kanaldan sorun.

Her katkıcı bu sayfayı okumuş ve kabul etmiş sayılır. İnceleyiciler (reviewers) her PR'da bu kuralları kontrol eder; CI bunların bir kısmını otomatik uygular ([ADR 0010](../decisions/0010-content-safety-gates.md)), ama **son sorumluluk insanındır**.

> **Temel ilke:** Şüphedeysen yayımlama. Yanlışlıkla eksik yayımlamanın maliyeti küçüktür; yanlışlıkla fazla yayımlamanın maliyeti geri alınamaz.

---

## 1. Türk kuvvetlerinin konum ve hareketleri

Türk Silahlı Kuvvetleri, Jandarma, Sahil Güvenlik, Emniyet, MİT ve diğer Türk güvenlik/istihbarat unsurlarının **konum, hareket, konuşlanma, düzen, kabiliyet açığı veya zafiyetine** dair hiçbir bilgi yayımlanmaz, toplanmaz, analiz edilmez.

- **Tek istisna resmî açıklamalardır** (Millî Savunma Bakanlığı, Genelkurmay, ilgili kurumların resmî duyuruları). Bunlar bile yalnızca:
  - **koordinatsız**,
  - konum hassasiyeti yalnızca `admin1`, `country` veya `sea-area`,
  - olaydan **en az 24 saat sonra**,
  - `policy.sensitivity: elevated` ile,
  - bir bakımcının `policy:approved` etiketiyle yayımlanabilir.
- **Harita katmanı istisnası:** Türk devletinin resmî olarak ilan ettiği harekât bölgeleri, **bölgenin tamamı olarak** haritada gösterilebilir. Üs, karakol, birlik ve hareket bilgisi yine gösterilmez ([ADR 0015](../decisions/0015-announced-operation-areas.md)).
- Bu kurallar CI'daki **"Türk kuvvetleri kapısı"** tarafından da uygulanır: Türk askerî/güvenlik/istihbarat aktörü `perpetrator`, `participant`, `target` veya `host` rolüyle kayıttaysa ya da `policy.involves_tur_forces: true` ise yukarıdaki koşullar sağlanmadan kayıt birleştirilemez.
- Resmî olmayan görüntüler (sosyal medyada paylaşılan konvoy videoları, tatbikat fotoğrafları, "şu an şuradan geçiyorlar" paylaşımları) **kamuya açık olsa bile kullanılmaz**, bağlantısı verilmez, geolokasyonu yapılmaz.
- Türk askerî uçaklarının ADS-B, gemilerinin AIS verisi **izlenmez, kaydedilmez, paylaşılmaz.**
- Türkiye topraklarındaki askerî tesisler (müttefik/NATO tesisleri dahil) ve savunma sanayii tesislerinin güvenlik ayrıntıları kapsam dışıdır. Bunlara değinen bir kayıt zorunluysa `policy.involves_tur_forces: true` işaretlenir ve aynı kapıdan geçer.
- Yabancı bir kaynağın Türk kuvvetleri hakkındaki iddiası (ör. "X ülkesi, Türk İHA'larının şu bölgede uçtuğunu iddia etti") da bu kurallara tabidir: atfedilir, kaba tutulur, gecikmeli yayımlanır, onay gerektirir.

**Neden?** Açık kaynakta dağınık duran bilgilerin bir araya getirilmesi (mozaik etkisi) tek tek zararsız görünen parçalardan hassas bir tablo çıkarabilir. Biz o tabloyu çizmeyiz.

## 2. Gizli veya sızdırılmış materyal — hangi ülkeden olursa olsun

- Gizlilik dereceli (ör. GİZLİ, ÇOK GİZLİ, HİZMETE ÖZEL, SECRET, TOP SECRET, NOFORN, CONFIDENTIAL) veya sızdırılmış belgeler, görüntüler, veri tabanları **kaynak olarak kullanılmaz, alıntılanmaz, özetlenmez, bağlantısı verilmez, analiz edilmez.**
- Bu kural, sızıntı bir başka ülkeye ait olsa ve ana akım medyada yayımlanmış olsa da geçerlidir.
- Bir olay yalnızca sızıntı üzerinden biliniyorsa, kayda girmez.
- En fazla, resmî bir makamın bir sızıntı hakkında yaptığı açıklama, **sızıntının içeriği aktarılmadan** atfedilerek kaydedilebilir (bakımcı onayıyla).
- Size özelden böyle bir materyal gelirse: açmayın, iletmeyin, depolamayın; bakımcıları [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) kanalından bilgilendirin.

## 3. Sahada toplama yok

Biz **yalnızca kamuya açık, pasif kaynaklarla** çalışırız.

- Askerî yasak bölgelerde ve güvenlik bölgelerinde fotoğraf/video çekmek, kroki çizmek, drone uçurmak yasaktır (Türkiye'de **2565 sayılı Askerî Yasak Bölgeler ve Güvenlik Bölgeleri Kanunu**; birçok ülkede benzer yasalar vardır). Topluluk adına veya topluluğa katkı için **hiçbir tesise gidilmez, gözlem yapılmaz.**
- Askerî personelle, görevlilerle veya olay tanıklarıyla bilgi almak amacıyla **iletişim kurulmaz**; sosyal mühendislik yapılmaz.
- Kamuya açık olmayan sistemlere erişilmez: parola denemesi, sızdırılmış kimlik bilgisi kullanımı, port taraması, zafiyet taraması, kapalı grupların içine sahte hesapla girme **yoktur.**
- Başkalarının sahada topladığı materyali "biz çekmedik" diyerek kullanmak da, eğer materyal yasadışı yolla elde edilmiş görünüyorsa, yasaktır.

## 4. Özel kişiler ve kişisel veriler

- **Özel kişilerin** adı, yüzü, adresi, telefonu, e-postası, kimlik numarası, plakası, sosyal medya hesabı kayda girmez (**6698 sayılı KVKK**).
- Herhangi bir ülkenin **rütbesiz/alt kademe askerî personeli** kimliklendirilmez; sosyal medya profilleri araştırılmaz, paylaşılmaz. Doxxing (kişiyi ifşa etme) yasaktır.
- Resmî sıfatıyla kamuya açık faaliyet gösteren üst düzey kişiler (bakan, genelkurmay başkanı, sözcü) yalnızca **resmî rolleriyle ve resmî açıklamaları bağlamında** aktör olarak geçebilir.
- Özel nitelikli kişisel veriler (sağlık, din, etnik köken, siyasi görüş vb.) hiçbir koşulda kayda girmez.
- Görüntülerde ve ekran görüntülerinde yüzler, plakalar, kullanıcı adları kaldırılmadan hiçbir şey paylaşılmaz — ve zaten medya depoya konmaz ([06](06-sourcing-archiving.md)).

## 5. Esir ve kayıp görüntüsü yok

- Savaş esirlerinin, gözaltındakilerin, ölü veya yaralıların **fotoğraf ve videoları paylaşılmaz, bağlantısı verilmez, betimlenmez.** (Esirlerin kamu merakına karşı korunması III. Cenevre Sözleşmesi'nin 13. maddesinde de yer alır.)
- Kayıp sayıları yalnızca **metin olarak ve atfedilerek** kaydedilir: "X Savunma Bakanlığı'na göre 4 asker hayatını kaybetti."
- Şiddet içerikli görüntüden kanıt olarak yararlanmak gerekiyorsa bile (ör. bir saldırının yerini doğrulamak), görüntünün kendisi yayımlanmaz; yalnızca doğrulama sonucu ve arşiv bağlantısı (bakımcı onayıyla, uyarı notuyla) kayda girer.

## 6. Hedefleme dili ve tahrik yok

- Kayıtlar, paylaşımlar ve yorumlar **hedef göstermez**: "Burası vurulmalı", "şu koordinatlar hedef", "şu kişiyi bulun" gibi ifadeler yasaktır.
- Herhangi bir silahlı tarafa **operasyonel tavsiye** verilmez (hangi silahla, nereden, ne zaman).
- Şiddete, intikama, linç kültürüne çağrı yapılmaz; ödül, bağış, "gönüllü toplama" duyurusu yapılmaz.
- Koordinatlar bir olayın **gerçekleştiği yeri** belgelemek içindir; asla "gelecekteki bir eylem" için sunulmaz.

## 7. Nefret söylemi yok

- Hiçbir halka, etnik kökene, dine, mezhebe veya milliyete karşı aşağılayıcı, genelleyici, insanlıktan çıkarıcı dil kullanılmaz.
- **Örgütler ile halklar ayrılır.** Bir örgütün eylemleri o örgüte atfedilir; bir halka yüklenmez. Örneğin PKK'nın eylemleri PKK'ya aittir, Kürtlere değil; bir devletin eylemleri o devletin hükümetine veya kuvvetlerine aittir, halkına değil.
- Terör örgütü nitelendirmeleri de atfedilir: "Türkiye, ABD ve AB tarafından terör örgütü olarak listelenen PKK…" gibi.

## 8. Her zaman atıf

- Tartışmalı veya doğrulanmamış her bilgi, onu söyleyene atfedilir: **"…'e göre", "…'nın iddiasına göre", "…'nın açıklamasına göre".**
- Proje kendi sesiyle tartışmalı nitelendirme **yapmaz**. "Hava sahası ihlali", "provokasyon", "saldırganlık", "işgal", "terör saldırısı" gibi nitelendirmeler `claims[]` alanında, sahibine atfedilerek kaydedilir.
- Kaynak göstermeden bilgi yazılmaz. "Kulağıma geldi", "bir arkadaş söyledi" kaynak değildir.

## 9. Telif hakkı

- Makaleler, raporlar, görseller, videolar **kopyalanmaz**, depoya konmaz, yeniden yayımlanmaz.
- Kendi cümlelerinizle özetleyin; bağlantı ve arşiv bağlantısı verin.
- Yalnızca bir iddiayı doğru aktarmak için **kısa alıntı** yapılabilir (tırnak içinde, kaynağıyla).
- `terms: restricted` veya `no-redistribution` olan kaynakların (ör. ACLED) verisi kopyalanmaz; bunlar yalnızca **ipucu** olarak kullanılır ve hiçbir kaydın **tek** kaynağı olamaz.

---

## İhlaller nasıl ele alınır?

| Durum | Ne olur? |
|---|---|
| Birleşmemiş PR'da ihlal | PR hemen kapatılır; gerekirse yorumlar gizlenir/silinir. Hassas içerik varsa bakımcılar GitHub'dan önbellek temizliği ister. |
| Birleşmiş kayıtta ihlal | Kayıt `schema: tombstone/1` ile geri çekilir (ID asla yeniden kullanılmaz). Kanal paylaşımları silinir; düzeltme notu yayımlanır. |
| Kişisel veri veya gizli materyal git geçmişine girdiyse | Mezar taşı yetmez: bakımcılar geçmişi temizler ve GitHub Destek'ten önbellek kaldırma ister. Bu, "dosya silinmez" kuralının belgelenmiş tek istisnasıdır; ID yine mezar taşı olarak kalır. |
| Katkıcı davranışı | İlk ve hafif ihlalde uyarı; tekrarında geçici uzaklaştırma; Türk kuvvetleri, gizli materyal, doxxing, hedefleme veya nefret söylemi gibi ağır ihlallerde **doğrudan kalıcı yasak** ve yetkilerin geri alınması. |
| Kasıtlı zehirleme (sahte kaynak, uydurma kayıt) | Kalıcı yasak; katkıcının diğer tüm kayıtları yeniden incelenir. |

İhlal fark ederseniz: **herkese açık yorumla dikkat çekmeyin** (içeriği daha görünür yapar). [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) içindeki özel iletişim adresine yazın.

## Hızlı kontrol listesi (PR göndermeden önce)

- [ ] Kayıtta Türk kuvvetlerine dair resmî açıklama dışı bir bilgi yok.
- [ ] Gizli/sızdırılmış materyal yok.
- [ ] Sahada toplanmış materyal yok.
- [ ] Özel kişi, kişisel veri, alt kademe personel kimliği yok.
- [ ] Esir/kayıp görüntüsü veya bağlantısı yok.
- [ ] Hedef gösteren, tahrik eden, nefret içeren ifade yok.
- [ ] Tartışmalı her nitelendirme `claims[]` içinde ve atfedilmiş.
- [ ] Kopyalanmış metin/görsel yok; kısıtlı kaynak tek kaynak değil.
