import os
from time import sleep

from selenium.webdriver import ActionChains, Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

WRITE_EMAIL_BUTTON_XPATH = (
    "/html/body/div[8]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div"
)

SEND_EMAIL_DIALOG_CSS_SELECTOR = "div.nH.Hd[role='dialog']"
RECIPIENT_INPUT_CSS_SELECTOR = "input.agP.aFw[aria-label='Destinatários']"
SUBJECT_INPUT_CSS_SELECTOR = "input.aoT[aria-label='Assunto']"
BODY_INPUT_CSS_SELECTOR = "div[role='textbox'][aria-label='Corpo da mensagem']"


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

    sleep(5)

    print("Email sent successfully")
