import pytesseract
import pyautogui
from PIL import Image
import time

# Tesseract yolu
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 1. Ekran görüntüsü al
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")

# 2. OCR ile analiz
data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

# 3. "Yeni" kelimesini bul ve tıkla
found = False
for i in range(len(data['text'])):
    if "Olustur" in data['text'][i]:  # Dilersen "Compose" ya da "New" de olabilir
        x = data['left'][i] + data['width'][i] // 2
        y = data['top'][i] + data['height'][i] // 2
        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.click()
        print(f"[✓] 'Olustur' butonuna tıklandı: ({x}, {y})")
        found = True
        break

if not found:
    print("[!] 'Olustur' butonu bulunamadı. Ekran çözünürlüğü, dil veya tema farkı olabilir.")
