import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main(message: str):
    """Open ChatGPT in a browser, send a message and print the response."""
    driver = webdriver.Chrome()
    driver.get("https://chat.openai.com")

    input("\nPlease log in to ChatGPT if needed, then press Enter to continue...")

    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(message + Keys.ENTER)

    # Wait for ChatGPT to respond
    time.sleep(5)
    responses = driver.find_elements(By.CSS_SELECTOR, ".markdown")
    if responses:
        print("ChatGPT response:\n")
        print(responses[-1].text)

    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to ChatGPT via Selenium")
    parser.add_argument("message", help="Message to send")
    args = parser.parse_args()
    main(args.message)
