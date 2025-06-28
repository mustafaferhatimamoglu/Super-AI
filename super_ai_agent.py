import pyautogui
import time
import os

PROMPT_FOLDER = "prompts"
WAIT_AFTER_EACH_STEP = 1  # seconds

def find_browser_input_box():
    # Not robust, replace with image-based detection later
    pyautogui.hotkey("ctrl", "l")  # Go to address bar
    pyautogui.press("tab", presses=5, interval=0.3)  # Navigate down to Sora input box
    pyautogui.press("enter")  # Focus input
    time.sleep(WAIT_AFTER_EACH_STEP)

def submit_prompt(prompt_text):
    pyautogui.write(prompt_text, interval=0.01)
    pyautogui.press("enter")
    time.sleep(WAIT_AFTER_EACH_STEP)

def main():
    print("🧠 Super-AI Agent started.")
    processed = set()

    while True:
        for filename in os.listdir(PROMPT_FOLDER):
            if not filename.endswith(".txt"):
                continue
            if filename in processed:
                continue

            with open(os.path.join(PROMPT_FOLDER, filename), "r", encoding="utf-8") as f:
                prompt_text = f.read().strip()

            print(f"🚀 Submitting: {filename}")
            find_browser_input_box()
            submit_prompt(prompt_text)

            processed.add(filename)
            time.sleep(5)

        time.sleep(10)

if __name__ == "__main__":
    main()
