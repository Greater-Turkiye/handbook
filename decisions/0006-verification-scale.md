# 0006 · Doğrulama ölçeği

> **EN:** We use the Admiralty scale — source reliability A–F on the source registry and information credibility 1–6 on each record — plus `assessment.status`; `verified` has strict machine-checked rules; contested characterisations are only ever recorded as attributed `claims[]`.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Açık kaynak bilgisi hızlı, taraflı ve sıklıkla yanlıştır. Kullanıcılar bir kaydın ne kadar güvenilir olduğunu bilmeli; inceleyiciler tutarlı kararlar vermeli; bu kararların bir kısmı makinece denetlenebilmeli. Ayrıca bölgemizdeki pek çok olay, tarafların nitelendirmesinde (ihlal, saldırı, işgal…) ihtilaflıdır.

## Karar

1. **Kaynak güvenilirliği (A–F)** kaynak sicilinde (`src_` kaydı) tutulur. Yeni kaynaklar `F` ile başlar.
2. **Bilgi inandırıcılığı (1–6)** her kayıtta `assessment.credibility` alanında tutulur. Yeni kayıtlar `6` ile başlar.
3. **Durum** `assessment.status`: `unverified` | `partially_verified` | `verified` | `disputed` | `false`.
4. **`verified` kuralları** (CI denetler):
   - `credibility` ≤ 2,
   - İngilizce metin mevcut,
   - her kaynağın arşiv bağlantısı var,
   - **iki bağımsız kaynak** VEYA **geolokasyon / kronolokasyon / uydu görüntüsü** ile doğrulama (yöntem kayıtta),
   - kısıtlı kaynak tek dayanak değil.
   CI "bağımsızlığı" anlamsal olarak denetleyemez; bu, inceleyicinin sorumluluğudur. CI yalnızca en az iki farklı kaynak ID'si veya bir doğrulama yöntemi bulunduğunu kontrol eder.
5. **`false` kayıtlar silinmez.**
6. **İddialar atfedilir.** Tartışmalı nitelendirmeler ("hava sahası ihlali", "terör saldırısı", "işgal", "misilleme"…) proje sesiyle **asla** yazılmaz; `claims[]` içinde, iddiayı yapan aktöre ve kaynağa bağlanarak kaydedilir. Kayıt başlığı ve özeti bu kurala uyar ([08](../tr/08-style-guide.md)).
7. Analiz metinlerinde olasılık dili ICD 203 tarzı 7 düzeyli ölçekle sınırlıdır ([05](../tr/05-verification.md)).

## Sonuçlar

- Kullanıcılar kayıtları doğrulama düzeyine göre süzebilir.
- Uluslararası OSINT ve analiz topluluğunun bildiği bir ölçek kullanıldığı için veri başka veri setleriyle karşılaştırılabilir.
- `verified` eşiği yüksektir; kayıtların çoğunun uzun süre `unverified` veya `partially_verified` kalması beklenir ve kabul edilir.
- Kaynak ve bilgi ayrımı, "resmî kaynak = doğru" yanılgısını engeller.
- `claims[]` yapısı, projeyi tarafların nitelendirme savaşının dışında tutar; aynı zamanda tarafların ne dediğini analiz edilebilir kılar.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Tek boyutlu güven puanı (0–100) | Kaynak ve bilgi karışır; sahte kesinlik. |
| Yalnızca "doğrulandı / doğrulanmadı" | İhtilaflı ve yanlış durumlar ifade edilemez. |
| Projenin nitelendirme yapması | Tarafsızlığı ve güvenilirliği yok eder; hukuki risk. |
| `false` kayıtları silmek | Aynı dezenformasyon tekrar ettiğinde referans kalmaz. |
