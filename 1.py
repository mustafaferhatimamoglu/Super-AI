import subprocess
import sys
import os
import time
from datetime import datetime

# 🧠 Paket yükleme
def install():
    try:
        import pytesseract
        import pyautogui
        from PIL import Image
    except ImportError:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytesseract", "pyautogui", "pillow"])

install()

import pytesseract
import pyautogui
from PIL import Image

# 🧠 Tesseract yolunu ayarla (Windows için)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # ← Gerekirse ayarla

mail_list = {
    "Martı": "support@marti.tech",
    "Uber": "support@uber.com"
}

subject = "Yeni İş Birliği Önerisi – Kendi Aracınızla Eve Bırakılma"
body = """Merhaba {company} Ekibi,

Yeni bir hizmet modeli öneriyoruz: müşterileriniz, kendi araçlarıyla bir görevli tarafından güvenli şekilde evlerine bırakılabilir.

Bu model, hem gece ulaşım sorunlarına çözüm sunar hem de sizin hizmet ağınızı genişletir.

Detaylı görüşme için iletişime geçmenizi bekliyoruz.

Saygılarımızla,  
DriveWitness
"""

def log_step(step):
    print(f"[Super-AI] ✅ {step}")
    # Buraya JSON veya webhook log eklenebilir (isteğe bağlı)

def screenshot_and_ocr(region=None):
    screenshot = pyautogui.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot, lang='tur+eng')
    return text, screenshot

def find_button(target_word):
    log_step("Ekran taranıyor, OCR başlıyor...")
    screen = pyautogui.screenshot()
    width, height = screen.size

    step = 50
    for x in range(0, width, step):
        for y in range(0, height, step):
            region = (x, y, step, step)
            text, img = screenshot_and_ocr(region)
            if target_word.lower() in text.lower():
                pyautogui.moveTo(x + step // 2, y + step // 2)
                pyautogui.click()
                log_step(f'"{target_word}" butonu bulundu ve tıklandı.')
                return True
    print("❌ Buton bulunamadı.")
    return False

def type_email_fields(to, company):
    time.sleep(1)
    pyautogui.write(to)
    pyautogui.press('tab')
    pyautogui.write(subject)
    pyautogui.press('tab')
    pyautogui.write(body.format(company=company))
    log_step(f"{company} e-postası hazırlandı.")

def send_email():
    pyautogui.hotkey('ctrl', 'enter')
    log_step("E-posta gönderildi.")

def activate_chrome():
    pyautogui.hotkey('alt', 'tab')
    log_step("Chrome aktif hale getirildi.")

def run_all():
    activate_chrome()
    for company, to in mail_list.items():
        log_step(f"{company} için işlem başlıyor...")
        success = find_button("Yeni") or find_button("Compose")
        if not success:
            log_step("Buton bulunamadı, işlem atlandı.")
            continue
        time.sleep(1)
        type_email_fields(to, company)
        time.sleep(1)
        send_email()

run_all()
