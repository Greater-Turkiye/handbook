# 0010 · İçerik güvenliği kapıları

> **EN:** CI enforces content-safety rules defined in `policy.yaml` — forbidden personal-data keys, PII regexes (TC Kimlik, phone, email, IBAN), classification markings, blocked URL shorteners, the Turkish forces gate and the restricted-source rule — but CI cannot stop a public PR from being seen, so sensitive submissions go by private email.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Kırmızı çizgiler ([02](../tr/02-red-lines.md)) insan incelemesiyle korunur, ama insanlar yorulur ve hata yapar. Makinece denetlenebilecek kuralların her PR'da, istisnasız ve aynı biçimde uygulanması gerekir. Kuralların kod içine gömülmesi yerine, incelenebilir ve sürümlenebilir tek bir politika dosyasında durması tercih edilir.

## Karar

`datasets/policy.yaml`, CI'ın uyguladığı içerik güvenliği kurallarını tanımlar. `gt.py validate` bu kuralları hem yerelde hem CI'da çalıştırır. `policy.yaml` değişiklikleri bakımcı onayı gerektirir (CODEOWNERS).

### CI'ın uyguladıkları

| Kontrol | Ne yapar? |
|---|---|
| **Yasaklı kişisel veri anahtarları** | Kayıtlarda kişisel veri taşıyan alan adlarını reddeder (ör. telefon, e-posta, adres, kimlik numarası, doğum tarihi, plaka türünden anahtarlar; tam liste `policy.yaml`'da). |
| **Kişisel veri kalıpları (regex)** | Tüm metin alanlarında tarar: **T.C. kimlik numarası** (11 hane, ilk hane sıfır değil, sağlama algoritmasıyla), **telefon numarası** (Türkiye ve uluslararası biçimler), **e-posta adresi**, **IBAN** (özellikle `TR` + 24 hane). Eşleşme PR'ı durdurur; yanlış pozitifler inceleyici tarafından gerekçeyle geçilebilir. |
| **Gizlilik derecesi işaretleri** | `GİZLİ`, `ÇOK GİZLİ`, `HİZMETE ÖZEL`, `KİŞİYE ÖZEL`, `SECRET`, `TOP SECRET`, `CONFIDENTIAL`, `NOFORN`, `RESTRICTED` gibi işaretleri metinlerde ve URL'lerde arar; eşleşme PR'ı durdurur ve bakımcıya bildirilir. |
| **Engellenen URL kısaltıcıları** | `bit.ly`, `t.co`, `tinyurl.com` vb. alan adlarını reddeder; izleme parametrelerini uyarı olarak işaretler. |
| **Türk kuvvetleri kapısı** | Türk askerî/güvenlik/istihbarat aktörü `perpetrator`, `participant`, `target` veya `host` rolündeyse ya da `policy.involves_tur_forces: true` ise: koordinat yok; hassasiyet yalnızca `admin1`/`country`/`sea-area`; olay en az **24 saat** önce; `policy.sensitivity: elevated`; bakımcının **`policy:approved`** etiketi. Biri eksikse birleştirme engellenir. |
| **Kısıtlı kaynak kuralı** | `terms: restricted` veya `no-redistribution` kaynak, bir kaydın tek kaynağı olamaz. |
| **Doğrulama kuralları** | `verified` koşulları ([0006](0006-verification-scale.md)). |
| **Biçim kuralları** | Koordinatlarda en fazla 5 ondalık, UTC zaman, ID–yol tutarlılığı, şema uyumu, medya dosyası yasağı. |

### CI'ın yapamadıkları

- **PR'lar anında herkese açıktır.** CI bir PR'ı birleştirmeden durdurabilir, ama içeriğin görünmesini engelleyemez. PR kapatılsa bile içerik önbelleklerde, fork'larda ve bildirim e-postalarında kalabilir. Bu yüzden **hassas gönderiler** (kırmızı çizgiye yakın olabilecek her şey) PR ile değil, [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) içindeki **özel e-posta** ile bakımcılara gönderilir.
- **Anlam denetimi yapamaz:** Kaynakların gerçekten bağımsız olup olmadığını, bir cümlenin hedef gösterip göstermediğini, bir görüntünün esir içerip içermediğini insan inceleyici değerlendirir.
- **Bağlantının arkasındaki içeriği denetleyemez:** Bir kaynak bağlantısının açtığı sayfanın kırmızı çizgi ihlali içerip içermediği inceleyiciye kalır.
- Regex'ler kaçırılabilir (boşluklu yazım, görsel içinde metin vb.); CI, insan incelemesinin yerine geçmez.

## Sonuçlar

- Kurallar tek yerde, herkese açık ve sürümlüdür; neyin neden engellendiği görünür.
- Yanlış pozitifler katkıcıları zaman zaman yavaşlatır; bu, güvenliğin bedelidir.
- Kötü niyetli bir kişi, CI'ı bilerek atlatmaya çalışabilir; bu yüzden ilk katkılar çift incelenir ([0011](0011-threat-model.md)).

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Kuralların yalnızca insan incelemesine bırakılması | Tutarsız; yorgunluk ve hata. |
| Kuralların kod içine gömülmesi | Görünmez, incelemesi zor; politika değişikliği kod değişikliği gerektirir. |
| Tüm katkıların önce özel depoda toplanması | Açık katkı modelini ve şeffaflığı öldürür; özel kanal yalnızca hassas durumlar için. |
