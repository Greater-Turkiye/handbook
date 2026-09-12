# 04 · Operasyonel Güvenlik (OPSEC)

Bu sayfa **sizi** korumak içindir. Açık kaynak savunma analizi; devlet aktörlerinin, trol ağlarının ve kötü niyetli kişilerin ilgisini çekebilen bir alandır. Aşağıdaki önlemler ücretsizdir ve çoğu bir kerelik ayardır.

## 1. Takma ad anonimlik değildir

- Takma adla katkı vermek serbesttir ve desteklenir. Kimliğinizi kimseye açıklamak zorunda değilsiniz — bakımcılara da.
- Ama bilin: **GitHub, Telegram, Bluesky ve diğer platformlar yasal taleplere uyar.** IP adresi, e-posta, telefon numarası, ödeme bilgisi gibi kayıtlar talep hâlinde paylaşılabilir.
- Takma ad; iş arkadaşlarınızın, trollerin veya meraklıların sizi kolayca bulmasını zorlaştırır. Devlet düzeyinde bir hasma karşı koruma **sağlamaz**.
- Bu nedenle en iyi OPSEC, **kuralları çiğnememektir**: Kırmızı çizgilere uyan bir katkının saklanacak bir tarafı yoktur.

### Takma ad hijyeni
- Takma adınızı başka hiçbir yerde (oyun hesapları, forumlar, eski sosyal medya) kullanmadığınız yeni bir ad olarak seçin.
- Profil fotoğrafı olarak kendi fotoğrafınızı veya ters görsel aramayla bulunabilecek bir görseli kullanmayın.
- Yazım alışkanlıkları, çalışma saatleri, şehrinizden bahsetmek, "bizim buradaki üs" gibi ifadeler sizi ele verebilir.
- Gerçek kimlikli hesaplarınızla takma ad hesabınız arasında takip, beğeni, etiketleme gibi bağlar kurmayın.

## 2. GitHub e-posta gizliliği

GitHub → **Settings → Emails**:
1. **"Keep my email addresses private"** seçeneğini açın. GitHub size `ID+kullanıcıadı@users.noreply.github.com` biçiminde bir adres verir.
2. **"Block command line pushes that expose my email"** seçeneğini açın. Böylece yanlışlıkla gerçek e-postanızla yapılan commit'ler reddedilir.
3. Yerel git'i bu adresle yapılandırın:

```bash
git config --global user.name "takma-adiniz"
git config --global user.email "12345678+takma-adiniz@users.noreply.github.com"
```

Daha önce gerçek e-postanızla commit yaptıysanız, o commit'ler herkese açık kalır; yeni ve temiz bir hesap açmayı düşünün.

## 3. Commit'lerde saat dilimi

Git, her commit'e **yerel saat dilimi farkınızı** (ör. `+0300`) yazar. Bu, bulunduğunuz bölgeyi ele verebilir. Commit'lerinizi UTC ile yapın:

```bash
# Bash / Git Bash / macOS / Linux
TZ=UTC git commit -m "evt: ..."

# Kalıcı yapmak için (bash)
alias git='TZ=UTC git'
```

```powershell
# PowerShell (oturum boyunca)
$env:TZ = "UTC"
git commit -m "evt: ..."
```

Kontrol: `git log -1 --format="%ad"` çıktısında `+0000` görmelisiniz. Web arayüzünden yapılan commit'ler için bu sorun genellikle GitHub tarafında ele alınır, ama emin değilseniz yerelden UTC ile çalışın.

## 4. Cihaz ve ağ

- **İş yerinin veya devlet kurumunun cihazlarını ve ağlarını ASLA kullanmayın.** Bu cihazlar izlenebilir, kayıt tutulabilir; ayrıca bir kamu görevlisiyseniz çıkar çatışması ve disiplin sorunları doğabilir.
- Kişisel cihazınızın işletim sistemini ve tarayıcısını güncel tutun.
- Topluluk işleri için ayrı bir tarayıcı profili kullanın (takma ad hesaplarınız yalnızca orada oturum açık olsun).
- Halka açık Wi-Fi ağlarında dikkatli olun. VPN veya Tor kullanmak sizin tercihinizdir; kullanımlarının yasal olup olmadığını bulunduğunuz ülkede kontrol edin. Unutmayın: Tor/VPN, hesabınıza giriş yaptığınız anda platform karşısında sizi anonim yapmaz.

## 5. Meta veri temizliği

Topluluğa hiçbir medya dosyası (fotoğraf, video) **commit edilmez** ([06](06-sourcing-archiving.md)). Yine de bir görseli bakımcılara özelden göndermeniz, bir sorun kaydına ekran görüntüsü eklemeniz gerekebilir:

- Fotoğraflarda **EXIF** verisi (GPS konumu, cihaz modeli, çekim zamanı) bulunabilir. Paylaşmadan önce silin (ör. `exiftool -all= dosya.jpg`) veya ekran görüntüsü alarak yeni bir dosya oluşturun.
- PDF ve Office belgelerinde yazar adı, kurum adı, düzenleme geçmişi bulunabilir.
- Ekran görüntülerinde; tarayıcı sekmeleri, yer imleri, bildirimler, kullanıcı adınız, saat ve dil ayarlarınız görünmesin.
- GitHub'a yüklenen görsellerin EXIF'i genellikle temizlenir, ama buna güvenmeyin.

