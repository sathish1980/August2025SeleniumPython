import time


from selenium import webdriver
from selenium.webdriver.common.by import By

class scroll():

    def scrollimplementation(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/drag.xhtml")
        self.driver.maximize_window()
        # scroll down
        self.driver.execute_script("window.scrollTo(0, 100)", "")
        time.sleep(3)
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -100)", "")
        time.sleep(3)

        # scroll right
        self.driver.execute_script("window.scrollTo(100, 0)", "")
        time.sleep(3)
        # scroll left
        self.driver.execute_script("window.scrollTo(-100, 0)", "")
        time.sleep(3)
        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        #scroll up
        self.driver.execute_script("window.scrollTo(0, 0)", "")
        time.sleep(3)
        # screenshot
        startbutton=self.driver.find_element(by=By.ID,value="form:j_idt119")
        self.driver.execute_script("arguments[0].scrollIntoView();", startbutton)
        time.sleep(3)


obj= scroll()
obj.scrollimplementation()

