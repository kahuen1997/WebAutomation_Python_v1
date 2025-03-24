import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_teardown():
    service = Service(executable_path="../chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    time.sleep(5)
    driver.quit()


