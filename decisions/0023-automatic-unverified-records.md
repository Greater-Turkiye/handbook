# 0023 · Doğrulanmamış kayıtların otomatik yayını

> **EN:** Amends [0007](0007-human-in-the-loop-publishing.md) for one class of records. Candidates that pass the collector's relevance filter and its safety gates are written to `datasets` as event records automatically, with no person reading them first. They are published as what they are: `assessment.status: unverified`, `credibility: 6` ("cannot be judged"), a bilingual note saying no one reviewed them, machine-written title and summary marked in `i18n.machine`, and the tag `otomatik`. Verification comes later, as a separate pass over that tag. Everything 0007 guards that is not volume stays guarded: nothing about Turkish forces is published automatically, sources graded E or F never feed it, the content-policy validator runs on every record, and a single repository variable stops it.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-24
- **Önerenler:** @nukIeer
- **İlgili:** [0006](0006-verification-scale.md), [0007](0007-human-in-the-loop-publishing.md) (kısmen değiştirir), [0009](0009-licensing.md), [0010](0010-content-safety-gates.md), [0011](0011-threat-model.md)

## Bağlam

0007 her kaydın veri setine girmeden önce bir insan tarafından okunmasını şart koştu. Toplayıcılar
ve ilgi süzgeci çalışmaya başladıktan sonra darboğazın tam da orada olduğu görüldü: 2026-09-24'te
günlük kuyruk 40 aday ve 39 ertelenen aday üretiyordu, veri setinde ise 13 olay vardı. İnceleyici
emeği olmadan kayıt birikmiyor; kayıt birikmeden de doğrulayacak bir şey olmuyor.

Sahip (owner) kararı açık: veriler doğrulanmamış olarak yayımlansın, doğrulama sistemleri sonra
eklensin.

## Karar

### Ne otomatik yayımlanır

Toplayıcının partisinde `queued` ya da `pending` durumundaki, yani ilgi süzgecinden (bölge **ve**
olay türü) geçmiş her aday. `datasets` deposundaki zamanlanmış iş (`auto-records.yml`) son üç günün
partilerini okur ve:

1. Zaten bir kayıtta kaynak olarak geçen adresleri atlar.
2. GitHub Models'a her adayın başlığını ve alıntısını verir; model (a) yazının bir **olay** mı yoksa
   analiz, yorum, özet, röportaj mı olduğuna karar verir, (b) türü sözlükten seçer, (c) aynı günün aynı
   bölgesindeki tekrar haberleri işaretler ve (d) Türkçe ve İngilizce başlık ve özet yazar. Olay
   olmayanlar kayda dönüşmez; tekrarlar tek kayda birden çok kaynak olarak girer.
3. Kaydı yazar, `gt.py validate` ile doğrular, geçmeyeni siler, geçenleri doğrudan `main`'e işler.

### Kayıt ne olduğunu söyler

| alan | değer |
|---|---|
| `assessment.status` | `unverified` — hiçbir zaman daha iyi değil |
| `assessment.credibility` | `6` (değerlendirilemez) |
| `assessment.note` | "Otomatik kayıt … kimse okumadan yayımlandı (ADR 0023)", akış adı ve çalıştırma bağlantısıyla |
| `i18n` | `source: en`, `machine: [tr, en]` |
| `tags` | `otomatik` |
| `time` | yayın günü, `precision: day`, `basis: reported` |

Kayıt kaynağın metnini kopyalamaz ([0009](0009-licensing.md)): başlık ve özet modelin kendi
cümleleriyle, kaynağa atfedilerek ("…'a göre") yazılır; kaynağın kendi başlığı yalnızca atıf olarak
`sources[].title` içinde durur.

### Neler değişmedi

- **Türk kuvvetleri.** Toplayıcının güvenlik süzgecinin düşürdüğü hiçbir şey kuyruğa zaten girmez;
  `redline_check` işaretli adaylar ve metninde Türk kuvvetlerini anan her aday otomatik yoldan
  **atlanır** ve bir insanı bekler. [0010](0010-content-safety-gates.md)'daki kapı gevşetilmez.
- **Kaynak kalitesi.** E ve F notlu kaynaklar kuyruğa giremez, dolayısıyla bu yola da giremez.
- **İçerik politikası.** Kişisel veri, gizlilik işaretleri ve konum kuralları her kayıtta
  doğrulayıcı tarafından denetlenir; model özel kişileri adlandırmamakla talimatlıdır.
- **Doğrulanmış kayıtlar.** `verified` ve `partially_verified` hâlâ insan işidir; 0006 aynen geçerli.
  Herkese açık akış (`feed.xml`) yalnızca bu iki durumu yayar, otomatik kayıtlar oraya girmez.
- **Acil durdurma.** `datasets` deposunun `AUTO_RECORDS` değişkeni `on` değilse iş hiçbir şey yazmaz.
  Bir bakımcı onu `off` yapınca otomatik yayın durur ([0007](0007-human-in-the-loop-publishing.md)).

### `main`'e doğrudan yazma

Kuruluş ayarları GitHub Actions'ın çekme isteği açmasına izin vermiyor. Bu yüzden `main` kural
setine yalnızca GitHub Actions uygulaması için bir atlama (bypass) eklendi. İş `validate`'i kendisi
çalıştırır ve geçmeyen dosyayı yazmaz. Çatallardan (fork) gelen çekme isteklerinin belirteci
salt okunurdur; atlama onlara yetki vermez.

## Sonuçlar

- Veri seti günde onlarca kayıt büyür; bunların çoğu tek kaynaklı ve doğrulanmamıştır, ve sitede
  öyle görünür.
- Hatalı özet olasılığı gerçektir. Her kayıt kaynağına bağlıdır ve bir düzeltme ya da mezar taşı
  0007'deki düzeltme yoluyla yayılır.
- Doğrulama artık ayrı bir iştir: `otomatik` etiketli kayıtlar üzerinde bağımsız ikinci kaynak,
  arşiv bağlantısı ve konum eklenerek `partially_verified`'a taşınır.
- GitHub Models ücretsiz katmanı günlük istek sınırlıdır; model erişilemezse o gün kayıt yazılmaz,
  sonraki çalıştırma yeniden dener.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Her kayıt için insan onayı (0007 olduğu gibi) | Günde 40+ aday, tek bakımcı: kayıt birikmiyor. |
| Adayları kayıt yerine yalnızca "bülten" olarak yayımlamak | Bültenler veri setinin parçası değil; haritada ve panoda görünmez. |
| Kaynağın başlığını ve alıntısını olduğu gibi kopyalamak | Üçüncü taraf metni CC BY 4.0 veri setine girer ([0009](0009-licensing.md)); Türkçe metin olmaz. |
| Otomatik yoldan Türk kuvvetleriyle ilgili adayları da geçirmek | Kırmızı çizgi; bir insan olmadan yayımlanamaz. |
