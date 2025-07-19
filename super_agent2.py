import pyautogui
import pyperclip
import time
import pygetwindow as gw
import subprocess
import datetime
import os

# Konumlar 1366x768 için
MSG_AREA_POS = (600, 550)
INPUT_BOX_POS = (600, 720)
ATTACH_BUTTON_POS = (1280, 720)

def find_chatgpt_window():
    for w in gw.getAllWindows():
        if 'ChatGPT' in w.title:
            try:
                w.activate()
                return w
            except:
                continue
    return None

def read_last_message():
    try:
        pyautogui.moveTo(MSG_AREA_POS)
        pyautogui.tripleClick()
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        return pyperclip.paste()
    except Exception as e:
        return f"read_error:{str(e)}"

def send_message(message):
    try:
        pyautogui.moveTo(INPUT_BOX_POS)
        pyautogui.click()
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.press('enter')
    except Exception as e:
        print("send_error:", e)

def upload_file_to_chatgpt(file_path):
    try:
        pyautogui.moveTo(ATTACH_BUTTON_POS)
        pyautogui.click()
        time.sleep(1)
        pyperclip.copy(os.path.abspath(file_path))
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        return "Screenshot uploaded."
    except Exception as e:
        return f"Upload error: {e}"

def run_command_from_text(text):
    try:
        text = text.lower()

        if "notepad" in text:
            subprocess.Popen("notepad.exe")
            return "Notepad launched"

        elif "chrome" in text:
            subprocess.Popen("chrome.exe")
            return "Chrome launched"

        elif "dosya sil" in text:
            if os.path.exists("test.txt"):
                os.remove("test.txt")
                return "test.txt deleted"
            else:
                return "test.txt not found"

        elif "ekran görüntüsü al" in text or "screenshot" in text:
            filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            pyautogui.screenshot(filename)
            return f"Screenshot saved as {filename}"

        elif "merhaba" in text:
            filename = "merhaba_screenshot.png"
            pyautogui.screenshot(filename)
            time.sleep(1)
            result = upload_file_to_chatgpt(filename)
            return result

        return "No known command matched."

    except Exception as e:
        return f"Error: {str(e)}"

def main_loop():
    last = ""
    print("Agent başlatıldı...")
    while True:
        win = find_chatgpt_window()
        if win:
            msg = read_last_message().strip()
            if msg.startswith("read_error:"):
                print(msg)
                time.sleep(5)
                continue
            if msg and msg != last:
                print("Yeni mesaj:", msg)
                result = run_command_from_text(msg)
                send_message(f"Uygulandı: {result}")
                last = msg
        else:
            print("ChatGPT sekmesi bulunamadı.")
        time.sleep(5)

if __name__ == "__main__":
    main_loop()
