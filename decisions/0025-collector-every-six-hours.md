# 0025 · Toplayıcı altı saatte bir çalışır

> **EN:** Amends [0016](0016-collector-schedule-until-worker.md), which ran the collectors once a day. Since [0023](0023-automatic-unverified-records.md) candidates become public records automatically, so a once-a-day run makes the site up to a day late for no reason. The collector now runs every six hours (05:23, 11:23, 17:23, 23:23 UTC) and the automatic-record job forty minutes after each run. The review queue still gets one issue per day: later runs on the same day comment on it. Everything else in 0016 stands.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-24
- **Önerenler:** @nukIeer
- **İlgili:** [0016](0016-collector-schedule-until-worker.md) (sıklığı değiştirir), [0023](0023-automatic-unverified-records.md), [0024](0024-automatic-records-without-a-language-model.md)

## Bağlam

0016 toplayıcıyı günde bir kez çalıştırdı; kuyruğu bir insan okuyacağı için daha sık çalışmanın
anlamı yoktu. 0023'ten beri ilgi süzgecini geçen adaylar kimse okumadan kayıt olarak yayımlanıyor.
Günde bir çalışma, 05:30'da yayımlanan bir haberin ertesi sabaha kadar sitede görünmemesi demek.

## Karar

- `collect.yml` 05:23, 11:23, 17:23 ve 23:23 UTC'de çalışır.
- `auto-records.yml` her toplayıcı çalışmasından kırk dakika sonra çalışır (06:03, 12:03, 18:03, 00:03 UTC).
- İnceleme kuyruğu yine günde tek issue'dur; aynı günün sonraki çalışmaları ona yorum ekler.
- Akışların `cadence_minutes` değerleri en az 60 dakikadır; altı saatlik aralık hepsine uyar.
  Toplayıcı koşullu GET kullanır, değişmeyen akış yeniden indirilmez.

## Sonuçlar

- Olaylar sitede en geç yaklaşık yedi saat içinde görünür.
- GitHub Actions dakikaları açık depoda ücretsizdir; günlük dört kısa çalışma bütçeyi değiştirmez ([0008](0008-zero-budget-infrastructure.md)).
- Sağlık denetimi toplayıcıyı bundan sonra altı saatlik ritme göre yoklar.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Günde bir kez kalmak | Otomatik kayıtla birlikte gereksiz bir gecikme. |
| Saatte bir | Akışların çoğu günde birkaç öğe yayımlar; kazanç küçük, kuyruk ve yük gereksiz büyür. |
