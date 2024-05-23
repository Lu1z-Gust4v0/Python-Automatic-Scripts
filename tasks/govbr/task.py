from dotenv import load_dotenv
from handle_add_document import handle_add_document
from handle_govbr_login import handle_govbr_login
from handle_page_access import handle_page_access

from tasks.utils import init_web_driver


def main():
    load_dotenv()

    # file_path = input("Enter the file path of the document you want to sign: ").strip()

    browser, waiter = init_web_driver([], undetected=True)

    print("Browser initiated sucessfully")

    handle_page_access(browser, waiter)

    handle_govbr_login(browser, waiter)

    handle_add_document(
        browser,
        waiter,
        "/home/gustavo/projects/python/tests/bots/sign_this_document.pdf",
    )


main()
