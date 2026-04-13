import os
import time 
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
ID = os.environ.get("CHAT_ID")
NO = os.environ.get("SABIS_NO")
SIFRE = os.environ.get("SABIS_SIFRE")

def telegram_mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={mesaj}"
    requests.get(url)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("Sisteme giriş yapılıyor...")
    driver.get("https://sabis.sakarya.edu.tr")
    time.sleep(2)
    
    driver.find_element(By.ID, "UserName").send_keys(NO)
    driver.find_element(By.ID, "Password").send_keys(SIFRE)
    driver.find_element(By.ID, "btnLogin").click() 
    time.sleep(3)
    
    print("Notlar sayfasına yönleniliyor...")
    driver.get("https://obs.sabis.sakarya.edu.tr/Ders")
    time.sleep(3)

    if len(driver.find_elements(By.ID, "Username")) > 0:
        driver.find_element(By.ID, "Username").send_keys(NO)
        sifre_alani = driver.find_element(By.ID, "Password")
        sifre_alani.send_keys(SIFRE)
        sifre_alani.send_keys(Keys.ENTER) 
        time.sleep(3)

    print("Ders kartları okunuyor...")
    kartlar = driver.find_elements(By.CLASS_NAME, "card-body") 
    
    guncel_not_verisi = ""
    for kart in kartlar:
        guncel_not_verisi += kart.text + "\n---\n" 
        
    print(f"Toplam {len(kartlar)} adet ders kartı bulundu.")

    dosya_adi = "sabis_hafiza.txt"
    eski_not_verisi = ""
    
    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            eski_not_verisi = dosya.read()

    if guncel_not_verisi == "":
        print("Hata: Notlar okunamadı, sayfa yüklenmemiş olabilir.")
    elif guncel_not_verisi != eski_not_verisi:
        print("DEĞİŞİKLİK VAR! Yeni veriler hafızaya yazılıyor...")
        telegram_mesaj_gonder("🚨 SABİS'te bir hareketlilik var! Notlarından biri girilmiş veya güncellenmiş olabilir. Hemen kontrol et!")
        
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write(guncel_not_verisi)
    else:
        print("Değişiklik yok. Kimse not girmemiş, beklemeye devam...")

except Exception as e:
    print(f"Hata oluştu: {e}")
    telegram_mesaj_gonder("SABİS botu çalışırken bir hata oluştu, kontrol etmen gerekebilir.")

finally:
    driver.quit()