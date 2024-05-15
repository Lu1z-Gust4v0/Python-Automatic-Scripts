from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_TITLE_XPATH = "//*[@id='login-cpf']/h3"
LOGIN_PAGE_URL = "https://sso.acesso.gov.br/login"


def handle_page_access(browser: Chrome, waiter: WebDriverWait):
    browser.get(LOGIN_PAGE_URL)

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LOGIN_PAGE_TITLE_XPATH)
        )
    )
    print("Login page accessed successfully")
