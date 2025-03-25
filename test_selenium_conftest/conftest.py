import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()