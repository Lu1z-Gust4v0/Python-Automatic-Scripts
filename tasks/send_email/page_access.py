from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

GMAIL_PATH_URL = "https://www.google.com/intl/pt-BR/gmail/about/"


def handle_page_access(browser: Chrome, waiter: WebDriverWait):
    browser.get(GMAIL_PATH_URL)

    waiter.until(expected_conditions.url_to_be(GMAIL_PATH_URL))
    assert "Gmail" in browser.title

    print("Gmail accessed successfully")
