# 0012 · Yönetişim

> **EN:** Roles are contributor → triager → reviewer → maintainer; PRs need 1 approval from a non-author by default (N configurable in `policy.yaml`, raised to 2 once there are ≥3 reviewers); admins may only change protected branches via PR; decisions are made by maintainer consensus with ADRs for core changes; maintainers enforce the code of conduct.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-12

## Bağlam

Gönüllü, takma adlı ve bütçesiz bir topluluğun kimin neye karar verdiğini açıkça yazması gerekir. Başlangıçta çok az kişi olacak; kurallar hem küçük hem büyümüş bir topluluğa uymalıdır. Güvenlik gerekçesiyle (bkz. [0011](0011-threat-model.md)) hiçbir kişinin tek başına yayın kapılarını aşamaması gerekir.

## Karar

### Roller

| Rol | GitHub ekibi | Yetki | Yol |
|---|---|---|---|
| Katkıcı | — | Fork + PR, sorun kaydı | Herkes |
| Triyajcı | `triagers` | Triage (etiketleme, kapatma, atama) | 5 birleşmiş PR + bakımcı önerisi |
| İnceleyici | `reviewers` | `datasets` ve `handbook`'ta yazma; veri için CODEOWNERS; PR onayı; Kapı 1 triyajı | ~3 ay katkı + 2 kefil + OPSEC brifingi |
| Bakımcı | `maintainers` | Yönetici; `policy:approved`; `policy.yaml`; altyapı; acil durdurma | Bakımcıların oydaşması |

Ayrıntılar: [10 · Katkı Rehberi](../tr/10-contributing.md).

### İnceleme kuralları

1. Varsayılan: Her PR, **yazarı dışında en az 1 onay** gerektirir.
2. Gerekli onay sayısı (N) `policy.yaml` içinde ayarlanır ve dal korumasına yansıtılır.
3. **İnceleyici sayısı 3 veya daha fazla olduğunda N = 2'ye yükseltilir.** İlk katkılar, N'den bağımsız olarak iki inceleyiciden geçer.
4. Türk kuvvetleri kapısına takılan kayıtlar ayrıca bir bakımcının `policy:approved` etiketini gerektirir; etiketi koyan bakımcı PR'ın yazarı olamaz.
5. `policy.yaml`, şemalar, sözlüklerde politik anlam taşıyan değişiklikler ve CI iş akışları bakımcı onayı gerektirir (CODEOWNERS).
6. **Yöneticiler de kurallara tabidir:** Korumalı dallara doğrudan push yoktur; yöneticiler değişiklikleri yalnızca PR yoluyla yapabilir, dal koruması yöneticileri de kapsar. Acil durumlarda (ör. kişisel verinin geçmişten temizlenmesi) yapılan istisnai işlemler `internal`'da gerekçesiyle kayda geçirilir.
7. Çıkar çatışması olan inceleyici çekimser kalır.

### Karar alma

- Günlük kararlar (bir kaydın birleştirilmesi, etiketleme) inceleme kurallarıyla alınır.
- **Temel değişiklikler** (depo yapısı, veri modeli, doğrulama kuralları, kırmızı çizgiler, lisans, yönetişim, altyapı) **ADR** gerektirir ([decisions/README.md](README.md)).
- ADR'ler ve politika değişiklikleri **bakımcı oydaşmasıyla** kabul edilir: PR en az 7 gün açık kalır; hiçbir bakımcı gerekçeli itiraz etmezse kabul edilir. İtiraz varsa tartışma sürer; uzlaşılamazsa değişiklik yapılmaz (mevcut durum korunur).
- Kırmızı çizgileri **gevşeten** bir değişiklik, tüm bakımcıların açık onayını gerektirir. Sıkılaştıran değişiklik acil durumda tek bakımcı tarafından geçici olarak uygulanabilir ve sonra olağan süreçten geçer.

### Davranış kuralları

- Davranış kuralları `.github` deposundadır; tüm depolarda, kanallarda ve topluluk alanlarında geçerlidir.
- Uygulama bakımcıların sorumluluğundadır. Şikâyetler [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) içindeki özel adrese yapılır.
- Şikâyetle ilgili bakımcı karar sürecinden çekilir.
- Yaptırımlar kademelidir (uyarı → geçici uzaklaştırma → kalıcı yasak); ağır kırmızı çizgi ihlallerinde doğrudan kalıcı yasak uygulanır ([02](../tr/02-red-lines.md)).

### Süreklilik

- Organizasyonun ve her hizmet hesabının **en az iki sahibi** vardır.
- Uzun süre etkin olmayan hesapların yetkileri geri alınabilir.
- Bakımcı sayısı birin altına düşme riskine karşı, bakımcılar güvenilir inceleyicileri bakımcılığa hazırlamaktan sorumludur.

## Sonuçlar

- Küçük bir toplulukla çalışabilir (1 onay), büyüdükçe sıkılaşır (2 onay).
- Hiçbir kişi, yönetici dahil, inceleme kapılarını tek başına aşamaz.
- Oydaşma yavaştır; temel değişikliklerin yavaş olması bilinçli bir tercihtir.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Tek kurucu yönetimi (BDFL) | Tek kişi riski (ele geçirme, tükenme, baskı). |
| Oylama (çoğunluk) | Küçük toplulukta kukla hesap riskini büyütür; azınlığın güvenlik itirazları ezilebilir. |
| Yöneticilerin doğrudan push yetkisi | Ele geçirilmiş bir yönetici hesabının tek başına zarar vermesine izin verir. |
