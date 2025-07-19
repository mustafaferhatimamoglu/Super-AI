import pyautogui
import pyperclip
import time
import pygetwindow as gw
import subprocess
import datetime
import os

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
    pyautogui.moveTo(600, 600)
    pyautogui.tripleClick()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    return pyperclip.paste()

def send_message(message):
    pyautogui.moveTo(600, 950)
    pyautogui.click()
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')

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
