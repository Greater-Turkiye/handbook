# 0014 · Harita: işgal altındaki topraklar, insan hakları işaretleri, tampon bölgeler

> **EN:** Extends 0013: territory Türkiye regards as occupied (Palestine on 1967 lines incl. Gaza, Golan, Crimea) is drawn hatched with its de jure state and a sourced note; human-rights markers (East Turkestan) outline a region with sources and are explicitly not boundary claims; zones controlled by Turkish forces (e.g., in Syria or Iraq) are never drawn — presence stays at country level only.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-13

## Bağlam

[0013](0013-map-layers-turkiye-perspective.md) sonrası bakımcılar üç ek istekte bulundu: Filistin'in (Gazze dahil) net ayrılması ve işgal altındaki bölgelerin gösterilmesi; Doğu Türkistan'da Uygur Türklerine yönelik ihlallerin işaretlenmesi; Suriye ve başka yerlerdeki "tampon bölgelerin" yeşille gösterilmesi. İlk ikisi Türkiye'nin resmî tutumuyla ve kaynak kuralımızla uyumludur. Üçüncüsü Türk kuvvetlerinin konumunu haritalamak anlamına gelir ([02 · Kırmızı çizgiler](../tr/02-red-lines.md) §1, [0010](0010-content-safety-gates.md)).

## Karar

1. **İşgal altındaki topraklar** (`apps/web/assets/data/disputed-tur-view.geojson`, `occupier` alanı): Filistin Devleti 1967 sınırlarıyla (Batı Şeria — Doğu Kudüs dahil — ve Gazze), Golan ve Kırım; hukuki (de jure) devletin rengiyle, taramalı dolgu ve kesikli kenarla çizilir. Her birinin notu dayanağını verir (BMGK 2334, BMGK 497, BMGK 68/262; Türkiye'nin 1988'de Filistin'i tanıması). Türkiye'nin tanıdığı devletlerin adları silinmez; etiketler işgal altındaki toprakların üzerine yerleştirilmez.
2. **İnsan hakları işaretleri** (`apps/web/assets/data/concern-regions.geojson`): bir bölgeyi turkuaz kesikli kenarla çevreler ve kaynaklı not taşır. İlk kayıt: Doğu Türkistan (Sincan Uygur Özerk Bölgesi) — T.C. Dışişleri Bakanlığı açıklaması (9 Şubat 2019) ve BM İnsan Hakları Yüksek Komiserliği değerlendirmesi (31 Ağustos 2022). İşaret bir sınır veya egemenlik iddiası değildir ve bunu açıkça söyler. Yeni işaret en az bir resmî (Türkiye veya BM) kaynakla eklenir.
3. **Tampon / operasyon bölgeleri gösterilmez.** Türk kuvvetlerinin kontrol ettiği veya konuşlandığı alanlar (Suriye, Irak veya başka yer) haritada çizilmez, renklendirilmez, etiketlenmez. Resmî TSK varlığı yalnızca ülke düzeyinde ([0013](0013-map-layers-turkiye-perspective.md) §3) kalır.

## Sonuçlar

- Filistin ve Gazze her ölçekte görünür; "işgal altında" görsel dili Filistin, Golan ve Kırım için tutarlıdır.
- İnsan hakları konuları haritada görünür olur ama sınır tartışmasına dönüşmez.
- Operasyon bölgeleri isteği karşılanmaz; bu, kırmızı çizginin bilinçli sonucudur ve ancak kırmızı çizgilerin kendisini değiştiren (tüm bakımcıların açık onayını gerektiren, [0012](0012-governance.md)) yeni bir ADR ile değişebilir.

## Alternatifler

- **Tampon bölgeleri "resmî açıklamalara dayanarak" çizmek:** Resmî açıklamalar da olsa alan çizmek konum bilgisi üretir; reddedildi.
- **Doğu Türkistan'ı ayrı ülke gibi çizmek:** Türkiye'nin resmî tanımasıyla uyuşmaz ve güvenilirliği zedeler; insan hakları işareti seçildi.
