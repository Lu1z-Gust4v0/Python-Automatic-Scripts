import os

from dotenv import load_dotenv
from selenium.webdriver import ActionChains, Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utils import init_web_driver

LOGIN_PAGE_BUTTON_XPATH = "/html/body/header/div/div/div/a[2]"
EMAIL_INPUT_XPATH = "//*[@id='identifierId']"
EMAIL_BUTTON_XPATH = "//*[@id='identifierNext']/div/button"
PASSWORD_INPUT_XPATH = "//*[@id='password']/div[1]/div/div[1]/input"
PASSWORD_BUTTON_XPATH = "//*[@id='passwordNext']/div/button"

WRITE_EMAIL_BUTTON_XPATH = (
    "/html/body/div[8]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div"
)

SEND_EMAIL_DIALOG_CSS_SELECTOR = "div.nH.Hd[role='dialog']"
RECIPIENT_INPUT_CSS_SELECTOR = "input.agP.aFw[aria-label='Destinatários']"
SUBJECT_INPUT_CSS_SELECTOR = "input.aoT[aria-label='Assunto']"
BODY_INPUT_CSS_SELECTOR = "div[role='textbox'][aria-label='Corpo da mensagem']"


RECIPIENT_INPUT_XPATH = "//*[@id=':ui']"
SUBJECT_INPUT_XPATH = "//*[@id=':p4']"
BODY_INPUT_XPATH = "//*[@id='qd']"
SEND_EMAIL_BUTTON_XPATH = "//*[@id=':mg']"


def handle_page_access(browser: Chrome):
    browser.get("https://www.google.com/intl/pt-BR/gmail/about/")
    assert "Gmail" in browser.title

    print("Gmail accessed successfully")


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


def handle_send_email(browser: Chrome, waiter: WebDriverWait):
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, WRITE_EMAIL_BUTTON_XPATH)
        )
    )

    write_email_button = browser.find_element(By.XPATH, WRITE_EMAIL_BUTTON_XPATH)
    write_email_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, SEND_EMAIL_DIALOG_CSS_SELECTOR)
        )
    )

    email_dialog = browser.find_element(By.CSS_SELECTOR, SEND_EMAIL_DIALOG_CSS_SELECTOR)

    recipient_input = email_dialog.find_element(
        By.CSS_SELECTOR, RECIPIENT_INPUT_CSS_SELECTOR
    )
    recipient_input.send_keys(os.getenv("EMAIL_RECIPIENT"))

    print("Email recipient filled")

    subject_input = email_dialog.find_element(
        By.CSS_SELECTOR, SUBJECT_INPUT_CSS_SELECTOR
    )
    subject_input.send_keys(os.getenv("EMAIL_SUBJECT"))

    print("Email subject filled")

    body_input = email_dialog.find_element(By.CSS_SELECTOR, BODY_INPUT_CSS_SELECTOR)
    body_input.send_keys(os.getenv("EMAIL_BODY"))

    print("Email body filled")

    ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()

    print("Email sent successfully")


def main():
    load_dotenv()

    browser, waiter = init_web_driver([])

    print("Browsed initialized successfully")

    handle_page_access(browser)

    handle_gmail_login(browser, waiter)

    handle_send_email(browser, waiter)

    print("Task finished successfully")


main()
