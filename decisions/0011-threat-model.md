# 0011 · Tehdit modeli

> **EN:** Main threats and mitigations: data poisoning and sock-puppet reviewers (vetting, independent-source rule, double review for first-timers); mass reporting/deplatforming (ToS-aligned policy, Zenodo and clone mirrors); contributor de-anonymisation (OPSEC); prompt injection (LLM outputs are schema-checked JSON only, no tools, cannot publish); account takeover (2FA, second owner, recovery codes).

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Bölgesel güvenlik konularında açık veri üreten bir topluluk; devlet destekli bilgi operasyonlarının, trol ağlarının, fırsatçı saldırganların ve projeyi itibarsızlaştırmak isteyenlerin hedefi olabilir. Bütçemiz ve tüzel kişiliğimiz yok; savunmamız süreç tasarımına dayanmalıdır.

## Karar

Aşağıdaki tehditler ve karşı önlemler kabul edilmiştir. Ayrıntılı olay müdahale notları `internal` deposunda tutulur.

| # | Tehdit | Olası etki | Karşı önlemler |
|---|---|---|---|
| 1 | **Kasıtlı veri zehirleme** (uydurma olay, sahte kaynak, geçmişe uygun görünen sahte arşiv) | Veri setinin yanlış bilgi yaymak için kullanılması; itibar kaybı | Bağımsız kaynak kuralı ve `verified` eşiği ([0006](0006-verification-scale.md)); her kaynağın arşivi; **ilk katkıların çift incelemesi**; tespit edilen zehirlemede katkıcının tüm kayıtlarının yeniden incelenmesi ve kalıcı yasak. |
| 2 | **Kukla inceleyiciler** (sahte hesapların güven kazanıp inceleyici olması, birbirini onaylaması) | Kapıların içeriden aşılması | İnceleyicilik için ~3 ay + **2 kefil** + OPSEC brifingi ([10](../tr/10-contributing.md)); yazar kendi PR'ını onaylayamaz; inceleyici sayısı yeterince artınca 2 onay ([0012](0012-governance.md)); Türk kuvvetleri kapısında ayrıca bakımcı onayı; olağandışı onay örüntülerinin bakımcılarca izlenmesi. |
| 3 | **Toplu şikâyet / platformdan atılma** (GitHub, Telegram, Bluesky hesaplarının raporlanıp kapatılması; erişim engeli) | Yayın kanallarının ve deponun kaybı | İçerik politikasının platform kullanım koşullarıyla uyumlu tutulması (kırmızı çizgiler bunu zaten sağlar); veri sürümlerinin **Zenodo**'ya aynalanması; katkıcıların ve üçüncü tarafların **klonları**; kalıcı veri git'te olduğu için yeniden kurulum mümkün. |
| 4 | **Katkıcıların kimliğinin açığa çıkarılması** (commit meta verisi, e-posta, saat dilimi, yazım üslubu, platformlardan yasal talep) | Katkıcılara taciz, tehdit, hukuki baskı | [OPSEC](../tr/04-opsec.md) rehberi: noreply e-posta, UTC commit, iş/devlet cihazı yasağı, meta veri temizliği, hedeflerle etkileşim yasağı; takma adın anonimlik olmadığının açıkça söylenmesi; kırmızı çizgilere uyulması (saklanacak bir şey olmaması). |
| 5 | **İstem enjeksiyonu (prompt injection)** — toplanan içeriğe gömülü talimatların LLM adımlarını yönlendirmesi | Yanlış sınıflandırma, zararlı içeriğin öne çıkarılması, gizli bilgi sızdırma girişimi | LLM adımları **isteğe bağlıdır** ([0008](0008-zero-budget-infrastructure.md)); LLM çıktısı yalnızca **şemayla denetlenen JSON**'dur; LLM'e **araç (tool) erişimi verilmez**; LLM hiçbir şeyi **yayımlayamaz**, PR birleştiremez, mesaj gönderemez; tüm çıktılar insan triyajından geçer ([0007](0007-human-in-the-loop-publishing.md)); sırlar LLM bağlamına konmaz. |
| 6 | **Hesap ele geçirme** (bakımcı veya bot hesapları) | Deponun silinmesi, sahte yayın, gizli bilgilere erişim | Tüm üyelerde zorunlu **2FA** (tercihen passkey/TOTP); organizasyonda ve her hizmet hesabında **en az iki sahip**; **kurtarma kodlarının çevrimdışı saklanması**; bot belirteçlerinin asgari yetkili ve süreli olması; dal korumasının yöneticileri de kapsaması; **acil durdurma** ([0007](0007-human-in-the-loop-publishing.md)); şüphede belirteçlerin derhal yenilenmesi. |
| 7 | **Kötü amaçlı dosya ve bağlantılar** (katkıcılara "sızıntı" yemi) | Cihaz ele geçirme, kimlik açığa çıkma | OPSEC rehberinde sanal makine/sandbox kuralı; gizli materyalin hiç açılmaması ([02](../tr/02-red-lines.md)); PR'larda ikili dosya yasağı. |
| 8 | **Tedarik zinciri** (kötü amaçlı bağımlılık, ele geçirilmiş GitHub Action) | CI üzerinden sır çalma, depo değiştirme | `platform` ve `datasets` iş akışlarında Action'ların commit SHA ile sabitlenmesi; asgari `GITHUB_TOKEN` yetkileri; fork PR'larında sırların kullanılmaması; bağımlılıkların asgaride tutulması. |

## Sonuçlar

- Güven, zamanla ve kefillikle kazanılır; bu, yeni katkıcılar için daha yavaş bir yol demektir.
- Süreçler (çift inceleme, bekleme süreleri, onay etiketleri) hızı düşürür; bu bilinçli bir tercihtir.
- Tehdit modeli yılda en az bir kez veya önemli bir olaydan sonra yeniden gözden geçirilir; değişiklikler yeni ADR ile yapılır.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Katkıcılardan kimlik doğrulaması istemek | Takma adla katkı modelini ortadan kaldırır; toplanan kimlik verisi başlı başına bir risk olur. |
| Tamamen kapalı (davetli) topluluk | Şeffaflık ve açık veri misyonuyla çelişir; yine de içeriden tehdit riski kalır. |
| LLM'e araç erişimi verip otomasyonu artırmak | İstem enjeksiyonu riskini kabul edilemez düzeye çıkarır. |
