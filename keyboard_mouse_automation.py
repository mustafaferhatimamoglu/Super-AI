"""Demonstrate basic keyboard and mouse automation using ``pyautogui``.

Run ``python -m py_compile keyboard_mouse_automation.py`` to validate the
script before executing it.
"""

import pyautogui
import time

# Simple example script demonstrating step-by-step keyboard and mouse
# automation. Adjust the coordinates and text as needed for your system.

def main():
    print("Starting automation in 3 seconds...")
    time.sleep(3)

    # Step 1: move mouse to a specific position
    pyautogui.moveTo(200, 200, duration=1)

    # Step 2: left click
    pyautogui.click()

    # Step 3: type some text
    pyautogui.write("Hello from automation", interval=0.1)
    pyautogui.press("enter")

if __name__ == "__main__":
    main()
