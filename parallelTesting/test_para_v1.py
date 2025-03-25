import time

from selenium import webdriver

def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.selenium.dev/documentation/webdriver/")

    time.sleep(5)
    driver.quit()

def test_two():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/maps")

    time.sleep(5)
    driver.quit()

def test_three():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.timeanddate.com/date/duration.html")

    time.sleep(5)
    driver.quit()

def test_four():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com/watch?v=ocDo3ySyHSI&list=PL1-3rA_ZNvo00TiphZm4aW2TNTjo5arc1")

    time.sleep(5)
    driver.quit()

def test_five():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://grok.com/chat/10046935-718f-4189-9261-453b1e7cb9cd")

    time.sleep(5)
    driver.quit()