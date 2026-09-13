# 09 · Sözlük

Kayıtlarda, paylaşımlarda ve tartışmalarda kullandığımız terimler. Kısaltmalar metinde ilk geçtiği yerde açılır ([08](08-style-guide.md)).

## İstihbarat disiplinleri ve yöntem

| Türkçe | English | Açıklama |
|---|---|---|
| Açık kaynak istihbaratı (OSINT) | Open-source intelligence | Kamuya açık kaynaklardan toplanan ve analiz edilen bilgi. Topluluğumuzun tek yöntemi. |
| Coğrafi-uzamsal istihbarat (GEOINT) | Geospatial intelligence | Harita, uydu görüntüsü ve konum verisinin analizi. |
| Görüntü istihbaratı (IMINT) | Imagery intelligence | Hava ve uydu görüntülerinden elde edilen istihbarat. |
| Sinyal istihbaratı (SIGINT) | Signals intelligence | Elektronik sinyallerin ve haberleşmenin dinlenmesi. Devlet işidir; **biz yapmayız.** |
| Elektronik istihbarat (ELINT) | Electronic intelligence | SIGINT'in alt dalı: radar gibi haberleşme dışı elektronik yayınlardan elde edilen istihbarat. Devlet işidir; **biz yapmayız.** |
| Haberleşme istihbaratı (COMINT) | Communications intelligence | SIGINT'in alt dalı: haberleşmenin içeriğinden veya trafiğinden elde edilen istihbarat. **Biz yapmayız.** |
| Ölçüm ve iz istihbaratı (MASINT) | Measurement and signature intelligence | Nesnelerin ve olayların fiziksel izlerinden (akustik, sismik, spektral, radyasyon vb.) elde edilen teknik istihbarat. Devlet işidir; kamuya açık bilimsel ölçümlere (ör. sismik kayıtlar) atıf yapmak bundan farklıdır. |
| İstihbarat, gözetleme ve keşif (ISR) | Intelligence, surveillance and reconnaissance | Bilgi toplama faaliyetleri ve bunları yürüten platformların (keşif uçağı, İHA, uydu vb.) genel adı. |
| İnsan istihbaratı (HUMINT) | Human intelligence | Kişilerden bilgi toplama. **Kapsam dışı** ([02 §3](02-red-lines.md)). |
| Sosyal medya istihbaratı (SOCMINT) | Social media intelligence | Sosyal medyadaki açık içeriğin analizi. |
| Geolokasyon | Geolocation | Bir görüntünün çekildiği yeri belirleme ([07](07-geo-time-disputed.md)). |
| Kronolokasyon | Chronolocation | Bir görüntünün çekildiği zamanı belirleme. |
| Admiralty ölçeği | Admiralty scale | Kaynak güvenilirliği (A–F) ve bilgi inandırıcılığı (1–6) ölçeği ([05](05-verification.md)). |
| Bağımsız kaynak | Independent source | Bilgiyi başka bir kaynaktan ayrı bir yolla elde etmiş kaynak. |
| Dairesel raporlama | Circular reporting | Kaynakların birbirini aktararak tek bir bilgiyi çok kaynaklıymış gibi göstermesi. |
| Mozaik etkisi | Mosaic effect | Tek tek zararsız bilgilerin birleşince hassas bir tablo oluşturması. |
| Operasyon güvenliği (OPSEC) | Operational security | Kendinizi ve topluluğu açığa çıkarmamak için alınan önlemler ([04](04-opsec.md)). |
| Dezenformasyon | Disinformation | Kasıtlı olarak yayılan yanlış bilgi. |
| Mezenformasyon | Misinformation | Kasıt olmadan yayılan yanlış bilgi. |
| Kukla hesap | Sock puppet | Gerçek kimliği gizleyen sahte hesap. Hedeflerle etkileşimde **kullanılmaz.** |

## Uydu ve görüntüleme

