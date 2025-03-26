import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixture 定義，用於管理 WebDriver 並在失敗時截圖
@pytest.fixture
def test_selenium_capture_debug(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # 檢查測試是否失敗
    if request.node.rep_call.failed:
        # 截圖並附加到 Allure 報告
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name=f"失敗截圖 - {request.node.name}",
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()


# 在 conftest.py 中啟用報告鉤子（若無此檔案需新增）
# conftest.py 內容見下方說明

@allure.severity(allure.severity_level.CRITICAL)
def test_allureReport_v1(test_selenium_capture_debug):
    driver = test_selenium_capture_debug
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//span[@class='vp-icon DocSearch-Search-Icon']")
    element.click()
    # 不需手動 quit，由 fixture 處理


@allure.severity(allure.severity_level.MINOR)
def test_allureReport_v2(test_selenium_capture_debug):
    driver = test_selenium_capture_debug
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Allure Report']")
    element.click()
    # 故意失敗的測試
    assert False, "故意失敗以測試截圖"
    # 不需手動 quit，由 fixture 處理


@allure.severity(allure.severity_level.BLOCKER)
def test_allureReport_v3():
    driver = webdriver.Chrome()
    driver.get("https://allurereport.org/")
    element = driver.find_element(by=By.XPATH, value="//a[@class='button primary']")
    element.click()
    driver.quit()