import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/documentation/webdriver/waits/")

linkclick = driver.find_element(by=By.XPATH, value="//a[@href='https://www.selenium.dev/documentation/']")
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _: linkclick.is_displayed())
linkclick.click()
time.sleep(3)

driver.quit()
