import math
import random

from PIL import Image
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_IN_SECONDS = 30


def init_web_driver(arguments: list[str]):
    webdriver_options = webdriver.ChromeOptions()

    for argument in arguments:
        webdriver_options.add_argument(argument)

    browser = webdriver.Chrome(options=webdriver_options)
    waiter = WebDriverWait(browser, TIMEOUT_IN_SECONDS)

    return browser, waiter


def save_page(browser: Chrome, open_screenshot=False):
    page_id = math.floor(random.random() * 100)

    browser.save_screenshot(f"saved_page_{page_id}.png")

    if open_screenshot:
        screenshot = Image.open(f"saved_page_{page_id}.png")
        screenshot.show()

    with open(f"saved_page_{page_id}.html", "w", encoding="utf-8") as file:
        file.write(browser.page_source)
