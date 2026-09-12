# 0001 · Depo sınırları

> **EN:** Five repositories (`.github`, `handbook`, `datasets`, `platform`, `internal`); data and code are separated, all code lives in one monorepo, schemas live with the data, and `platform` pins `datasets` release tags.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Topluluk; kurallar, doğrulanmış veri, otomasyon kodu ve bakımcılara özel bilgiler üretir. Bunların erişim ihtiyacı (herkese açık / özel), inceleme sorumluları, lisansları ve değişim hızları farklıdır. Az sayıda gönüllüyle çok sayıda depoyu yönetmek ise zordur.

## Karar

Organizasyon `Greater-Turkiye` altında beş depo:

| Depo | Görünürlük | İçerik | Lisans |
|---|---|---|---|
| `.github` | Açık | Organizasyon profili, sorun/PR şablonları, davranış kuralları, `SECURITY.md` | CC BY 4.0 |
| `handbook` | Açık | Bu el kitabı ve ADR'ler | CC BY 4.0 |
| `datasets` | Açık | Doğrulanmış kayıtlar (kayıt başına bir YAML), JSON Şemaları, `vocab/`, `policy.yaml`, `tools/gt.py` | Veri CC BY 4.0, araç kodu MIT |
| `platform` | Açık | Tüm kod (monorepo): toplayıcılar, yayıncılar, Cloudflare Workers API ve inceleme botu, web | MIT |
| `internal` | **Özel** | Yalnızca bakımcılar: operasyonel notlar, olay müdahale kayıtları, hesap kurtarma bilgilerinin konumu | — |

İlkeler:
1. **Veri ve kod ayrıdır.** Veri inceleyicileri kod bilmek zorunda değildir; kod değişiklikleri veri geçmişini kirletmez.
2. **Tüm kod tek bir monorepodadır** (`platform`). Paylaşılan tipler, tek CI, tek sürüm akışı.
3. **Şemalar verinin yanında yaşar** (`datasets/schemas`). Bir şema değişikliği ve veri geçişi aynı PR'da yapılır ([0004](0004-schema-versioning.md)).
4. **`platform`, `datasets`'in sürüm etiketlerini sabitler** (ör. `v2026.09.0`). Şema değişiklikleri kodu habersiz bozamaz; yükseltme bilinçli bir PR'dır.
5. `datasets/tools/gt.py`, katkıcıların kayıt oluşturup doğrulaması için gereken **tek** araçtır ve bağımlılıkları asgaridir; `platform` kodu buna bağımlı olmaz.

## Sonuçlar

- Her deponun CODEOWNERS ve dal koruması kendi riskine göre ayarlanır (`datasets` en sıkı).
- Katkıcılar yalnızca ilgilendikleri depoyu fork'lar.
- `datasets` ile `platform` arasında şema uyumu, etiket sabitleme ile yönetilir; bu, yükseltme işi gerektirir.
- Özel depo (`internal`) asgaride tutulur; topluluğu ilgilendiren kararlar oraya değil buraya yazılır.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Tek depo (her şey birlikte) | Veri incelemesi ve kod incelemesi karışır; lisans ayrımı zorlaşır; veri geçmişi gürültülenir. |
| Her bileşen için ayrı kod deposu | Az gönüllüyle bakım yükü; sürüm uyumsuzlukları. |
| Şemaların `platform`'da olması | Veri doğrulaması koda bağımlı olur; şema ve veri geçişi ayrı PR'lara bölünür. |
