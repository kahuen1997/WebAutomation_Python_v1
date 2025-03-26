from selenium.webdriver.common.by import By

def test_seleniumbasic_v3(setup_teardown):
    driver = setup_teardown
    driver.get("https://getbootstrap.com/docs/4.0/examples/")
    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Documentation']")
    element.click()
    introelement = driver.find_element(by=By.XPATH,value="//h1[@id='content']")
    assert introelement.is_displayed()


