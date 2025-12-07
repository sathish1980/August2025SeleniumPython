import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dropdown():

    def lauch(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        """self.browser.get("https://www.google.com/")
        self.browser.back()
        self.browser.forward()
        self.browser.refresh()"""
        #By ID
        #username =self.browser.find_element(by=By.ID,value="email")
        # By name
        #username = self.browser.find_element(by=By.NAME, value="email")
        # By class name
        #username = self.browser.find_element(by=By.CLASS_NAME, value="inputtext_55r1_6luy")
        # By css -tag and id
        #username = self.browser.find_element(by=By.CSS_SELECTOR, value="input#email")
        # By css -tag and class (make sure class value does not contains space in it)
        #username = self.browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy")
        # By css -tag and attribute
        self.browser.implicitly_wait(60)
        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='open-registration-form-button']")))
        Createaccount = self.browser.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']")
        Createaccount.click()
        #time.sleep(60)
        #WebDriverWait(self.browser, 60).until(
         #   EC.visibility_of_element_located((By.NAME, "firstname")))
        dayDropdown = Select(self.browser.find_element(by=By.ID,value="day"))
        dayDropdown.select_by_value("10")
        time.sleep(5)
        dayDropdown.select_by_index(20)
        time.sleep(5)
        dayDropdown.select_by_visible_text("15")
        print(dayDropdown.is_multiple)
        time.sleep(5)
        self.browser.close()

obj = Dropdown()
obj.lauch()