| Türkçe | English | Açıklama |
|---|---|---|
| Elektro-optik / kızılötesi (EO/IR) | Electro-optical / infrared | Görünür ışıkta (EO) ve ısıl kızılötesinde (IR) çalışan algılayıcılar. EO bulut ve karanlıktan etkilenir; IR ısı farklarını gösterir. |
| Sentetik açıklıklı radar (SAR) | Synthetic aperture radar | Kendi radar sinyalini gönderip yansımasından görüntü üreten algılayıcı; bulut ve geceden etkilenmez (ör. Sentinel-1). Görüntüsü fotoğraf gibi okunmaz; yorum deneyim ister ([11](11-tools.md)). |
| Yer örnekleme aralığı (GSD) | Ground sample distance | Görüntüdeki bir pikselin yerde karşılık geldiği mesafe (ör. 10 m). Hangi nesnelerin ayırt edilebileceğini belirler. |
| Tekrar ziyaret süresi | Revisit time | Bir uydunun veya uydu takımının aynı noktayı yeniden görüntüleyebildiği süre. Kronolokasyondaki "iki geçiş arası" penceresini belirler ([07](07-geo-time-disputed.md)). |

## Havacılık ve denizcilik

| Türkçe | English | Açıklama |
|---|---|---|
| ADS-B | Automatic Dependent Surveillance–Broadcast | Uçakların konumlarını yayınladığı sistem; askerî uçaklar çoğu zaman kapatır. Türk askerî uçakları **izlenmez.** |
| AIS | Automatic Identification System | Gemilerin kimlik ve konum yayını; kapatılabilir ve sahtelenebilir. Türk savaş gemileri **izlenmez.** |
| NOTAM | Notice to Air Missions | Havacılara yönelik resmî duyuru (ör. atış, tatbikat, kapalı hava sahası). |
| NAVTEX | Navigational Telex | Denizcilere yönelik seyir uyarısı yayını (ör. atış ve tatbikat alanları). |
| Uçuş Bilgi Bölgesi (FIR) | Flight Information Region | Uçuş bilgi ve uyarı hizmetlerinin verildiği hava sahası bölümü; egemenlik alanı değildir. Ulusal hava sahasıyla karıştırılmamalıdır: Bir FIR uluslararası hava sahasını da kapsayabilir. |
| Ulusal hava sahası | National airspace | Bir devletin kara ülkesi ve karasuları üzerindeki, egemenliği altındaki hava sahası. FIR bir hizmet sorumluluğu, ulusal hava sahası ise egemenlik alanıdır; ikisi ayrı kavramlardır. Ege'de hava sahasının genişliği ihtilaflıdır; nitelendirmeler atfedilir ([07](07-geo-time-disputed.md)). |
| Hava Savunma Tanımlama Bölgesi (ADIZ) | Air Defence Identification Zone | Bir devletin tanımlama talep ettiği hava sahası bölgesi. |
| Karasuları | Territorial waters | Kıyı devletinin egemenliğindeki deniz şeridi. Genişliği Ege'de ihtilaflıdır. |
| Bitişik bölge | Contiguous zone | Karasularının ötesinde, kıyı devletinin gümrük, maliye, göç ve sağlık kurallarının ihlalini önlemek için sınırlı denetim yetkisi kullandığı bölge. Egemenlik alanı değildir. |
| Münhasır Ekonomik Bölge (MEB) | Exclusive Economic Zone (EEZ) | Kıyı devletinin su kütlesi, deniz yatağı ve toprak altındaki canlı ve cansız kaynaklar üzerinde egemen haklara sahip olduğu deniz alanı; ilan edilmesi gerekir. Egemenlik alanı değildir. |
| Kıta sahanlığı | Continental shelf | Kıyı devletinin deniz yatağı ve toprak altı kaynakları üzerindeki hak alanı. MEB'den farklı olarak su kütlesini kapsamaz ve ilan gerektirmez. Doğu Akdeniz ve Ege'deki MEB ve kıta sahanlığı sınırlandırmaları ihtilaflıdır; proje bunlar hakkında kendi sesiyle hüküm vermez ([07](07-geo-time-disputed.md)). |
| Askerden arındırılmış statü | Demilitarised status | Antlaşmalarla bir bölgede askerî kuvvet, tesis veya tahkimat bulundurulmasının sınırlandırılması ya da yasaklanması. Doğu Ege adalarının statüsü Türkiye ile Yunanistan arasında ihtilaflıdır; bu konudaki nitelendirmeler atfedilir ([07](07-geo-time-disputed.md)). |
| EGAYDAAK | Islands, islets and rocks whose sovereignty was not ceded to Greece by treaties | "Egemenliği Antlaşmalarla Yunanistan'a Devredilmemiş Ada, Adacık ve Kayalıklar": Türkiye'nin Ege'deki bu coğrafi unsurlar için kullandığı resmî terim. Yunanistan bu değerlendirmeyi kabul etmez. Proje terimi yayın dili olarak kullanır, egemenlik hükmü vermez ([07](07-geo-time-disputed.md)). |
| Önleme | Intercept | Bir hava aracının başka bir hava aracı tarafından tanımlama/eşlik amacıyla karşılanması. |
| GNSS karıştırma / aldatma | GNSS jamming / spoofing | Uydu konum sinyallerinin bastırılması / sahte sinyalle yanıltılması. |

