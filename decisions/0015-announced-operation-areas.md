# 0015 · Harita: Türkiye'nin resmî olarak ilan ettiği harekât bölgeleri

> **EN:** Supersedes ADR 0014 §3. Operation areas officially announced by the Turkish state (e.g. Euphrates Shield, Olive Branch, Peace Spring) may be shown in green as whole areas, with a status, an as-of date and official sources. Bases, posts, units, strengths and movements remain forbidden (red line §1).

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-13

## Bağlam

[0014](0014-occupied-territory-and-human-rights-markers.md) §3, Türk kuvvetlerinin kontrol ettiği bölgelerin haritada hiç gösterilmemesini seçmişti. Kurucu bakımcı bu bölgelerin yeşil olarak gösterilmesini üç kez açıkça istedi.

[Kırmızı çizgiler](../tr/02-red-lines.md) §1, resmî açıklamalar için zaten bir istisna tanır. Bu istisna koordinatsız, kaba konum hassasiyetinde, gecikmeli ve onaylı yayımı kapsar. Söz konusu bölgeler Cumhurbaşkanlığı ve MSB tarafından ilan edilmiştir; yıllardır kamuya açıktır ve binlerce km²'lik alanlardır. İlan edilen sınır bir birliğin konumunu değil, bir harekâtın kapsamını gösterir.

## Karar

1. Türk devletinin resmî olarak ilan ettiği harekât ve güvenlik bölgeleri (`platform` → `apps/web/assets/data/tur-operation-areas.geojson`) haritada **yeşil alan** olarak gösterilebilir.
2. **Yalnızca bölgenin tamamı** gösterilir.
   - Sınır, ilan edilen kapsama karşılık gelen idari birimlerden (ilçe/nahiye) kurulur ve sadeleştirilir.
   - Her özellikte şunlar bulunur: `status` (`active` | `ended` | `unclear`), `status_as_of`, resmî kaynaklar ve yöntem notu.
   - Kapsamı yaklaşık olan bölge "şematik" olarak etiketlenir.
3. **Hâlâ yasak olanlar:**
   - üs, karakol, gözlem noktası, kontrol noktası;
   - birlik adı ve gücü;
   - konuşlanma ve hareket;
   - bölge içindeki her türlü nokta verisi;
   - bölgenin güncel bir cephe hattı gibi sunulması.

   Resmî TSK varlığı ülke düzeyinde kalır ([0013](0013-map-layers-turkiye-perspective.md) §3).
4. Bu katman bir veri kaydı değildir. `datasets` deposundaki Türk kuvvetleri kapısı ([0010](0010-content-safety-gates.md)) değişmez.
5. Yeni bölge yalnızca resmî bir ilanla eklenir. Geçerli ilan kaynakları:
   - Cumhurbaşkanlığı,
   - MSB,
   - TBMM tezkeresi,
   - Resmî Gazete,
   - BM'ye yapılan Madde 51 bildirimi.

   Her bölgenin durumu, bölgeyi etkileyen her büyük gelişmede yeniden gözden geçirilir.

## Sonuçlar

- Bu karar 0014 §3'ün yerine geçer; 0014'ün geri kalanı geçerliliğini korur.
- Kırmızı çizgiler §1'e bu ADR'ye bağlanan bir harita katmanı istisnası eklenir.
- Artık geçerli olmayan bir kontrolün bugünkü durum gibi görünme riski vardır. Bu risk `status` ve `status_as_of` alanlarıyla ve haritadaki durum etiketiyle yönetilir.

## Alternatifler

- **Hiç göstermemek (0014 §3):** Bakımcının açık kararıyla terk edildi.
- **Üs veya nokta düzeyinde göstermek:** Kırmızı çizgi olduğu için reddedildi.
