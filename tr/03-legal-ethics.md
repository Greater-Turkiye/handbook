# 03 · Hukuk ve Etik

> **Bu sayfa hukuki tavsiye değildir.** Amacı, katkıcıların hangi mevzuatın bu işle ilgili olduğunu bilmesini sağlamaktır. Kanun metinlerinin güncel hâline mevzuat.gov.tr üzerinden bakın; somut bir durumda bir avukata danışın.

## Temel gerçek: sorumluluk kişiseldir

- Greater Türkiye'nin **tüzel kişiliği yoktur**. Dernek, vakıf veya şirket değildir; sizi temsil edecek, savunacak ya da sorumluluğu üstlenecek bir kurum yoktur.
- Yaptığınız her katkının hukuki sorumluluğu **size aittir**.
- Takma ad kullanmak sizi hukuken korumaz; platformlar yasal taleplere uyar ([04 · OPSEC](04-opsec.md)).
- Türkiye dışındaki katkıcılar, bulundukları ülkenin (ve vatandaşı oldukları ülkenin) yasalarına da uymak zorundadır. Pek çok ülkede askerî tesislerin fotoğraflanması, gizli bilgi, casusluk ve kişisel veri konusunda sıkı kurallar vardır.

## İlgili Türk mevzuatı

### Türk Ceza Kanunu (5237) m. 326–339 — Devlet sırlarına karşı suçlar ve casusluk

Bu bölüm; devletin güvenliğine veya iç ya da dış siyasal yararlarına ilişkin, niteliği itibarıyla gizli kalması gereken bilgilerin **temin edilmesi, açıklanması**, bu nitelikteki belgelerin yok edilmesi veya sahteleştirilmesi, **siyasal veya askerî casusluk** ve yetkili makamlarca açıklanması **yasaklanan bilgilerin** temin edilmesi ve açıklanması gibi fiilleri düzenler. Cezalar ağırdır.

**Bizim için anlamı:**
- Kamuya açık bilgiler de bir araya getirildiğinde (mozaik etkisi) hassas bir nitelik kazanabilir. Türk kuvvetlerine dair hiçbir derleme yapmamamızın temel nedeni budur ([02 · Kırmızı çizgiler §1](02-red-lines.md)).
- Gizli veya sızdırılmış materyal hiçbir koşulda kullanılmaz ([02 §2](02-red-lines.md)).
- Yayın yasağı getirilmiş bir konuda, yasak süresince içerik üretilmez; bakımcılar bu tür yasakları duyurur.

### TCK m. 217/A — Halkı yanıltıcı bilgiyi alenen yayma

Ülkenin iç ve dış güvenliği, kamu düzeni ve genel sağlığı ile ilgili **gerçeğe aykırı bir bilgiyi**, halk arasında endişe, korku veya panik yaratmak saikiyle ve kamu barışını bozmaya elverişli şekilde **alenen yaymayı** suç olarak tanımlar. Suçun **failin gerçek kimliğini gizlemek suretiyle** veya bir örgütün faaliyeti çerçevesinde işlenmesi cezayı artıran bir hâldir.

**Bizim için anlamı:**
- Doğrulanmamış bilgi, doğrulanmamış olarak işaretlenir (`unverified`) ve **atfedilerek** yazılır; asla kesin bilgi gibi sunulmaz ([05 · Doğrulama](05-verification.md)).
- Sansasyonel, panik yaratan dil kullanılmaz ([08 · Yazım kılavuzu](08-style-guide.md)).
- Yanlış çıkan iddialar düzeltme ile işaretlenir; paylaşım kanallarında da düzeltme yayımlanır.
- Takma adla çalışmanın bu maddede cezayı artıran bir unsur olabileceğini bilin; doğruluk ve atıf kuralları bu yüzden de hayatidir.

### 2565 sayılı Askerî Yasak Bölgeler ve Güvenlik Bölgeleri Kanunu

Askerî yasak bölgelere ve güvenlik bölgelerine izinsiz girmeyi; buralarda fotoğraf ve film çekmeyi, kroki, resim, plan çizmeyi, not almayı ve benzeri faaliyetleri yasaklar ve cezalandırır.

**Bizim için anlamı:** Sahada toplama yapmayız. Hiçbir katkıcı topluluk için bir tesise gitmez, çekim yapmaz, drone uçurmaz ([02 §3](02-red-lines.md)).

### 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK)

