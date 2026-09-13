# 0013 · Harita katmanları: Türkiye perspektifi

> **EN:** The web map shows Türkiye's official positions explicitly and attributed (borders per Türkiye's recognition, defence agreements, Mavi Vatan, islands), never as undisputed fact; every layer entry needs a signed agreement or official document plus a source; Turkish military presence is shown at country level only; diplomatic missions are shown as inviolable missions, not Turkish territory; schematic maritime areas are labelled as such.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-13

## Bağlam

Web sitesinin ([platform/apps/web](https://github.com/Greater-Turkiye/platform/tree/main/apps/web)) haritası, topluluğun en görünür yüzüdür. Bakımcılar haritanın Türkiye'nin bakış açısını açıkça yansıtmasını istedi: müttefikler ve anlaşmalar, Mavi Vatan, adalar, Kıbrıs, dış temsilcilikler. Aynı zamanda proje bir OSINT projesidir; güvenilirliği, iddialarını kaynağa dayandırmasına ve tartışmalı konuları atfetmesine bağlıdır ([0006](0006-verification-scale.md), [02 · Kırmızı çizgiler](../tr/02-red-lines.md), [07 · Coğrafya, zaman, tartışmalı alanlar](../tr/07-geo-time-disputed.md)).

Kullanılan temel harita verisi (Natural Earth) bazı yerlerde Türkiye'nin resmî tutumuyla çelişir (ör. Kırım'ı Rusya'ya, Golan'ı İsrail'e bağlar; Somaliland'i ayrı gösterir).

## Karar

1. **Sınırlar Türkiye'nin tanımasına göre çizilir** ve farkı açıklayan not taşır: Kırım → Ukrayna (BMGK 68/262), Golan → Suriye (BMGK 497), Somaliland → Somali; KKTC ayrı devlet; Filistin etiketlenir. Türkiye'nin tanıdığı devletler (ör. İsrail) yeniden adlandırılmaz. Veri: `apps/web/assets/data/disputed-tur-view.geojson`, `gt.js` (`NAMELESS`).
2. **Anlaşma katmanı** (`GT.AGREEMENTS`, `GT.PARTNERS`) yalnızca **imzalanmış** anlaşma veya resmî belgeyle ve **kaynak bağlantısıyla** doldurulur. Seviyeler: `ally` (karşılıklı savunma taahhüdü), `coop` (savunma/askerî işbirliği anlaşması), `kin` (Türk Devletleri Teşkilatı üyesi/gözlemcisi). Niyet beyanı, ziyaret veya basın yorumu yeterli değildir; kaynağı bulunamayan ülke boyanmaz.
3. **Resmî TSK varlığı** yalnızca resmî olarak açıklanmış kalıcı varlık (anlaşma, TBMM tezkeresi) için ve **yalnızca ülke düzeyinde** gösterilir; üs, konum, birlik veya hareket gösterilmez (kırmızı çizgi, [0010](0010-content-safety-gates.md)). Doğrulanmamış "üs" iddiaları gösterilmez.
4. **Mavi Vatan** (`maritime-tur.geojson`) üç durumla çizilir: `agreed` (anlaşmayla belirlenmiş), `claimed` (Türkiye'nin BM'ye bildirdiği sınırlar; itiraz edilen), `schematic` (resmî koordinat bulunmayan kesimler için Türkiye'nin tutumu esas alınarak bizim çizdiğimiz alan). Şematik alanlar ekranda ve verinin kendisinde **şematik** olarak etiketlenir ve yöntemleri [MARITIME-SOURCES.md](https://github.com/Greater-Turkiye/platform/blob/main/apps/web/assets/data/MARITIME-SOURCES.md)'de yazılıdır; asla resmî koordinat gibi sunulmaz.
5. **Adalar**: Türk adaları gösterilir; Kardak gibi egemenliği tartışmalı kayalıklar "Türkiye'nin tutumu" notuyla ve farklı simgeyle gösterilir.
6. **Dış temsilcilikler** şehir düzeyinde "Türk dış temsilciliği" olarak gösterilir. Temsilcilikler 1961/1963 Viyana Sözleşmeleri gereği dokunulmazdır ancak **Türk toprağı değildir**; site bunu böyle ifade eder.
7. Olay kayıtları konumsuzsa haritada **bölge düzeyi halka** olarak, "kesin konum yok" notuyla gösterilir; konum uydurulmaz.
8. Her katmanın kaynağı, lisansı ve işleme adımları `apps/web/assets/LICENSES.md` ve `*-SOURCES.md` dosyalarında tutulur.

## Sonuçlar

- Harita Türkiye'nin bakışını açıkça gösterir, ancak her unsur bir kaynağa ve açık bir etikete dayanır; yabancı okur neyin Türkiye'nin tutumu olduğunu ayırt edebilir.
- Bazı istekler karşılanmaz veya bekletilir (ör. imzalı anlaşması bulunamayan bir ülkeyi boyamak). Yeni kaynak bulunduğunda tek satırlık bir PR ile eklenir.
- Anlaşma listesi zamanla eskir; gözden geçirme yılda en az bir kez veya önemli bir anlaşma imzalandığında yapılır.

## Alternatifler

- **Tarafsız (yalnızca Natural Earth) harita:** Topluluğun amacıyla ve Türkiye'nin resmî tanımalarıyla uyuşmadığı için reddedildi.
- **Popüler Mavi Vatan haritasını elle çizmek:** Kaynağı ve yöntemi belirsiz olduğu için reddedildi; bunun yerine resmî koordinatlar + belgelenmiş şematik yöntem seçildi.
- **Kaynaksız "dost ülke" boyaması:** Doğrulanamaz ve güvenilirliği zedeler; reddedildi.
