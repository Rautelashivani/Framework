import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService




@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=1520,820")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    time.sleep(10)
    driver.quit()
