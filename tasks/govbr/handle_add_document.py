from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

SIGN_DOCUMENT_PAGE_URL = "https://assinador.iti.br/assinatura/index.xhtml"
PAGE_TITLE_XPATH = "//h1[contains(text(), 'Assinatura de documento')]"
DROP_FILE_AREA_XPATH = "//*[@id='resultForm:uploadArquivo']"
FILE_INPUT_XPATH = "//*[@id='resultForm:uploadArquivo_input']"
SEND_FILE_BUTTON_XPATH = "//button[@type='submit']/span[contains(text(), 'Avançar')]"
SIGN_FILE_BUTTON_XPATH = "//button[@type='button']/span[contains(text(), 'Assinar')]"
CONFIRM_SIGN_BUTTON_XPATH = (
    '//*[@id="dlgAdicionarOutroDocumentoForm"]//span[contains(text(), "Assinar")]'
)


def handle_add_document(browser: Chrome, waiter: WebDriverWait, file_path: str):
    browser.get(SIGN_DOCUMENT_PAGE_URL)

    sleep(2)

    waiter.until(
        expected_conditions.visibility_of_element_located((By.XPATH, PAGE_TITLE_XPATH))
    )

    print("Sign page accessed successfully")
    # Simulate drag and drop event

    drop_file_area = browser.find_element(By.XPATH, DROP_FILE_AREA_XPATH)

    js_script = """
        var target = arguments[0];
        var filePath = arguments[1];
        var dataTransfer = new DataTransfer();
        var file = new File([filePath], "file.txt");
        dataTransfer.items.add(file);
        target.files = dataTransfer.files;
        target.dispatchEvent(new Event('change', { bubbles: true }));
    """

    browser.execute_script(js_script, drop_file_area, file_path)
    # file_input = browser.find_element(By.XPATH, FILE_INPUT_XPATH)
    # file_input.send_keys(file_path)

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, SEND_FILE_BUTTON_XPATH)
        )
    )

    send_file_button = browser.find_element(By.XPATH, SEND_FILE_BUTTON_XPATH)
    send_file_button.click()

    print("File uploaded successfully")

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, SIGN_FILE_BUTTON_XPATH)
        )
    )

    sign_file_button = browser.find_element(By.XPATH, SIGN_FILE_BUTTON_XPATH)
    sign_file_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, CONFIRM_SIGN_BUTTON_XPATH)
        )
    )

    confirm_sign_button = browser.find_element(By.XPATH, CONFIRM_SIGN_BUTTON_XPATH)
    confirm_sign_button.click()

    print("File entered the sign process successfully")
