# 0026 · Animasyon motoru için ayrı depo

> **EN:** Proposes a fifth repository, `motion`, for an engine that turns sourced records into short video cards automatically — a relief globe, country and alliance highlights, a news card — built to spread on short-video platforms. It is a separate repository because it needs a build step (WebGL shaders, TypeScript) that the site repository deliberately does not have, and because its output is media, not data or the site. The project's rules apply to video unchanged: sourced hooks only, the verification status on screen, nothing about Turkish forces, no targeting views; state arms and alliance emblems appear only in news context, over their subject. Posting to channels automatically would change ADR 0007 and needs its own decision. Proposed; the plan and four design directions are in the repository for the owner's choice.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-30
- **Önerenler:** @nukIeer
- **İlgili:** [0001](0001-repository-boundaries.md), [0007](0007-human-in-the-loop-publishing.md), [0013](0013-map-layers-turkiye-perspective.md), [0023](0023-automatic-unverified-records.md)

## Bağlam

Kayıtlar artık otomatik birikiyor, ama okuyan az. Kısa video platformları bir haberi en geniş
kitleye ulaştıran yer. Sahip, veri setindeki olaylardan otomatik ve yüksek kaliteli animasyonlu
video kartları istiyor; amaç yayılmaları.

## Karar

- `Greater-Turkiye/motion` deposu açılır. İçinde animasyon motoru, şablonlar, sahne dosyaları ve
  dışa aktarım hattı yaşar.
- [0001](0001-repository-boundaries.md)'deki "kod tek monorepo" ilkesine bir istisnadır: motorun
  derleme adımı (TypeScript, GLSL) gerekir, site deposu ise bilerek derlemesizdir; motorun çıktısı da
  ne veri ne site, medyadır.
- Kurallar videoya da uygulanır: kanca kaydın kendi olgusudur; kaynak satırı ve doğrulama durumu
  ekrandadır; Türk kuvvetlerine ait kayıttan video üretilmez; hedef görünümü, kritiklik puanı ve
  kişisel veri yoktur. Devlet armaları ve ittifak amblemleri yalnızca haber bağlamında, konularının
  üstünde kullanılır; logomuzun yanında ya da onay izlenimi veren biçimde değil.
- Üretim tam otomatiktir. Kanallara otomatik gönderim [0007](0007-human-in-the-loop-publishing.md)'yi
  değiştirir ve ayrı bir ADR ile açılır.

## Sonuçlar

- Beşinci depo, bakım yükü. Plan aşamalı (M1–M7); her aşamanın kabul ölçütü var.
- Videolar kaynaklı olduğu için bir hatanın düzeltmesi de kayıttan videoya yayılabilir.

## Alternatifler

| Alternatif | Neden seçilmedi? |
|---|---|
| Motoru `platform` içine koymak | Site deposunun derlemesiz kuralını bozar; medya üretimi site işiyle karışır. |
| Remotion | Üç kişiden büyük kuruluşlarda ücretli lisans; sıfır bütçeye aykırı. |
| Elle kurgu (After Effects vb.) | Otomatik değil, ücretli, tekrarlanamaz. |
