# 0022 · Ticaret uyumu izlenir, sivil gemi takip edilmez

> **EN:** Opens a second compliance register, this time for Türkiye's own declared trade policy: the halt of trade with Israel announced in 2024, measured against what both states' official monthly statistics record. It is built from published statistics, not from ship movements. Live or near-live positions of civilian vessels are placed permanently out of scope — merchant ships in these waters are being attacked, a position is the one field that turns a compliance record into a target list, and the crews at risk include Turkish ones. What may be recorded about a ship is only what registries publish about its identity — IMO number, flag history, recorded owner or operator — and only with delay. The asymmetry of [0019](0019-foreign-installations-register.md) is deliberately reversed here: this register measures **our own** state's declared policy, which is the one thing a project of this kind can hold itself to without endangering anybody.

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-20
- **Önerenler:** @nukIeer
- **İlgili:** [0006](0006-verification-scale.md), [0009](0009-licensing.md), [0010](0010-content-safety-gates.md), [0011](0011-threat-model.md), [0013](0013-map-layers-turkiye-perspective.md), [0019](0019-foreign-installations-register.md), [0021](0021-coordinates-with-provenance.md)

## Bağlam

Soru şöyle soruldu: *İsrail'le ticaret yapan Türk gemilerini izleyebilir miyiz; muhtemelen bayrak değiştiriyorlar.*

Bu soru iki bambaşka ürüne çıkar ve aradaki fark, projenin var olup olmamasını belirler.

**Birinci ürün: gemi takibi.** Bir geminin şu anda nerede olduğunu, nereye gittiğini yayımlamak. Teknik olarak kısmen mümkündür (AIS akışları, kimi ücretsiz kimi ücretli). Sorun teknik değildir:

- **Kızıldeniz ve Doğu Akdeniz'de ticaret gemilerine fiilen saldırılıyor.** Bir sivil geminin konumunu ve yükünü birlikte yayımlamak, o gemiyi saldırıya açık hâle getiren tek bilgi bileşimidir. Mürettebat listelerinde Türk denizciler de vardır.
- Bir sivil gemi, silahlı çatışma hukukunda korunan bir hedeftir; onu hedef hâline getirecek bilgiyi üreten sivil yapı, kendi korumasını da kaybeder ([0011](0011-threat-model.md)).
- AIS verisi kapatılabilir, taklit edilebilir ve sıklıkla yanlıştır. Yanlış bir gemiyi işaret etmek, sicilin tamamını çürütür — ve bu kez bedelini bir şirket değil, bir gemi adamı öder.

**İkinci ürün: uyum ölçümü.** Türkiye 2024'te İsrail'le ticareti durdurduğunu açıkladı. "Bu gerçekten uygulanıyor mu?" sorusunun cevabı, gemilerde değil, **iki devletin kendi resmî istatistiklerinde** duruyor: Türkiye ihracatını varış ülkesine göre, İsrail ithalatını menşe ülkesine göre raporlar. Yasaktan önce iki çizgi birbirini yüzde birkaç farkla takip eder. Sonrasında Türkiye'nin defterinde İsrail satırı yoktur; İsrail'in defterinde Türkiye menşeli ithalat satırı durmaktadır.

İkisi arasındaki fark, kaçakçılık iddiası değildir — **yönlendirmenin ölçüsüdür**. Üçüncü bir ülke üzerinden sevk edilen Türk menşeli bir mal, Türkiye'nin defterinde o ülkeye ihracat, İsrail'in defterinde Türk menşeli ithalattır. Hiçbir gemi izlenmeden, iki resmî kaynağın kendi rakamlarıyla söylenebilecek en güçlü cümle budur ve kimseyi tehlikeye atmaz.

## Karar

### 1. Kapsam

Sicil, **Türkiye'nin kendi ilan ettiği ticaret politikasını** ve onun kayıtlardaki karşılığını izler. İlk konu, 2024'te ilan edilen İsrail ticareti durdurma kararıdır.

Kullanılan kaynaklar: UN Comtrade (her iki raportörün aylık beyanları), ulusal istatistik kurumları, resmî gazeteler ve bakanlık duyuruları, gemi sicillerinin yayımladığı kimlik kayıtları.