## 6. Hedeflerle etkileşim yok

- Sahte hesaplarla (sock-puppet) izlenen kişi, kanal veya gruplarla **etkileşime girmeyin**: mesaj atmayın, soru sormayın, kapalı gruplara katılmayın, tartışmaya girmeyin.
- Pasif gözlem: yalnızca kamuya açık olanı okuyun. Telegram kanallarını mümkün olduğunca **açık web önizlemesi** üzerinden izleyin (`t.me/s/kanaladi`).
- Kanal sahipleri, kanal üye listelerini görebilir; gerçek telefon numaranızla hesap açtıysanız numaranızı gizli tutun (Telegram → Gizlilik → Telefon numarası: Hiç kimse).
- Kışkırtıcı içeriğe cevap vermeyin; ekran görüntüsü alıp arşivleyin, gerisini bakımcılara bırakın.

## 7. Hesap güvenliği

- **İki aşamalı doğrulama (2FA) zorunludur.** Organizasyon, 2FA'sı olmayan üyeleri kabul etmez.
- Tercih sırası: **passkey / donanım anahtarı** → **TOTP uygulaması** (Aegis, 2FAS, Ente Auth vb.) → SMS (önerilmez; SIM değiştirme saldırılarına açıktır).
- **Kurtarma kodlarını** yazdırın veya çevrimdışı saklayın (şifreli bir USB, kâğıt). Bulut not uygulamasında düz metin olarak saklamayın.
- Her hizmet için benzersiz, uzun parolalar ve bir parola yöneticisi kullanın.
- Takma ad hesabınızın kurtarma e-postası, gerçek kimliğinize bağlı bir adres olmasın — ama erişiminizi kaybetmeyeceğiniz bir adres olsun.
- Yetkili rollerde (triager, reviewer, maintainer) GitHub oturumlarınızı ve yetkilendirdiğiniz OAuth uygulamalarını düzenli olarak gözden geçirin.

## 8. Kötü niyetli bağlantı ve dosyalar

Bu alanda çalışan kişiler, **oltalama ve kötü amaçlı yazılım** hedefidir. "Sızdırılmış belge", "özel görüntü", "kanıt dosyası" en klasik yemdir.

- Tanımadığınız kişilerden gelen dosyaları açmayın. Özellikle `.docx`, `.xlsm`, `.pdf`, `.zip`, `.rar`, `.iso`, `.lnk`, `.apk`.
- Açmanız gerçekten gerekiyorsa: **sanal makine (VM)** veya tek kullanımlık bir ortam (ör. Windows Sandbox) kullanın, ağ bağlantısını kesin.
- Bağlantıları tıklamadan önce gerçek adresini kontrol edin; kısaltılmış bağlantıları açmayın (kaynak olarak da kabul etmiyoruz).
- "GitHub hesabınız askıya alınacak", "Telegram doğrulama kodu" gibi aciliyet kokan mesajlar genellikle oltalamadır.
- Bir PR veya sorun kaydı içinde çalıştırılabilir kod, betik veya ikili dosya varsa **çalıştırmayın**; bakımcılara bildirin.

## 9. Hassas konular için özel kanal

Bazı şeyler herkese açık bir sorun kaydında veya PR'da **konuşulmamalıdır**:

- Kırmızı çizgi ihlali fark etmek,
- Size gizli/sızdırılmış materyal gönderilmesi,
- Taciz, tehdit, kimliğinizin açığa çıkması,
- Bir hesabın ele geçirildiğinden şüphelenmek,
- Güvenlik açığı bildirmek.

Bunlar için [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) dosyasındaki özel iletişim adresini kullanın. **GitHub'da açılan PR'lar ve sorun kayıtları anında herkese açıktır** — silinseler bile önbelleklerde ve bildirim e-postalarında kalabilirler.

## 10. Taciz ve tehdit durumunda

- Karşılık vermeyin, tartışmayın. Ekran görüntüsü ve arşiv bağlantısıyla kayıt altına alın.
- Bakımcılara özel kanaldan bildirin; platformun bildirim mekanizmasını kullanın.
- Fiziksel güvenliğinize dair bir tehdit varsa kolluk kuvvetlerine başvurun. Topluluk sizi korumak için gereken her şeyi (hesabınızı gizleme, katkılarınızın atfını düzenleme vb.) yapar.
- Bir süre ara vermek her zaman meşru bir seçenektir.

## Özet kontrol listesi

- [ ] Yeni, bağımsız bir takma ad
- [ ] "Keep my email addresses private" + "Block command line pushes that expose my email"
- [ ] `user.email` = noreply adresi
- [ ] Commit'ler UTC (`+0000`)
- [ ] İş/devlet cihazı veya ağı kullanılmıyor
- [ ] 2FA (passkey/TOTP) + çevrimdışı kurtarma kodları
- [ ] Medya dosyalarında meta veri temizliği
- [ ] Hedeflerle etkileşim yok
- [ ] Şüpheli dosyalar yalnızca VM/sandbox'ta
- [ ] Hassas konular yalnızca özel kanaldan
