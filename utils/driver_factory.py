import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()

    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    return driver

