# 01 · Misyon ve Kapsam

## Misyon

Greater Türkiye, Türkiye'nin **dış güvenlik ortamını** açık kaynaklardan izleyen bir topluluktur. Amacımız; yabancı ordular, komşu bölgelerdeki çatışmalar, savunma tedarikleri, tatbikatlar, konuşlanmalar ve olaylar hakkında **kaynaklandırılmış, arşivlenmiş, doğrulama derecesi açıkça belirtilmiş** kayıtlar üretmek ve bunları herkesin kullanabileceği açık veri olarak yayımlamaktır.

Yaklaşımımız **dışa dönük, analitik ve savunma amaçlıdır**. Gözlemleriz, kaydederiz, bağlama oturturuz. Hedef göstermeyiz, tahrik etmeyiz, sahaya çıkmayız.

## Kimiz?

- Gönüllü, bütçesiz, topluluk temelli bir girişimiz. Tüzel kişiliğimiz yoktur.
- **Hiçbir devlet kurumu, ordu, istihbarat servisi, siyasi parti veya şirketle bağlantımız yoktur**; kimseden talimat veya para almayız. Hiçbir kurum adına konuşmayız.
- Takma adla (pseudonim) katkı kabul edilir. Kimliğinizi açıklamak zorunda değilsiniz.
- Birincil dilimiz Türkçedir; İngilizce ikinci dildir. Kayıtlarda her iki dilde metin bulunur.
- Veriler ve içerik CC BY 4.0, kod MIT lisanslıdır.

## Kapsam içi

| Konu | Örnekler |
|---|---|
| Yabancı askerî faaliyet | Tatbikatlar, konuşlanmalar, üs açılış/kapanışları, deniz ve hava faaliyeti |
| Olaylar | Önleme (intercept), sınır olayları, saldırılar, kazalar, deniz olayları — iddialar atfedilerek |
| Tedarik ve sanayi | Silah alımları, sözleşmeler, teslimatlar, ihracat onayları, üretim kapasitesi |
| Aktörler | Yabancı devlet kurumları, silahlı kuvvetler, devlet dışı silahlı gruplar, uluslararası misyonlar |
| Tesisler | Yabancı askerî üsler, limanlar, havaalanları — kamuya açık bilgilerle |
| Teçhizat | Platformlar ve sistemler (türler, varyantlar, envanter iddiaları) |
| Resmî açıklamalar | Bakanlıklar, genelkurmaylar, uluslararası kuruluşlar, NOTAM/NAVTEX duyuruları |
| Dezenformasyon | Yanlış çıkan iddialar `false` durumuyla kayıtta tutulur |

## Kapsam dışı

| Konu | Neden |
|---|---|
| **Türk Silahlı Kuvvetleri, Jandarma, Emniyet, MİT ve diğer Türk güvenlik unsurlarının konum ve hareketleri** | Kırmızı çizgi. Resmî açıklamalar dışında hiçbir şey; olanlar da kaba ve gecikmeli. Bkz. [02](02-red-lines.md) |
| Türkiye iç siyaseti, seçimler, partiler | Misyon dışı |
| Özel kişiler, kişisel veriler | KVKK ve etik; bkz. [03](03-legal-ethics.md) |
| Gizli/sızdırılmış belgeler (hangi ülkeden olursa olsun) | Kırmızı çizgi |
| Sahada toplama (fotoğraf, keşif, iletişim kurma) | Kırmızı çizgi; 2565 sayılı Kanun ve benzerleri |
| Siber saldırı, sistemlere yetkisiz erişim, aktif tarama | Yasa dışı ve misyon dışı |
| Hedefleme, operasyonel tavsiye | Analitik ve savunma amaçlı bir topluluğuz |

## İzlenen bölgeler

Bölgeler egemenlik iddiası değil, **editoryal izleme alanlarıdır**. Bir kayıt birden fazla bölgeye ait olabilir. Kanonik liste `datasets` deposundaki `vocab/regions.yaml` dosyasıdır; aşağıdaki tablo özettir.

| Kod | Bölge (TR) | Region (EN) | Not |
|---|---|---|---|
| `syria` | Suriye | Syria | |
| `iraq` | Irak | Iraq | Kuzey Irak dahil |
| `iran` | İran | Iran | |
| `levant` | Levant (Doğu Akdeniz kıyı ülkeleri) | Levant | Lübnan, İsrail, Filistin, Ürdün |
| `caucasus` | Kafkasya | Caucasus | Azerbaycan, Ermenistan, Gürcistan, Kuzey Kafkasya |
| `aegean` | Ege | Aegean | Ege Denizi ve adaları |
| `east-med` | Doğu Akdeniz | Eastern Mediterranean | Deniz yetki alanları, enerji |
| `cyprus` | Kıbrıs | Cyprus | KKTC (`XNC`) ve GKRY (`CYP`) |
| `black-sea` | Karadeniz | Black Sea | Rusya–Ukrayna savaşının deniz boyutu dahil |
| `libya-north-africa` | Libya / Kuzey Afrika | Libya / North Africa | Sahel bağlantıları dahil |
| `gulf-red-sea` | Körfez / Kızıldeniz | Gulf / Red Sea | Basra Körfezi, Kızıldeniz, Bab-ül Mendep, Afrika Boynuzu |
| `balkans` | Balkanlar | Balkans | |
| `central-asia` | Orta Asya | Central Asia | |
| `global` | Küresel | Global | Büyük güçler, NATO, küresel tedarik |

## Veri ne işe yarar?

- Araştırmacılar, gazeteciler ve analistler için kaynaklı, tekrar üretilebilir bir olay arşivi.
- Dezenformasyona karşı referans: iddianın kim tarafından, ne zaman yapıldığı ve doğrulanıp doğrulanmadığı.
- Kamuya açık bilgilerle bölgesel eğilimlerin (tatbikat sıklığı, tedarik akışları vb.) izlenmesi.

## İlkelerin özeti

1. **Önce güvenlik**: Şüphedeysen yayımlama. Bkz. [Kırmızı Çizgiler](02-red-lines.md).
2. **Atıf**: Tartışmalı her nitelendirme, onu yapana atfedilir.
3. **Şeffaflık**: Her kaynak arşivlenir, her düzeltme kayıtta görünür.
4. **İnsan onayı**: Hiçbir içerik insan onayı olmadan yayımlanmaz.
5. **Sıfır bütçe**: Sadece ücretsiz katmanlar; ödeme yöntemi tanımlanmaz.
