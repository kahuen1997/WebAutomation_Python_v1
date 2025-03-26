import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.regression
def test_seleniumbasic_v1(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.w3schools.com/spaces/index.php")
    element = driver.find_element(by=By.XPATH, value="//a[@title='HTML Tutorial'][normalize-space()='HTML']")
    # 用 ActionChains 實現懸停
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _: element.is_displayed())
    element.click()
    time.sleep(3)

@pytest.mark.regression
def test_seleniumbasic_v2(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.selenium.dev/documentation/webdriver/waits/")
    element = driver.find_element(by=By.CSS_SELECTOR, value="#tabs-03-04-tab")
    assert element.is_displayed()
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    time.sleep(3)


