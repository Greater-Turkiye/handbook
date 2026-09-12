# 0007 · İnsan onaylı yayın

> **EN:** Nothing is published without human approval: gate 1 is private triage in a Telegram reviewer group, gate 2 is public PR review in `datasets`; bulletins are distinct from records; maintainers hold a kill switch; corrections and withdrawals are auto-posted.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Gelecekteki otomasyon (toplayıcılar, isteğe bağlı LLM adımları, yayıncı botlar) çok sayıda sinyal üretecek. Otomatik yayın; yanlış bilgi, kırmızı çizgi ihlali, istem enjeksiyonu (prompt injection) ve hukuki risk demektir ([0011](0011-threat-model.md)). Öte yandan hız da değerlidir: Bazı bilgiler, tam kayıt olmadan önce kısa bir duyuru olarak paylaşılabilmelidir.

## Karar

### İki kapı

| Kapı | Nerede | Kim | Ne onaylanır? |
|---|---|---|---|
| **Kapı 1 — Özel triyaj** | Özel Telegram inceleyici grubu (bot ile), veriler Cloudflare D1'de | İnceleyiciler | Ham sinyalin **bülten** olarak paylaşılması ve/veya kayda dönüştürülmek üzere işaretlenmesi. Reddedilenler paylaşılmaz. |
| **Kapı 2 — Açık PR incelemesi** | `datasets` deposu | İnceleyiciler (+ gerekirse bakımcı `policy:approved`) | **Kaydın** veri setine girmesi. |

- Kapı 1'i geçen öğeler, bot tarafından `datasets`'e **PR olarak** açılır; bot PR'ı kendi kendine birleştiremez.
- Kapı 2'yi geçip birleşen kayıtlar, yayıncılar tarafından Telegram ve Bluesky'ye gönderilir. X'e paylaşım **elle** yapılır ([0008](0008-zero-budget-infrastructure.md)).

### Bülten ve kayıt ayrımı

- **Bülten**: Kapı 1 onaylı, kısa, her zaman `[DOĞRULANMADI]` / `[UNVERIFIED]` etiketli, atfedilmiş duyuru. Veri setinin parçası değildir.
- **Kayıt**: Kapı 2'den geçmiş, şemaya uygun, kalıcı ID'li veri.
- Her bülten ya bir kayda dönüşür ya da (yanlış çıkarsa) geri çekme notuyla kapatılır.
- Kırmızı çizgilere dokunan hiçbir şey bülten olarak yayımlanamaz; Türk kuvvetlerine ilişkin içerik yalnızca Kapı 2 ve Türk kuvvetleri kapısı yoluyla, gecikmeli yayımlanır.

### Acil durdurma (kill switch)

- Herhangi bir bakımcı, **tek bir ayarla** tüm otomatik yayını (bülten ve kayıt paylaşımları, bot PR'ları) derhal durdurabilir.
- Durdurma; hesap ele geçirme şüphesi, toplu yanlış bilgi, hukuki talep veya kırmızı çizgi ihlali durumunda kullanılır. Durdurmak için oydaşma gerekmez; yeniden başlatmak için gerekçe `internal`'da kayda geçirilir.

### Düzeltmelerin otomatik paylaşımı

- Yayımlanmış bir kayda `corrections[]` girdisi eklenmesi veya kaydın mezar taşına dönüşmesi, ilk paylaşımın yapıldığı kanallara **otomatik** olarak "DÜZELTME / CORRECTION" veya "GERİ ÇEKİLDİ / WITHDRAWN" notu olarak gönderilir.
- Düzeltmeler en az ilk paylaşım kadar görünür olmalıdır.

## Sonuçlar

- Hiçbir içerik insan onayı olmadan kamuya ulaşmaz; LLM veya toplayıcı hataları yayına dönüşmez.
- Hız, bültenler sayesinde kısmen korunur; doğruluk, kayıtlar sayesinde korunur.
- İnceleyici emeği darboğazdır; toplayıcılar yüksek sinyal/gürültü oranına göre ayarlanmalıdır.
- Özel Telegram grubu, Telegram'a bağımlılık ve üye güvenliği riski yaratır ([0011](0011-threat-model.md)).

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Tam otomatik yayın | Yanlış bilgi ve kırmızı çizgi riski kabul edilemez. |
| Yalnızca PR incelemesi (Kapı 2) | Ham sinyaller herkese açık PR'larda görünür; hassas içerik sızar. |
| Triyajın GitHub özel deposunda yapılması | Mobil kullanımı zayıf; inceleyiciler için hantal. İleride yeniden değerlendirilebilir. |
