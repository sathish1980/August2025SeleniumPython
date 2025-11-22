import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver


class FirstClass():

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
        username = self.browser.find_element(by=By.CSS_SELECTOR, value="input[aria-label='Email address or phone number']")
        # By css -tag and class and attribute (make sure class value does not contains space in it)
        # username = self.browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy[aria-label='Email address or phone number']")
        # Startswith -^
        username = self.browser.find_element(by=By.CSS_SELECTOR,
                                             value="div._6lux>input[class^='inputtext']")
        # endswith -$
        username = self.browser.find_element(by=By.CSS_SELECTOR,
                                             value="div._6lux>input[class$='uy']")
        # contains -*
        username = self.browser.find_element(by=By.CSS_SELECTOR,
                                             value="div._6lux>input[class*='uy']")

        username.send_keys("sathish")
        username.clear()
        username.send_keys("FITA")
        #self.browser.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        #self.browser.find_element(by=By.PARTIAL_LINK_TEXT, value="pass").click()

        time.sleep(5)
        self.browser.close()

obj = FirstClass()
obj.lauch()