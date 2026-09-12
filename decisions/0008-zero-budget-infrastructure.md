# 0008 · Sıfır bütçe altyapı

> **EN:** We run only on free tiers with no payment method on any account, so limits are hard caps: GitHub Actions (Worker-triggered `workflow_dispatch`, not `schedule:`), Cloudflare Workers/Queues/D1 (D1 is the operational DB), optional GitHub Models, free social APIs; X is manual; R2 and Supabase are avoided; usage is tracked in a ledger.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Topluluğun bütçesi yoktur ve bağış kabul etmez ([03](../tr/03-legal-ethics.md)). Ücretli bir hizmete bağımlılık, bir kişinin kredi kartına bağımlılık demektir: Hem sürdürülemez hem de o kişinin kimliğini açığa çıkarma riski taşır. Ücretsiz katmanların sınırları ve koşulları değişebilir; tasarım buna dayanıklı olmalıdır.

## Karar

**Hiçbir hesaba ödeme yöntemi tanımlanmaz.** Böylece ücretsiz katman sınırları "sürpriz fatura" değil, **kesin sınır** olur: Sınır aşılırsa hizmet durur, para çıkmaz.

| Hizmet | Ücretsiz koşullar (bu tarih itibarıyla) | Karar |
|---|---|---|
| GitHub Actions | Açık depolar için ücretsiz ve süre sınırsız. **Zamanlanmış (`schedule:`) iş akışları, depoda 60 gün etkinlik olmazsa otomatik devre dışı kalır.** | Kullanılır. Toplayıcılar `schedule:` yerine, bir Cloudflare Worker'ın cron tetikleyicisinin çağırdığı `workflow_dispatch` ile çalışır. |
| GitHub Models | Ücretsiz, düşük günlük istek sınırları (modele göre yaklaşık 50–150 istek/gün); prototipleme amaçlı. | Yalnızca **isteğe bağlı** adımlarda. Her LLM adımı devre dışı bırakılabilir; sistem LLM olmadan da çalışır. |
| Cloudflare Workers | 100.000 istek/gün, istek başına 10 ms CPU, 3 cron tetikleyici. | Kullanılır: API, inceleme botu, zamanlayıcı. |
| Cloudflare Queues | Ücretsiz planda günde 10.000 işlem (mesaj başına yazma+okuma+silme ≈ 3 işlem → yaklaşık 3.300 mesaj/gün). | Kullanılır; mesaj hacmi bu sınıra göre tasarlanır. |
| Cloudflare D1 | Günde 5 milyon satır okuma / 100.000 satır yazma, veritabanı başına 500 MB, 7 günlük Time Travel (zamanda geri dönüş). | **Operasyonel veritabanı olarak SEÇİLDİ** (ham sinyaller, triyaj durumu, yayın kuyruğu). Kalıcı veri git'tedir ([0002](0002-git-as-source-of-truth.md)). |
| Cloudflare R2 | 10 GB ücretsiz, ama **ödeme yöntemi tanımlanmasını gerektirir.** | **Kaçınılır**, gerçekten ihtiyaç doğana kadar. |
| Supabase | Ücretsiz projeler 7 gün etkinlik olmazsa duraklatılır; ücretsiz planda yedek yok. | Çekirdek altyapıda **kullanılmaz**. |
| X (Twitter) API | Şubat 2026'dan beri ücretsiz katman yok (paylaşım başına yaklaşık 0,015 USD). | Otomatik paylaşım **yok**; X'e paylaşım elle yapılır. |
| Bluesky, Telegram, Mastodon | API'ler ücretsiz. | Otomatik yayın kanalları. |
| Zenodo | Ücretsiz DOI ve arşivleme. | Veri sürümleri Zenodo'ya aynalanır (atıf ve dayanıklılık). |

### Kullanım defteri

- Her hizmetin kullanımı (istek, satır, dakika) ve sınıra uzaklığı bir **kullanım defterinde** izlenir; defter `platform` tarafından üretilir ve bakımcılara görünür.
- Bir hizmet sınırının %80'ine yaklaşınca uyarı üretilir; toplayıcıların sıklığı düşürülür.
- Hizmet koşulları değişirse bu ADR yeni bir ADR ile güncellenir.

### Hesap sahipliği

- Hizmet hesapları kişisel değil, topluluk adına açılmış hesaplardır; en az **iki bakımcı** erişimine sahiptir ([0011](0011-threat-model.md)).
- Hiçbir hesap bir kişinin gerçek kimliğine veya ödeme bilgisine bağlanmaz.

## Sonuçlar

- Maliyet sıfırdır ve sürpriz fatura riski yoktur.
- Sınırlar gerçekten sınırdır: Yoğun dönemlerde toplama yavaşlayabilir; bu kabul edilir.
- Sağlayıcı koşulları değişirse (ör. bir ücretsiz katmanın kaldırılması) mimari buna uyarlanabilir olmalıdır: Kalıcı veri git'te olduğu için en kötü durumda yalnızca otomasyon durur.
- LLM'e bağımlılık yoktur; bu, hem maliyeti hem de istem enjeksiyonu riskini sınırlar.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Ücretli VPS | Bütçe ve kimlik (ödeme) sorunu. |
| `schedule:` ile GitHub Actions | 60 gün etkinliksizlikte devre dışı kalma riski. |
| Supabase/Postgres operasyonel veritabanı | Duraklatma ve yedek yokluğu. |
| X API ücretli katman | Bütçe yok. |
