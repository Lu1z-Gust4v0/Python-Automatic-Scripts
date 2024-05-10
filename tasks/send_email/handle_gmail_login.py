import os

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_BUTTON_XPATH = "/html/body/header/div/div/div/a[2]"
EMAIL_INPUT_XPATH = "//*[@id='identifierId']"
EMAIL_BUTTON_CSS_SELECTOR = "button#identifierNext[name='action']"
PASSWORD_INPUT_CSS_SELECTOR = "input#password[name='Passwd']"
PASSWORD_BUTTON_CSS_SELECTOR = "button#passwordNext[name='action']"


def handle_gmail_login(browser: Chrome, waiter: WebDriverWait):
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LOGIN_PAGE_BUTTON_XPATH)
        )
    )

    login_button = browser.find_element(By.XPATH, LOGIN_PAGE_BUTTON_XPATH)
    login_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located((By.XPATH, EMAIL_INPUT_XPATH))
    )

    email_input = browser.find_element(By.XPATH, EMAIL_INPUT_XPATH)
    email_input.send_keys(os.getenv("GMAIL_EMAIL"))

    print("Email inserted successfully")

    email_button = browser.find_element(By.CSS_SELECTOR, EMAIL_BUTTON_CSS_SELECTOR)
    email_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, PASSWORD_INPUT_CSS_SELECTOR)
        )
    )

    password_input = browser.find_element(By.CSS_SELECTOR, PASSWORD_INPUT_CSS_SELECTOR)
    password_input.send_keys(os.getenv("GMAIL_PASSWORD"))

    print("Password inserted successfully")

    password_button = browser.find_element(
        By.CSS_SELECTOR, PASSWORD_BUTTON_CSS_SELECTOR
    )
    password_button.click()

    print("User logged successfully")
