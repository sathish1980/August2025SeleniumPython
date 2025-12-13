import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FrameConcepts():

    def lauch(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.leafground.com/frame.xhtml")
        frameidentified =False
        allFrames = browser.find_elements(by=By.TAG_NAME,value="iframe")
        for eachvalue in range(0,len(allFrames)):
            browser.switch_to.frame(eachvalue) # navigate in to the frame
            elementExist = browser.find_elements(by=By.XPATH, value="//*[@id='Click' and contains(@style,'00aadf')]")
            print(len(elementExist))
            if len(elementExist)>0:
                frameidentified= True
                browser.find_element(by=By.XPATH, value="//*[@id='Click' and contains(@style,'00aadf')]").click()
            browser.switch_to.default_content() # come out of the frame
            if frameidentified == True:
                break

        time.sleep(5)
        browser.close()



obj = FrameConcepts()
obj.lauch()
