# 0009 · Lisanslama

> **EN:** Data and content are CC BY 4.0, code is MIT; inbound = outbound (opening a PR means agreeing); no DCO, to protect pseudonymity; third-party content is never copied and each source's terms are respected.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Verinin araştırmacılar, gazeteciler ve diğer projeler tarafından serbestçe kullanılmasını istiyoruz; ama katkının kaynağının belirtilmesi de önemli. Katkıcıların büyük kısmı takma adla çalışacak; gerçek ad isteyen süreçler (DCO, CLA) bu modelle çelişir. Ayrıca kaynaklarımızın önemli bir kısmı telifli veya kısıtlı lisanslıdır.

## Karar

| Ne | Lisans |
|---|---|
| Veri (`datasets/data`, sözlükler, şemalar) | **CC BY 4.0** |
| İçerik (`handbook`, `.github` belgeleri) | **CC BY 4.0** |
| Kod (`platform`, `datasets/tools`) | **MIT** |

1. **Gelen = giden (inbound = outbound):** Bir depoya PR açmak, katkının o deponun lisansıyla yayımlanmasını kabul etmek anlamına gelir. Bu, PR şablonunda ve katkı rehberinde açıkça yazılıdır.
2. **DCO veya CLA istenmez.** DCO, `Signed-off-by` satırında gerçek ad beklentisi taşır; bu, takma adla katkı modelimizle çelişir.
3. **Atıf biçimi:** "Greater Türkiye katkıcıları, CC BY 4.0" ve veri sürümü etiketi veya Zenodo DOI'si.
4. **Üçüncü taraf içerik asla kopyalanmaz.** Metin, görsel, video, veri tabloları depoya konmaz; kendi cümlelerimizle özet + bağlantı + arşiv bağlantısı kullanılır. Bir iddiayı doğru aktarmak için kısa alıntı yapılabilir.
5. **Kaynak koşulları (`terms`) uygulanır:** `restricted` ve `no-redistribution` kaynakların verisi kopyalanmaz, türetilmez; yalnızca ipucu olarak kullanılır ve hiçbir kaydın tek kaynağı olamaz ([06](../tr/06-sourcing-archiving.md), [0010](0010-content-safety-gates.md)).
6. Kayıtlarımızdaki olgusal bilgiler (bir olayın yeri, zamanı, aktörü) kendi yazdığımız metinle ifade edilir; bu, kaynakların ifadesinin değil, bizim derlememizin lisanslanmasıdır.

## Sonuçlar

- Veri, ticari kullanım dahil serbestçe yeniden kullanılabilir; atıf zorunludur.
- Takma ad korunur; katkı sahipliği git geçmişi ve takma ad üzerinden izlenir.
- DCO olmaması, katkının kaynağı konusunda daha zayıf hukuki güvence demektir; bunu inceleme süreci ve "gelen = giden" beyanıyla dengeliyoruz.
- Lisans değişikliği, geçmiş katkıların tüm sahiplerinin onayı olmadan yapılamaz; bu yüzden bu karar kalıcı kabul edilir.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| CC0 / kamu malı | Atıf zorunluluğu olmaz; kaynağın izlenebilirliği zayıflar. |
| CC BY-SA / ODbL | Paylaşım-aynı-koşul yükümlülüğü, kullanıcıları (özellikle gazetecileri) caydırır. |
| CC BY-NC | "Ticari olmayan" belirsizdir; açık veri tanımına uymaz. |
| DCO / CLA | Takma adla katkıyla çelişir. |
