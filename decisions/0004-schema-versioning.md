# 0004 · Şema sürümleme

> **EN:** Records are validated against JSON Schema 2020-12 with URN `$id`s (e.g. `urn:gt:schema:event:1`); each record declares `schema: event/1`; additive changes need no bump, breaking changes create v2 with a migration in the same PR; data releases use CalVer (e.g. `v2026.09.0`).

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Veri modeli zamanla gelişecek. Hem katkıcılar (`gt.py validate`) hem de `platform` kodu ve dış kullanıcılar, bir kaydın hangi yapıya uyduğunu kesin olarak bilmeli. Şema değişikliklerinin mevcut veriyi ve kodu habersiz bozmaması gerekir.

## Karar

1. Şemalar **JSON Schema 2020-12** ile yazılır ve `datasets/schemas/` altında yaşar ([0001](0001-repository-boundaries.md)).
2. Her şemanın `$id` değeri, konumdan bağımsız bir **URN**'dir: `urn:gt:schema:<kind>:<major>`, ör. `urn:gt:schema:event:1`. Böylece şemalar bir alan adına veya URL'ye bağlı değildir.
3. Her kayıt uyduğu şemayı ilk alanda bildirir: `schema: event/1`, `schema: actor/1`, `schema: tombstone/1` …
4. **Geriye uyumlu (eklemeli) değişiklikler** — isteğe bağlı yeni alan, sözlüğe yeni kod, açıklama iyileştirmesi — **sürüm artırmaz**.
5. **Kırıcı değişiklikler** — alan silme/yeniden adlandırma, zorunlu yeni alan, anlam değişikliği, tip değişikliği — yeni ana sürüm oluşturur (`event/2`, `urn:gt:schema:event:2`). **Aynı PR'da**:
   - yeni şema,
   - tüm mevcut kayıtları dönüştüren geçiş betiği ve dönüştürülmüş kayıtlar,
   - `gt.py` güncellemesi,
   - bir ADR (kırıcı değişiklik temel değişikliktir).
   Geçişten sonra depoda eski sürümde kayıt kalmaz; eski şema belgeleme için saklanır.
6. **Veri sürümleri CalVer** ile etiketlenir: `vYYYY.MM.N` (ör. `v2026.09.0`, aynı ay içindeki sonraki sürüm `v2026.09.1`). Sürüm notları, varsa şema ana sürüm değişikliklerini açıkça belirtir.
7. `platform` belirli bir veri sürüm etiketini sabitler; yeni ana şema sürümüne geçiş bilinçli bir PR'dır.

## Sonuçlar

- Doğrulama deterministiktir; aynı kayıt, aynı şemayla her yerde aynı sonucu verir.
- Kırıcı değişiklikler pahalıdır (tüm veriyi dönüştürmek gerekir); bu, onları nadir tutmaya teşvik eder.
- Dış kullanıcılar sürüm etiketine göre yükseltme yapabilir.
- CalVer, verinin ne zaman yayımlandığını doğrudan gösterir; şema uyumluluğu ayrıca `schema` alanıyla izlenir.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Şemasız YAML | Tutarsızlık; otomatik denetim imkânsız. |
| `$id` olarak https URL | Alan adına bağımlılık; alan adı kaybı şemaları "kırar". |
| Veri için SemVer | Veri sürümlerinde "kırıcı" kavramı şema düzeyindedir; tarih bilgisi daha anlamlı. |
| Eski ve yeni sürümlerin depoda birlikte yaşaması | Tüketiciler iki yapıyı birden desteklemek zorunda kalır. |
