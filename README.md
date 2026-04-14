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

# SABIS Grade Tracking Bot

Checking the SABIS system repeatedly during midterm and final periods to see if grades have been announced is a significant waste of time. This project is an automation script designed to eliminate the need for manual refreshes and provide instant notifications as soon as grades are posted.

## Features

The bot logs into the SABIS system at predefined intervals and scrapes grade cards. It compares current grades with the data from the previous check. If a new grade is entered or an existing one is updated, it sends an instant notification via Telegram.

## Tech Stack

* **Python & Selenium:** For automated login and data scraping.
* **GitHub Actions:** To run the bot in the cloud automatically every 30-45 minutes.
* **Telegram Bot API:** For sending real-time notifications.

## How to Use

You can use this bot to track your own grades. Your credentials remain completely private and secure, encrypted within GitHub Secrets.

1. **Fork** this repository to your own GitHub account.
2. Go to **Settings > Secrets and variables > Actions** in your forked repository.
3. Click on **New repository secret** and add the following 4 variables:
   * `SABIS_NO`: Your student number
   * `SABIS_SIFRE`: Your SABIS password
   * `TELEGRAM_TOKEN`: The bot token obtained from BotFather
   * `CHAT_ID`: Your Telegram Chat ID
4. Navigate to the **Actions** tab and click "I understand my workflows, go ahead and enable them" to activate the automation.
5. Select **SABIS Not Kontrol Botu** from the left sidebar and click **Run workflow** to start the bot manually for the first time.

After these steps, the bot will run automatically at set intervals and notify you via Telegram whenever a change is detected.
