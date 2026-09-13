# 10 · Katkı Rehberi

Hoş geldiniz! Bu sayfa, hiç katkı vermemiş birinin ilk katkısını nasıl yapacağını adım adım anlatır. Kod bilmeniz gerekmez.

## Başlamadan önce (zorunlu)

1. [Kırmızı Çizgiler](02-red-lines.md) sayfasını okuyun. **Bu pazarlık konusu değildir.**
2. [OPSEC](04-opsec.md) sayfasındaki kontrol listesini uygulayın (noreply e-posta, 2FA, UTC commit).
3. [Doğrulama](05-verification.md) ve [Yazım Kılavuzu](08-style-guide.md) sayfalarına göz atın.
4. Organizasyonun [davranış kurallarını](https://github.com/Greater-Turkiye/.github) okuyun.

Bir PR açmak, katkınızın **CC BY 4.0** (veri ve içerik) veya **MIT** (kod) lisansıyla yayımlanmasını kabul ettiğiniz anlamına gelir ([ADR 0009](../decisions/0009-licensing.md)). DCO imzası istemiyoruz.

## Roller ve terfi yolu

| Rol | Yetki | Nasıl olunur? |
|---|---|---|
| **Katkıcı** (contributor) | Fork + PR, sorun kaydı açma | Herkes. İzin gerekmez. |
| **Triyajcı** (triager, `triagers` ekibi) | Sorun kayıtlarını etiketleme, kapatma, atama | **5 birleşmiş PR** sonrası, bir bakımcının önerisiyle. |
| **İnceleyici** (reviewer, `reviewers` ekibi) | `datasets` ve `handbook` depolarına yazma; veri için CODEOWNERS; PR onayı | **Yaklaşık 3 ay** düzenli katkı + **2 kefil** (mevcut inceleyici/bakımcı) + **OPSEC brifingi**. |
| **Bakımcı** (maintainer, `maintainers` ekibi) | Yönetici; `policy:approved` etiketi; politika ve altyapı | Bakımcıların **oydaşmasıyla** ([ADR 0012](../decisions/0012-governance.md)). |

Notlar:
- Rol, bir ödül değil sorumluluktur. İnceleyici olmak, kırmızı çizgilerin bekçisi olmak demektir.
- Takma adla çalışanlar da her role yükselebilir. Kimlik doğrulaması istenmez; güven, katkı geçmişiyle kazanılır.
- Uzun süre (ör. 6 ay) etkin olmayan hesapların yetkileri güvenlik amacıyla geri alınabilir; geri döndüğünüzde tekrar verilir.

## İlk işinizi bulun

- Organizasyon genelinde **`good first issue`** etiketli açık kayıtlar: [bu aramayla](https://github.com/search?q=org%3AGreater-Turkiye+label%3A%22good+first+issue%22+state%3Aopen&type=issues) listelenir.
- İyi başlangıç işleri: eksik İngilizce çeviri, arşiv bağlantısı eksik kaynaklar, kaynak siciline yeni kaynak, `i18n.machine` işaretli metinlerin gözden geçirilmesi, el kitabındaki yazım hataları.
- Bir işi almak için kayıtta "Bunu ben alıyorum" yazın; bir hafta içinde ilerleme yoksa iş başkasına açılır.

## Yol A: Kod bilmeden veri gönderme (sorun formları)

1. [`datasets` sorun formları](https://github.com/Greater-Turkiye/datasets/issues/new/choose) sayfasına gidin.
2. Uygun formu seçin (ör. olay bildirimi, kaynak önerisi, düzeltme talebi).
3. Formu doldurun: ne oldu, nerede, ne zaman (UTC), kaynak bağlantısı ve **arşiv bağlantısı** ([06](06-sourcing-archiving.md)).
4. Gönderin. Bir triyajcı etiketler; bir katkıcı veya inceleyici bunu kayda dönüştürür.

> ⚠ Sorun kayıtları **anında herkese açıktır**. Hassas bir durum (kırmızı çizgi şüphesi, size gönderilen sızıntı vb.) için form değil, [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) kanalını kullanın.

## Yol B: Kayıt dosyası ile PR (fork + PR)

Gerekenler: git, güncel bir Python 3 sürümü, bir metin düzenleyici. Kesin kurulum adımları `datasets` deposunun README dosyasındadır.

```bash
# 1. GitHub'da datasets deposunu fork'layın, sonra:
git clone https://github.com/<takma-adiniz>/datasets.git
cd datasets
git remote add upstream https://github.com/Greater-Turkiye/datasets.git

# 2. Yeni bir dal açın
git switch -c evt-girit-tatbikat

# 3. Yeni kayıt iskeleti oluşturun (ID ve dosya yolu otomatik üretilir)
python tools/gt.py new event
#   -> data/event/<yyyy>/<mm>/evt_<26 karakter>.yaml

# 4. Dosyayı düzenleyin: başlık/özet (tr + en), zaman (UTC) ve hassasiyet,
#    konum ve hassasiyet, countries, actors, sources (arşivli), assessment, claims

# 5. Doğrulayın
python tools/gt.py validate

# 6. UTC ile commit edin ve gönderin
TZ=UTC git commit -am "evt: Girit açıklarında Yunan deniz tatbikatı"
git push -u origin evt-girit-tatbikat
```

7. GitHub'da **Pull Request** açın. PR şablonundaki kontrol listesini doldurun (kırmızı çizgiler, kaynak, arşiv, doğrulama).
8. CI kontrollerini bekleyin. Kırmızı olan kontrolü okuyup düzeltin; anlamadığınız bir hata varsa PR'da sorun.

Kurallar:
- **Bir PR, bir konu.** Birbiriyle ilgisiz kayıtları aynı PR'a koymayın.
- Mevcut bir kaydı **silmeyin, taşımayın, ID'sini değiştirmeyin.** Düzeltme için `corrections[]`, geri çekme için mezar taşı ([ADR 0003](../decisions/0003-identifiers.md)).
- Kaynak sicilde yoksa, önce (veya aynı PR'da) `python tools/gt.py new source` ile ekleyin.
- Medya dosyası eklemeyin ([06](06-sourcing-archiving.md)).

## İnceleme süreci: ne beklemelisiniz?

- Her PR, yazarı dışında **en az bir inceleyicinin onayını** alır; gerekli onay sayısı `policy.yaml` ile ayarlanır ([ADR 0012](../decisions/0012-governance.md)).
- **İlk katkılar** ek dikkatle, iki inceleyici tarafından incelenir ([ADR 0011](../decisions/0011-threat-model.md)).
- Türk kuvvetleri kapısına takılan kayıtlar ayrıca bir bakımcının `policy:approved` etiketini bekler ve en az 24 saat bekletilir.
- İnceleyiciler gönüllüdür; birkaç gün sürebilir. Bir hafta içinde yanıt yoksa PR'da nazikçe hatırlatın.
- İnceleme yorumları kayda yöneliktir, size değil. Anlaşmazlıkta [Doğrulama](05-verification.md) kuralları ve kaynaklar konuşur.
- İnceleyici değişiklik isterse aynı dala yeni commit gönderin; PR otomatik güncellenir.

## İnceleyiciler için beklentiler

- Kırmızı çizgi kontrolü **her PR'da** yapılır; CI geçti diye atlanmaz.
- Kaynakları ve arşiv bağlantılarını **gerçekten açın**; bağımsızlığı kontrol edin.
- Kendi yazdığınız PR'ı onaylamayın; çıkar çatışması varsa çekimser kalın.
- Kibar, somut ve öğretici olun: "Bu yanlış" değil, "Bu nitelendirme `claims[]`'e taşınmalı, bkz. 08".

## Diğer katkı yolları

- **El kitabı**: Bu depoya PR açarak. Türkçe sayfa esastır; Türkçeyi değiştirirseniz İngilizce çeviriyi de güncelleyin veya bir sorun kaydı açın. CI'daki **çeviri sapması kontrolü** (`Translation drift`), Türkçe sayfası İngilizcesinden sonra değişen sayfalar için uyarı verir. Bir İngilizce sayfada `> translation_of: tr/<dosya>.md` başlığı eksikse, başlık var olmayan bir sayfayı gösteriyorsa veya bir Türkçe sayfanın İngilizce aynası yoksa başarısız olur.
- **Kod** (`platform`): Ayrı bir katkı rehberi o depoda yer alacaktır.
- **Karar önerisi**: Yeni bir ADR ile ([decisions/README.md](../decisions/README.md)).
