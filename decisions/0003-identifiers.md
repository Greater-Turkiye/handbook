# 0003 · Tanımlayıcılar

> **EN:** Records use TypeID-style IDs (`<prefix>_<26-char base32 UUIDv7>`) with prefixes evt/act/sit/eqp/src; the file path derives from the ID's timestamp; IDs are permanent and never reused; files are never deleted or moved — withdrawal is a tombstone.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Kayıtlara dışarıdan (başka veri setleri, makaleler, paylaşımlar) bağlantı verilecek. Kimlikler kalıcı olmalı, merkezi bir sayaç gerektirmeden çakışmasız üretilebilmeli, türü bir bakışta anlaşılmalı ve dosya sisteminde dengeli dağılmalı.

## Karar

### Biçim

TypeID tarzı: `<önek>_<26 karakter>`. Sonek, bir **UUIDv7**'nin küçük harfli Crockford base32 kodlamasıdır (26 karakter). UUIDv7 zaman sıralıdır; ilk bitleri oluşturulma zamanını milisaniye hassasiyetinde taşır.

| Tür | Önek | Örnek (uydurma) |
|---|---|---|
| event (olay) | `evt_` | `evt_01j8x3k5r2m9q7t4v6w8y0z2ab` |
| actor (aktör) | `act_` | `act_…` |
| site (tesis) | `sit_` | `sit_…` |
| equipment (teçhizat) | `eqp_` | `eqp_…` |
| source (kaynak) | `src_` | `src_…` |

`tombstone` ayrı bir önek değildir: Geri çekilen kayıt **kendi ID'sini korur**, yalnızca içeriği `schema: tombstone/1` olur.

### Dosya yolu

Yol ID'den türetilir: `data/<kind>/<yyyy>/<mm>/<id>.yaml`. Yıl ve ay, **ID'nin içindeki zaman damgasından** (UTC) alınır; olayın tarihinden değil. Böylece yol, ID'den her zaman hesaplanabilir ve kayıt içeriği değişince dosya taşınmaz. CI, yol–ID tutarlılığını denetler.

### Kalıcılık kuralları

1. ID bir kez atandıktan sonra **değişmez**.
2. ID **asla yeniden kullanılmaz**, geri çekilmiş olsa bile.
3. Dosyalar **silinmez ve taşınmaz**.
4. **Geri çekme** = dosyanın içeriğinin `schema: tombstone/1` ile değiştirilmesi (gerekçe ve varsa yerine geçen kaydın ID'si ile; kesin alanlar şemadadır).
5. **Mükerrer kayıt** tespit edilirse biri mezar taşı olur ve diğerine işaret eder.
6. **Düzeltmeler** `corrections[]` ile yapılır; ID değişmez.
7. Tek istisna: Kişisel veri veya gizli materyal içeren bir kaydın git geçmişinden temizlenmesi ([02 · Kırmızı çizgiler](../tr/02-red-lines.md)). Bu durumda bile ID, mezar taşı olarak kalır.

ID'ler yalnızca `python tools/gt.py new <kind>` ile üretilir; elle yazılmaz.

## Sonuçlar

- Merkezi sayaç yok; eşzamanlı PR'lar çakışmaz.
- Önek sayesinde bir ID'nin türü bağlamsız anlaşılır; yanlış türde referans CI'da yakalanır.
- Ay klasörleri dosyaları dengeli dağıtır.
- ID'deki zaman damgası kaydın **oluşturulma** zamanını açığa çıkarır (olay zamanını değil); bu kabul edilebilir bir bilgi sızıntısıdır. Commit zamanı zaten herkese açıktır.
- Mezar taşları birikir; bu bilinçli bir bedeldir (kırık bağlantı yok).

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Artan tamsayı (`evt-000123`) | Merkezi sayaç; eşzamanlı PR'larda çakışma. |
| UUIDv4 | Zaman sıralı değil; yol türetilemez; tür anlaşılmaz. |
| İçerikten türetilen kısa ad (slug) | Başlık düzeltilince ID değişir; dil bağımlı. |
| Olay tarihine göre klasör | Tarih düzeltilince dosya taşınmak zorunda kalır. |
