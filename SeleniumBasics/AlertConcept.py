import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertConcepts():

    def lauch(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.leafground.com/alert.xhtml")
        browser.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        browser.switch_to.alert.accept()

        actualText =browser.find_element(by=By.ID,value="simple_result").text
        expectedText="You have successfully clicked an alert"
        if actualText==expectedText:
            print("Test case passed")

        browser.find_element(by=By.ID, value="j_idt88:j_idt93").click()
        browser.switch_to.alert.dismiss()
        actualText = browser.find_element(by=By.ID, value="result").text
        expectedText = "User Clicked : Cancel"
        if actualText == expectedText:
            print("Canceled Test case passed")

        browser.find_element(by=By.ID, value="j_idt88:j_idt104").click()
        browser.switch_to.alert.send_keys("Fita Annanagar")
        print(browser.switch_to.alert.text)
        browser.switch_to.alert.accept()
        actualText = browser.find_element(by=By.ID, value="confirm_result").text
        expectedText = "User entered name as: Fita Annanagar"
        if actualText == expectedText:
            print("User enetered text Test case passed")

        time.sleep(5)
        browser.close()



obj = AlertConcepts()
obj.lauch()
