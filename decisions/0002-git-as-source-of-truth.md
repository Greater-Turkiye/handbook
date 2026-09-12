# 0002 · Tek doğruluk kaynağı olarak git

> **EN:** Verified records live in git as one YAML file per record; raw collected signals never enter git; all exports (JSON, CSV, GeoJSON, etc.) are built by CI from the files.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Yayımladığımız verinin kim tarafından, ne zaman, hangi gerekçeyle değiştirildiğinin şeffaf ve kalıcı biçimde izlenebilmesi gerekir. Bütçemiz yok; barındırılan bir veritabanının kaybı, kapanması veya ücretli hâle gelmesi projeyi bitirmemeli. Aynı zamanda otomatik toplayıcılar çok miktarda ham, doğrulanmamış ve potansiyel olarak hassas sinyal üretecek.

## Karar

1. **Doğrulama sürecinden geçmiş kayıtların tek doğruluk kaynağı `datasets` git deposudur.**
2. **Kayıt başına bir YAML dosyası.** Yol, ID'den türetilir: `data/<kind>/<yyyy>/<mm>/<id>.yaml` ([0003](0003-identifiers.md)).
3. Her değişiklik bir **PR** ile yapılır ve herkese açık incelemeden geçer. Git geçmişi, denetim kaydıdır.
4. **Ham sinyaller git'e girmez.** Toplayıcıların ürettiği ham öğeler (haber akışları, kanal gönderileri, önizlemeler) yalnızca operasyonel veritabanında (Cloudflare D1, [0008](0008-zero-budget-infrastructure.md)) ve sınırlı süre tutulur; insan triyajından geçip kayda dönüşenler PR ile git'e gelir.
5. **Dışa aktarımlar CI tarafından üretilir** (`tools/gt.py build`): JSON, CSV, GeoJSON gibi biçimler sürüm etiketlerinde yapı çıktısı olarak yayımlanır, depoya commit edilmez.
6. YAML biçimi sabittir (anahtar sırası, girinti, tırnaklama) ve `gt.py` ile denetlenir; böylece farklar (diff) okunaklı kalır.

## Sonuçlar

- Herkes depoyu klonlayarak verinin tamamına ve geçmişine sahip olur; tek bir sağlayıcıya bağımlılık yoktur.
- İnceleme, GitHub'ın PR araçlarıyla ücretsiz yapılır.
- Kayıt başına dosya, birleştirme çakışmalarını azaltır; binlerce dosya sonrasında bile git ölçeklenir. Çok büyük hacimlerde (yüz binlerce kayıt) yeniden değerlendirme gerekebilir.
- Geçmişten silmek zordur; bu, kişisel veri ve gizli materyalin **hiç girmemesi** gerektiği anlamına gelir ([0010](0010-content-safety-gates.md)).
- Operasyonel veritabanı kaybolursa yalnızca doğrulanmamış ham sinyaller kaybolur; yayımlanmış veri etkilenmez.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Barındırılan veritabanı ana kaynak | Sağlayıcı riski, maliyet riski, şeffaf inceleme yok. |
| Tek büyük JSON/CSV dosyası | Sürekli çakışma; okunaksız farklar; satır bazlı inceleme zor. |
| Ham sinyallerin de git'e konması | Hacim, kişisel veri riski, doğrulanmamış içeriğin kalıcılaşması. |