## Platformlar ve silahlar

| Türkçe | English | Açıklama |
|---|---|---|
| İnsansız hava aracı (İHA) | Uncrewed aerial vehicle (UAV) | Pilotsuz hava aracı. |
| Silahlı İHA (SİHA) | Armed UAV / UCAV | Mühimmat taşıyabilen İHA. |
| MALE | Medium-Altitude Long-Endurance | Orta irtifa, uzun havada kalış sınıfı İHA. |
| HALE | High-Altitude Long-Endurance | Yüksek irtifa, uzun havada kalış sınıfı İHA. |
| Dolanan mühimmat | Loitering munition | Hedef bölgesi üzerinde bekleyip hedefe dalan tek kullanımlık mühimmat ("kamikaze İHA"). |
| İnsansız deniz aracı (İDA) | Uncrewed surface vessel (USV) | Pilotsuz su üstü aracı. |
| Hava erken uyarı ve kontrol uçağı (AEW&C) | Airborne early warning and control | Uzun menzilli radar taşıyan, geniş bir alanın hava resmini çıkaran ve hava harekâtının yönetimine destek veren uçak. |
| Balistik füze | Ballistic missile | Uçuşunun büyük bölümünü balistik yörüngede yapan füze. |
| Seyir füzesi | Cruise missile | Atmosfer içinde, genellikle alçak irtifada güdümlü uçan füze. |
| Taşıyıcı-dikleştirici-fırlatıcı (TEL) | Transporter erector launcher | Füzeyi taşıyan, atış konumuna dikleştiren ve fırlatan araç. |
| Karadan havaya füze (KHF / SAM) | Surface-to-air missile | Hava savunma füzesi. |
| Omuzdan atılan hava savunma sistemi (MANPADS) | Man-portable air-defence system | Tek kişi veya küçük bir ekip tarafından taşınıp atılabilen kısa menzilli hava savunma füzesi. |
| Elektronik harp (EH) | Electronic warfare (EW) | Elektromanyetik spektrumun saldırı, koruma ve destek amacıyla kullanımı. |
| Komuta, kontrol… (C4ISR) | Command, control, communications, computers, intelligence, surveillance, reconnaissance | Komuta-kontrol ve gözetleme sistemlerinin bütünü. |

## Hava savunma ve harekât kavramları

Bu terimler kaynaklardaki ifadeleri anlamak içindir. Kayıtlarda tarafların nitelendirmeleri atfedilir ([08](08-style-guide.md)).

