from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_IN_SECONDS = 30


def init_web_driver(arguments: list[str]):
    webdriver_options = webdriver.ChromeOptions()

    for argument in arguments:
        webdriver_options.add_argument(argument)

    browser = webdriver.Chrome(options=webdriver_options)
    waiter = WebDriverWait(browser, TIMEOUT_IN_SECONDS)

    return browser, waiter
