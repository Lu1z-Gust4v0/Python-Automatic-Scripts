from dotenv import load_dotenv
from handle_gmail_login import handle_gmail_login
from handle_send_email import handle_send_email
from page_access import handle_page_access

from tasks.utils import init_web_driver


def main():
    load_dotenv()

    browser, waiter = init_web_driver([])

    print("Browsed initialized successfully")

    handle_page_access(browser)

    handle_gmail_login(browser, waiter)

    handle_send_email(browser, waiter)

    print("Task finished successfully")


main()
