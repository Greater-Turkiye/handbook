# 0016 · Toplayıcılar: Worker gelene kadar GitHub Actions `schedule:`

> **EN:** Amends ADR 0008: until a Cloudflare account exists, collectors run on a GitHub Actions `schedule:` instead of a `workflow_dispatch` triggered by a Worker cron. The 60-day inactivity risk is mitigated by the ledger commit each queuing run makes, and by re-arming with a manual dispatch; when the scheduler Worker exists, the trigger moves back and this ADR is superseded.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-16

## Bağlam

[0008](0008-zero-budget-infrastructure.md), toplayıcıların `schedule:` ile değil, bir Cloudflare Worker'ın cron tetikleyicisinin çağırdığı `workflow_dispatch` ile çalışmasını kararlaştırmıştı. Gerekçe, zamanlanmış iş akışlarının depoda 60 gün etkinlik olmazsa GitHub tarafından devre dışı bırakılmasıydı.

Bugün Cloudflare hesabı yok ve kurulması bakımcının yapması gereken manuel adımlara bağlı. Bu yüzden toplayıcı hattı hiç çalışmıyordu; veri yalnızca elle giriliyordu. Çalışmayan bir hat, 60 gün riskinden daha büyük bir sorundur.

## Karar

1. Toplayıcılar, `platform` deposunda bir GitHub Actions `schedule:` tetikleyicisiyle günde bir kez çalışır; `workflow_dispatch` da açık kalır.
2. 60 gün riski şöyle yönetilir:
   - Kuyruğa madde giren her koşu, tekrar eleme defterini (`collectors/state/`) `collector-state` dalına yazar; bu, depoda etkinlik sayılır ve cron'u diri tutar.
   - Hiç madde girmeyen koşular bir şey yazmaz. Üst üste 60 sessiz gün olursa GitHub bakımcılara e-posta gönderir ve iş akışı elle bir kez tetiklenerek yeniden kurulur.
3. Scheduler Worker devreye girdiğinde tetikleyici `workflow_dispatch`'e döner ve bu ADR yerine yeni bir karar yazılır.
4. Bu karar yalnızca tetikleyiciyi değiştirir. 0008'in geri kalanı — ödeme yöntemi yok, ücretsiz sınırlar tavan, D1 operasyonel veritabanı, X elle — aynen geçerlidir.

## Sonuçlar

- Toplayıcı hattı, hiçbir hesap veya gizli anahtar gerekmeden çalışır.
- Cron'un devre dışı kalma ihtimali kalır; bu, bilinçli olarak kabul edilmiş küçük bir bakım yüküdür.
- `platform/ARCHITECTURE.md` bu tetikleyiciyi anlatacak şekilde güncellenir.

## Alternatifler

- **Worker kurulana kadar beklemek:** Hattın çalışmamaya devam etmesi demekti; reddedildi.
- **Üçüncü taraf bir cron servisi:** Yeni hesap ve yeni bağımlılık; sıfır bütçe ve saldırı yüzeyi gerekçesiyle reddedildi.
- **Depoyu yapay etkinlikle canlı tutmak (keepalive commit):** Gürültülü geçmiş üretir; defter yazımı zaten doğal bir etkinlik sağlıyor.
