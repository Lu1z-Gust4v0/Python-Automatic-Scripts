import os

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_BUTTON_XPATH = "/html/body/header/div/div/div/a[2]"
EMAIL_INPUT_XPATH = "//*[@id='identifierId']"
EMAIL_BUTTON_XPATH = "//*[@id='identifierNext']/div/button"
PASSWORD_INPUT_XPATH = "//*[@id='password']/div[1]/div/div[1]/input"
PASSWORD_BUTTON_XPATH = "//*[@id='passwordNext']/div/button"


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

    email_button = browser.find_element(By.XPATH, EMAIL_BUTTON_XPATH)
    email_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, PASSWORD_INPUT_XPATH)
        )
    )

    password_input = browser.find_element(By.XPATH, PASSWORD_INPUT_XPATH)
    password_input.send_keys(os.getenv("GMAIL_PASSWORD"))

    print("Password inserted successfully")

    password_button = browser.find_element(By.XPATH, PASSWORD_BUTTON_XPATH)
    password_button.click()

    print("User logged successfully")
