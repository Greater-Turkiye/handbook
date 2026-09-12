# 0005 · Kontrollü sözlükler

> **EN:** Categorical values come from vocab files in `datasets/vocab/`; codes are never deleted (deprecated + `replaced_by`); event types are `domain.type`; regions are editorial watch areas; countries are ISO 3166-1 alpha-3 plus the project code `XNC`.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Serbest metin kategoriler ("tatbikat", "Tatbikat", "askeri tatbikat", "exercise") analiz edilemez. İki dilli çalışıyoruz; etiketlerin tek yerden yönetilmesi gerekir. Kodlar zamanla değişecek, ama eski kayıtlar ve dış kullanıcılar bozulmamalı.

## Karar

1. Tüm kategorik değerler `datasets/vocab/` altındaki YAML dosyalarından gelir (ör. olay türleri, aktör rolleri, bölgeler, ülkeler, konum hassasiyeti, kaynak türleri, kullanım koşulları). Şemalar bu dosyalara göre doğrular.
2. Her kodun **Türkçe ve İngilizce etiketi** ve kısa tanımı vardır.
3. **Kodlar asla silinmez.** Kullanımdan kalkan kod `deprecated: true` ve varsa `replaced_by: <yeni-kod>` ile işaretlenir. CI, yeni kayıtlarda kullanımdan kalkmış kodu reddeder; eski kayıtlar bir geçiş PR'ıyla yeni koda taşınır.
4. Kodlar küçük harfli ASCII'dir; anlamı değişmez. Anlam değişecekse yeni kod açılır.
5. **Olay türleri** iki düzeylidir: `<alan>.<tür>`, ör. `exercise.military`, `maritime.incident`, `procurement.contract`, `air.intercept` (örnekler gösterim amaçlıdır; kanonik liste sözlük dosyasındadır). Alan düzeyi kaba analiz, tür düzeyi ayrıntı sağlar.
6. **Bölgeler** egemenlik veya coğrafya tanımı değil, **editoryal izleme alanlarıdır** ([01](../tr/01-mission-scope.md)). Bir kayıt birden fazla bölgeye ait olabilir; bölgelerin sınırı çizilmez.
7. **Ülkeler** ISO 3166-1 alpha-3 kodlarıdır, ek olarak proje kodu **`XNC`** (KKTC / TRNC). `CYP` etiketi "GKRY / Greek Cypriot Administration of Southern Cyprus" olarak, Türkiye'nin resmî kullanımına göre verilir. `countries` alanı olaya aktörleri dahil olan devletleri gösterir, yerin egemenliğini değil ([07](../tr/07-geo-time-disputed.md)).
8. Yeni kod eklemek eklemeli bir değişikliktir (şema sürümü artmaz, [0004](0004-schema-versioning.md)); bir inceleyici onayıyla yapılır. Kod anlamını değiştirmek veya bölge/ülke listesinde politik anlam taşıyan değişiklik bakımcı onayı gerektirir.

## Sonuçlar

- Analiz ve filtreleme güvenilir olur; çeviriler tek yerden yönetilir.
- Sözlük dosyaları büyür (kullanımdan kalkmış kodlar kalır); bu, bağlantıların kırılmamasının bedelidir.
- Etiketlerdeki terminoloji (KKTC, GKRY vb.) Türkiye'nin resmî kullanımını izler; bu, veride egemenlik iddiası değil yayın dili tercihidir.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Serbest metin etiketler | Analiz edilemez, çeviri tutarsız. |
| Tek düzeyli uzun olay türü listesi | Kaba analiz zorlaşır; liste yönetilemez hâle gelir. |
| Kodların silinmesi | Eski kayıtlar ve dış kullanıcılar bozulur. |
| Bölgeleri çokgenlerle tanımlamak | Sınır çizmek politik bir iddia olur; bakım yükü. |
