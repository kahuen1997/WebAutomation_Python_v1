import webbrowser

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.CRITICAL)
def test_allureReport_v1():
    driver = webdriver.Chrome()
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//span[@class='vp-icon DocSearch-Search-Icon']")
    element.click()
    driver.quit()

@allure.severity(allure.severity_level.MINOR)
def test_allureReport_v2():
    driver = webdriver.Chrome()
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Allure Report']")
    element.click()
    driver.quit()

@allure.severity(allure.severity_level.BLOCKER)
def test_allureReport_v3():
    driver = webdriver.Chrome()
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//a[@class='button primary']")
    element.click()
    driver.quit()