| Türkçe | English | Açıklama |
|---|---|---|
| Entegre hava savunma sistemi (IADS) | Integrated air defence system | Radarların, hava savunma füzelerinin, önleme uçaklarının ve komuta-kontrol ağının tek bir bütün olarak çalıştığı hava savunma yapısı. |
| Füze angajman bölgesi (MEZ) | Missile engagement zone | Angajman sorumluluğunun normalde karadan havaya füze sistemlerinde olduğu hava sahası hacmi. Kaynaklarda bazen bir sistemin etkili menzilini anlatmak için de kullanılır. |
| Düşman hava savunmasının bastırılması (SEAD) | Suppression of enemy air defences | Hava savunma sistemlerini elektronik harp veya radar karşıtı mühimmatla geçici olarak etkisiz kılmaya yönelik harekât. Doktrin terimidir; kayıtlarda "düşman" nitelendirmesi projenin sesiyle kullanılmaz. |
| Erişim engelleme / alan hâkimiyeti (A2/AD) | Anti-access / area denial | Uzun menzilli füze, hava savunma, deniz ve elektronik harp kabiliyetleriyle karşı tarafın bir bölgeye girişini engelleme (A2) ve bölge içindeki hareket serbestliğini kısıtlama (AD) yaklaşımı. |
| Dairesel hata olasılığı (CEP) | Circular error probable | Atılan mühimmatın yarısının düşmesi beklenen, nişan noktası merkezli dairenin yarıçapı; isabet hassasiyeti ölçüsü. Üretici ve devlet beyanları iddiadır; atfedilir. |
| Muharebe hasar tespiti (BDA) | Battle damage assessment | Bir saldırının hedefte yol açtığı hasarın değerlendirilmesi. Tarafların hasar beyanları `claims[]` içinde atfedilir; uydu görüntüsüyle yapılan kendi gözlemimizin yöntemi kayda yazılır. |

## Askerî faaliyet ve tedarik

| Türkçe | English | Açıklama |
|---|---|---|
| Tatbikat | Exercise | Planlı askerî eğitim faaliyeti. |
| Konuşlanma | Deployment | Birliklerin veya sistemlerin bir bölgeye yerleştirilmesi. |
| Muharebe düzeni (ORBAT) | Order of battle | Kuvvetlerin yapısı, birlikleri ve teçhizatı. Türk kuvvetleri için **derlenmez.** |
| Tedarik | Procurement | Silah ve teçhizat alımı süreci. |
| Dış Askerî Satış (FMS) | Foreign Military Sales | ABD hükümetinin hükümetten hükümete silah satış programı. |
| Devlet dışı silahlı aktör | Non-state armed actor | Bir devletin resmî kuvvetlerine ait olmayan silahlı grup. |

## Proje terimleri

| Türkçe | English | Açıklama |
|---|---|---|
| Kayıt | Record | `datasets` deposundaki tek bir YAML dosyası (olay, aktör, tesis, teçhizat, kaynak). |
| Mezar taşı | Tombstone | Geri çekilen bir kaydın yerini alan `schema: tombstone/1` dosyası; ID yeniden kullanılmaz. |
| TypeID | TypeID | `<önek>_<26 karakter>` biçimindeki kalıcı kayıt kimliği ([ADR 0003](../decisions/0003-identifiers.md)). |
| İddia | Claim | `claims[]` içinde bir tarafa atfedilen nitelendirme. |
| Kaynak sicili | Source registry | Kaynakların güvenilirlik notu ve kullanım koşullarıyla tanımlandığı `src_` kayıtları. |
| Türk kuvvetleri kapısı | Turkish forces gate | Türk güvenlik unsurlarını içeren kayıtlar için CI kontrolü ([02](02-red-lines.md)). |
| Bülten | Bulletin | Henüz kayda dönüşmemiş, insan onaylı kısa bilgi paylaşımı ([ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)). |