Kimliği belirli veya belirlenebilir gerçek kişiye ilişkin her türlü bilginin işlenmesini düzenler; sağlık, din, etnik köken, siyasi düşünce gibi **özel nitelikli kişisel veriler** için daha sıkı kurallar öngörür.

**Bizim için anlamı:** Özel kişilere dair veri toplamayız, saklamayız, yayımlamayız. Resmî görevlilere yalnızca resmî sıfatlarıyla atıf yapılır. CI; T.C. kimlik numarası, telefon, e-posta, IBAN gibi kalıpları tarar ([ADR 0010](../decisions/0010-content-safety-gates.md)).

### 5651 sayılı Kanun — İnternet ortamında yapılan yayınlar

İçerik, yer ve erişim sağlayıcıların sorumluluklarını; içeriğin çıkarılması ve **erişimin engellenmesi** usullerini düzenler. Millî güvenlik ve kamu düzeni gerekçesiyle hızlı erişim engelleme yolları da vardır.

**Bizim için anlamı:**
- Kayıt yazan katkıcı, o içeriğin **içerik sağlayıcısı** konumundadır.
- Projenin veya kanallarımızın Türkiye'den erişime kapatılması ihtimaline karşı veriler Zenodo ve klonlar gibi aynalarla korunur ([ADR 0011](../decisions/0011-threat-model.md)).
- Resmî bir içerik çıkarma talebi gelirse bakımcılar değerlendirir; talep ve yapılan işlem, hukuken mümkün olduğu ölçüde şeffaf biçimde kayda geçirilir.

### Ayrıca göz önünde bulundurun

- **3713 sayılı Terörle Mücadele Kanunu**: Terör örgütü propagandası suçtur. Terör örgütlerinin propaganda görüntüleri, bildirileri ve sembolleri paylaşılmaz; bu örgütlerin iddiaları yalnızca metin olarak, atfedilerek ve gerekli olduğunda kaydedilir.
- **Fikir ve Sanat Eserleri Kanunu (5846)**: Telif hakkı. Kopyalama yok, özet ve bağlantı var.

## Etik ilkeler

### 1. Doğruluk
- Doğrulama derecesini abartmayın. Bilmediğinizi bilmediğinizi yazın.
- Kesinlik gerektirmeyen yerde kesin dil kullanmayın; tahmin dilini doğru kullanın ([05](05-verification.md)).
- İki bağımsız kaynak "iki haber sitesi" değil, **birbirinden bağımsız iki bilgi zinciri** demektir.

### 2. Atıf
- Proje kendi sesiyle tartışmalı nitelendirme yapmaz. İddialar sahibine atfedilir.
- Başkasının doğrulama çalışmasını kullanıyorsanız (ör. bir geolokasyon), onu yapana kredi verin.

### 3. Zararı en aza indirme
- "Bu bilginin yayımlanması kime zarar verebilir?" sorusunu her kayıtta sorun.
- Sivillerin, esirlerin, yaralıların, ailelerin onurunu koruyun.
- Hassas bilgilerde gecikme ve kaba konum, hızdan her zaman daha değerlidir.
- Kamu yararı ile zarar çatışıyorsa, kararı bakımcılar verir; varsayılan cevap "yayımlama"dır.

### 4. Düzeltmeler
- Hata yapmak normaldir; hatayı gizlemek değildir.
- Düzeltmeler `corrections[]` alanına tarih ve açıklamayla eklenir; eski hâl git geçmişinde görünür kalır.
- Önemli düzeltmeler, ilk paylaşımın yapıldığı kanallarda da otomatik olarak duyurulur ([ADR 0007](../decisions/0007-human-in-the-loop-publishing.md)).

### 5. Bağımsızlık ve çıkar çatışması
- Kimsenin adına çalışmayız. Bir savunma şirketinde, devlet kurumunda veya ilgili bir kuruluşta çalışıyorsanız, o kuruma dair kayıtları incelemeyin (inceleme sırasında çekimser kalın).
- Topluluk adına bağış, sponsorluk veya ödeme kabul edilmez.

## Resmî talepler ve sizin haklarınız

- Bir resmî kurumdan topluluğa dair talep alırsanız, kendi adınıza hukuki destek alın ve (hukuken mümkünse) bakımcıları bilgilendirin.
- Bakımcılar da hukuki tavsiye veremez; topluluğun kuralları hukuki korumanın yerine geçmez.
