from selenium.webdriver.common.by import By

def test_rosemaryBrown(setup_and_teardown):
    driver = setup_and_teardown
    driver.get("https://www.burnaby.ca/recreation-and-arts/recreation-facilities/rosemary-brown-recreation-centre")
    driver.maximize_window()
    assert "Rosemary Brown Recreation Centre | City of Burnaby" in driver.title

    button = driver.find_element(by=By.XPATH, value="//nav[@id='block-main-menu']//a[normalize-space()='Services & Payments']")
    button.click()


