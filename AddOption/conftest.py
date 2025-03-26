import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform")


@pytest.fixture()
def setup_teardown(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "fire":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Browser is not define")

    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

