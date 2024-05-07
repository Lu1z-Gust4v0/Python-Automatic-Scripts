from selenium.webdriver import Chrome


def handle_page_access(browser: Chrome):
    browser.get("https://www.google.com/intl/pt-BR/gmail/about/")
    assert "Gmail" in browser.title

    print("Gmail accessed successfully")
