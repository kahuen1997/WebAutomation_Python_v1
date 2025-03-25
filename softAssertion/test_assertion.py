import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#加左soft assertion package之後hard assertion就會變soft
def test_assert():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    assert driver.find_element(by=By.ID,value="APjFqb").is_displayed() #Assertion
    assert "XRX" in driver.title # Assertion
    time.sleep(5)
    driver.quit()

