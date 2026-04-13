# SABIS Not Takip Botu

Vize ve final dönemlerinde sürekli SABİS'e girip notların açıklanıp açıklanmadığını kontrol etmek ciddi bir zaman kaybı yaratıyor. Bu proje, sayfayı sürekli yenileme derdini bitirmek ve notlar girildiği an haberdar olmak için yazılmış bir otomasyon betiğidir.

## Ne Yapıyor?

Bot, belirlediğiniz aralıklarla arka planda SABİS'e giriş yapar ve not kartlarını okur. Mevcut notları bir önceki kontrolle karşılaştırır. Eğer sisteme yeni bir not girilmişse veya var olan bir not değiştirilmişse, size Telegram üzerinden anlık bir bildirim gönderir.

## Kullanılan Araçlar

* **Python & Selenium:** Sisteme giriş ve veri okuma işlemleri için.
* **GitHub Actions:** Botu bulutta (30 dakikada bir) otomatik çalıştırmak için.
* **Telegram Bot API:** Bildirimleri anlık olarak iletmek için.

## Kendi Hesabınızda Nasıl Kullanırsınız?

Bu botu kendi notlarınızı takip etmek için kullanabilirsiniz. Şifreleriniz GitHub Secrets altyapısı sayesinde tamamen gizli kalır ve kodun hiçbir yerinde görünmez.

1. Bu repoyu kendi GitHub hesabınıza **Fork**'layın.
2. Kendi deponuzda üst menüden **Settings > Secrets and variables > Actions** kısmına gidin.
3. **New repository secret** butonuna basarak aşağıdaki 4 veriyi tek tek ekleyin:
   * `SABIS_NO`: Öğrenci numaranız
   * `SABIS_SIFRE`: SABİS şifreniz
   * `TELEGRAM_TOKEN`: BotFather üzerinden oluşturduğunuz botun token'ı
   * `CHAT_ID`: Telegram Chat ID numaranız
4. Üst menüden **Actions** sekmesine gidin. "I understand my workflows, go ahead and enable them" butonuna basarak otomasyonu aktif edin.
5. Soldaki menüden **SABIS Not Kontrol Botu**'na tıklayıp **Run workflow** diyerek botu ilk kez manuel olarak başlatın.

Bu adımlardan sonra bot belirlediğiniz periyotlarda kendi kendine çalışacak ve bir değişiklik fark ettiğinde size Telegram'dan mesaj atacaktır.
