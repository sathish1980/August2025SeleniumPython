import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("Get_URL")
def test_lauchGoogle(Get_URL):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(Get_URL)
    browser.find_element(by=By.XPATH,value="//*[@jsname='yZiJbe']").send_keys("The hindu")
    keyboradactions= ActionChains(browser)
    keyboradactions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(4)
    frameidentified = False
    allFrames = browser.find_elements(by=By.TAG_NAME, value="iframe")
    print(len(allFrames))
    for eachvalue in range(0, len(allFrames)):
        browser.switch_to.frame(eachvalue)  # navigate in to the frame
        elementExist = browser.find_elements(by=By.CLASS_NAME, value="recaptcha-checkbox-border")
        print(len(elementExist))
        if len(elementExist) > 0:
            frameidentified = True
            browser.find_element(by=By.CLASS_NAME, value="recaptcha-checkbox-border").click()
        browser.switch_to.default_content()  # come out of the frame
        if frameidentified == True:
            break
    #browser.find_element(by=By.CLASS_NAME,value="recaptcha-checkbox-border").click()
    time.sleep(5)
    browser.quit()