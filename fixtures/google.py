from selenium.webdriver.common.by import By

def test_google(setup_and_teardown):
    driver = setup_and_teardown
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    # ✅ 使用更穩定的方式尋找 Google 搜尋框
    input_element = driver.find_element(by=By.ID, value="APjFqb")
    input_element.click()
    input_element.send_keys("selenium python")

def test_googlesearch(setup_and_teardown):
    driver = setup_and_teardown
    driver.get("https://playwright.dev/docs/accessibility-testing")