### 2. Gemiler hakkında ne kaydedilir

Yalnızca **kimlik** ve yalnızca **gecikmeli**:

- IMO numarası (kalıcıdır ve bayrak değişse de değişmez), bayrak geçmişi, sicile kayıtlı işletmeci/sahip, sınıflandırma kuruluşu — yani bir geminin kim olduğu.
- Liman idarelerinin veya sicillerin **yayımladığı** uğrak kayıtları, en az **30 gün gecikmeyle**.
- Her kayıt, [0021](0021-coordinates-with-provenance.md)'in künye kuralına tabidir: nereden bilindiği, hangi düzeyde, ne kadar yanlış olabileceği.

### 3. Kalıcı olarak dışarıda

1. **Canlı veya yakın-canlı konum.** Sivil bir geminin bulunduğu yer, rotası, tahmini varışı hiçbir biçimde yayımlanmaz — ne haritada, ne metinde, ne veri dosyasında.
2. **Mürettebat.** Ad, görev, uyruk, iletişim: hiçbiri ([0010](0010-content-safety-gates.md)).
3. **Tekil hedef gösterme.** "Şu gemi şunu taşıyor, durdurulmalı" biçiminde tek bir gemiye yönelen çağrı veya ima üretilmez. Bulgular **toplulaştırılmış** ve **kurumsal** düzeydedir.
4. **Küçük tekneler ve balıkçılar.** Ölçek eşiğinin altındaki tekneler hiçbir kayda girmez.
5. **Lisansı elvermeyen ticari AIS verisi** ([0009](0009-licensing.md)); MarineTraffic ve benzeri servislerin verisi yeniden yayımlanmaz.

### 4. Dil sınırı

İki istatistik arasındaki fark **"yönlendirme ölçüsü"** olarak yazılır; "kaçakçılık", "ihlal", "gizlice" gibi nitelemeler kaydın kendi sesiyle kurulmaz. Bir mekanizma iddiası varsa kaynağına atfedilir ([0019](0019-foreign-installations-register.md) §5).

Bir ortak ülkenin ihracat satırındaki büyüme, **rota değildir**: hiçbir mal bir istatistikten diğerine izlenmez ve her ekonomi kendi nedenleriyle büyür. Karşılaştırmanın söyleyebileceği tek şey, bir sonraki bakışın nereye yöneleceğidir.

### 5. Asimetri, bu kez tersine

[0019](0019-foreign-installations-register.md) başkalarının antlaşma yükümlülüklerini belgeler. Bu ADR, **kendi devletimizin kendi ilan ettiği politikayı** ölçer. İkisi birbirinin aynası değildir ve olmamalıdır: ilki dışarıya bakar, ikincisi kendimize. Bir açık kaynak topluluğunun kendi devletini ölçebileceği tek alan, o devletin **kendi beyanıdır** — ve bunu yapmak, dışarıyı ölçerken inandırıcı olmanın bedelidir.

Bu ADR, Türk kuvvetlerine ilişkin kırmızı çizgiye dokunmaz: konu sivil ticarettir, askerî hareket değil ([0013](0013-map-layers-turkiye-perspective.md)).

## Sonuçlar

- Proje ilk kez **kendi devletinin beyanını** ölçen bir seri yayımlar; rakamların ikisi de resmîdir, ikisi de tartışılmaz, aralarındaki fark okunabilirdir.
- Gemi takibi yapılmadığı için hiçbir mürettebat, hiçbir sivil gemi bu yüzden risk altına girmez; proje de silahlı çatışma hukuku bakımından sivil kalır.
- Bayrak değişikliği sorusu cevapsız kalmaz, yeri değişir: bayrak geçmişi bir **sicil kaydıdır** ve gecikmeli olarak kaydedilebilir; geminin nerede olduğu kaydedilmez.
- Risk dürüstçe: kendi devletinin politikasını ölçen bir seri, siyasi olarak rahatsız edici bulunabilir. Bunun karşılığı, dışarıyı ölçerken "siz de kendinize bakın" itirazına verilecek tek geçerli cevaptır.
