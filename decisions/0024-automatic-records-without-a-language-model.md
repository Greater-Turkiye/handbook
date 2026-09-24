# 0024 · Dil modeli olmadan otomatik kayıt

> **EN:** Replaces the language-model step of [0023](0023-automatic-unverified-records.md), which could not run: GitHub Models answered every request, from a runner and from a maintainer's machine, with a plain-text `OK` and no model output. Automatic records are now made without a model. The English title is the source's own headline; the Turkish title is a machine translation of it by MyMemory's free, account-less API, and `i18n.machine` says so. Rules on the headline pick the event type and drop analysis, opinion and newsletters; repeat reports of one occurrence still fold into one record. There is no summary, because the only text available is the source's excerpt and copying it is what [0009](0009-licensing.md) rules out. Everything else in 0023 — unverified status, the note, the `otomatik` tag, the red-line skips, validation, the kill switch and the `auto-data` branch — is unchanged.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-24
- **Önerenler:** @nukIeer
- **İlgili:** [0009](0009-licensing.md), [0023](0023-automatic-unverified-records.md) (dil modeli adımının yerine geçer)

## Bağlam

0023 başlık ve özeti, olay/analiz ayrımını, türü ve bölgeyi GitHub Models'a bırakmıştı. İlk canlı
çalıştırmada uç nokta her isteğe `200 text/plain` ve gövdesinde yalnızca `OK` döndü; katalog adresi de
aynı cevabı verdi, runner'dan da bakımcının makinesinden de. Hiçbir kayıt yazılamadı. Model yoksa
otomatik kayıt da yok demek, 0023'ün amacını boşa çıkarırdı.

## Karar

| iş | 0023 (model) | şimdi |
|---|---|---|
| İngilizce başlık | modelin yazdığı | **kaynağın kendi başlığı** (`i18n.source: en`) |
| Türkçe başlık | modelin yazdığı | **MyMemory makine çevirisi** (`i18n.machine: [tr]`) |
| Rusça, Arapça başlık | modelin yazdığı | iki dile de makine çevirisi (`machine: [tr, en]`) |
| özet | modelin yazdığı | **yok** — kaynağın alıntısı kopyalanmaz (0009) |
| olay mı, analiz mi | model | başlığın biçimi (soru, podcast, bülten, "quoted"…) ve akış (Atlantic Council akışı tümüyle analiz sayılır) |
| tür | model | başlıktaki eyleme bakan kurallar; toplayıcının konusu yedek |
| bölge | model | toplayıcının bölgesi |
| tekrar haberler | model | aynı gün, aynı bölge, başlık kelimelerinin çoğu ortak |

Çeviri servisi hesap istemez; günlük karakter kotası vardır. Kota dolunca iş o çalıştırmada durur,
kalan adaylar sonraki çalıştırmada çevrilir. Yanlış dilde bir alan yazılmaz: çeviri yoksa kayıt da yok.
Servise yalnızca haber başlıkları gider; kişisel veri gitmez.

## Sonuçlar

- Kayıtlar sitede kısa görünür: başlık, tür, bölge, tarih, kaynak bağlantısı ve "otomatik" notu.
  Özeti bir insan doğrularken yazar.
- Tür ve bölge hataları modelden daha sık olacaktır; kayıt bunu notunda söyler ("anahtar kelimeyle
  bulundu") ve doğrulanmamıştır.
- Bir dil modeli ileride erişilebilir olursa, onu geri getirmek bu ADR'nin yerine geçen yeni bir karardır.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Model gelene kadar beklemek | Kayıt birikmez; 0023'ün nedeni tam da buydu. |
| Türkçe alana İngilizce başlığı yazmak | Alan yanlış dil taşır; veri yalan söyler. |
| Kaynağın alıntısını özet diye koymak | Üçüncü taraf metni CC BY 4.0 veri setine girer (0009). |
| Ücretli ya da anahtarlı bir çeviri/LLM servisi | Sıfır bütçe (0008) ve sahibinden kimlik bilgisi istemek gerekir. |
