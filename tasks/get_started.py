from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options)

print("Browsed initialized")

browser.get("http://www.yahoo.com")
assert "Yahoo" in browser.title

print("Page accessed successfully")

elem = browser.find_element(By.NAME, "p")  # Find the search box
elem.send_keys("seleniumhq" + Keys.RETURN)

browser.quit()
print("Quitting...")
