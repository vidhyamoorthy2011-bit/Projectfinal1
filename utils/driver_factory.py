from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.common import WebDriverException


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)


    driver = webdriver.Chrome(options=options)
    return driver