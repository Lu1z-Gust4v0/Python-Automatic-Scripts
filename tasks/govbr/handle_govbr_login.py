import os
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

CPF_INPUT_XPATH = '//*[@id="accountId"]'
CONTINUE_BUTTON_XPATH = '//*[@id="enter-account-id"]'
PASSWORD_INPUT_XPATH = '//*[@id="password"]'
ENTER_BUTTON_XPATH = '//*[@id="submit-button"]'


def handle_govbr_login(browser: Chrome, waiter: WebDriverWait):
    cpf_input = browser.find_element(By.XPATH, CPF_INPUT_XPATH)
    cpf_input.send_keys(os.getenv("CPF"))

    sleep(2)

    continue_button = browser.find_element(By.XPATH, CONTINUE_BUTTON_XPATH)
    continue_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, PASSWORD_INPUT_XPATH)
        )
    )

    password_input = browser.find_element(By.XPATH, PASSWORD_INPUT_XPATH)
    password_input.send_keys(os.getenv("GOVBR_PASSWORD"))

    sleep(2)

    enter_button = browser.find_element(By.XPATH, ENTER_BUTTON_XPATH)
    enter_button.click()

    print("Logged successfully")

    sleep(2)
