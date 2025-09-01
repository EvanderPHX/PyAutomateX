# Placeholder for UI automation examples using Selenium
from selenium import webdriver

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    print(driver.title)
    driver.quit()
