"""Submit text prompts to the Sora interface automatically.

The script reads ``.txt`` files from the ``prompts/`` folder and types each
prompt into the Sora web interface using ``pyautogui``. Processed files are
moved to ``prompts/processed/`` so they are not submitted twice.

Run ``python -m py_compile super_ai_agent.py`` before executing to catch
syntax errors early.
"""

from __future__ import annotations

import argparse
import os
import shutil
import time

try:
    import pyautogui
except Exception as exc:  # pragma: no cover - environment may lack GUI
    raise SystemExit(
        "pyautogui is required. Install it with `pip install pyautogui`."
    ) from exc

PROMPT_FOLDER = "prompts"
WAIT_AFTER_EACH_STEP = 1  # seconds

def find_browser_input_box(wait: float) -> None:
    """Try to focus the Sora text input box.

    This approach is simplistic and may need adjustments depending on the
    browser window layout.
    """

    pyautogui.hotkey("ctrl", "l")  # Go to address bar
    pyautogui.press("tab", presses=5, interval=0.3)  # Navigate to input box
    pyautogui.press("enter")  # Focus input
    time.sleep(wait)

def submit_prompt(prompt_text: str, wait: float) -> None:
    """Type ``prompt_text`` into the active input box and submit."""

    pyautogui.write(prompt_text, interval=0.01)
    pyautogui.press("enter")
    time.sleep(wait)

def main() -> None:
    """Entry point for the automation script."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prompt-folder",
        default=PROMPT_FOLDER,
        help="Directory containing .txt prompts",
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Keep watching for new prompt files",
    )
    parser.add_argument(
        "--wait",
        type=float,
        default=WAIT_AFTER_EACH_STEP,
        help="Seconds to wait after each automation step",
    )
    args = parser.parse_args()

    prompt_folder = args.prompt_folder
    processed_dir = os.path.join(prompt_folder, "processed")
    os.makedirs(processed_dir, exist_ok=True)

    print("🧠 Super-AI Agent started.")

    while True:
        for filename in sorted(os.listdir(prompt_folder)):
            if not filename.endswith(".txt"):
                continue
            src = os.path.join(prompt_folder, filename)
            dst = os.path.join(processed_dir, filename)
            if os.path.exists(dst):
                continue

            with open(src, "r", encoding="utf-8") as f:
                prompt_text = f.read().strip()

            print(f"🚀 Submitting: {filename}")
            find_browser_input_box(args.wait)
            submit_prompt(prompt_text, args.wait)

            shutil.move(src, dst)
            time.sleep(5)

        if not args.loop:
            break
        time.sleep(10)

if __name__ == "__main__":
    main()
