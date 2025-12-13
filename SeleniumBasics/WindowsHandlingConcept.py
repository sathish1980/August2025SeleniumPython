import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindowsConcepts():

    def lauch(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.leafground.com/window.xhtml")
        print(browser.title)
        print(browser.current_url)
        print(browser.current_window_handle)
        ParentWindow=browser.current_window_handle
        browser.find_element(by=By.ID,value="j_idt88:new").click()
        allWindows =browser.window_handles
        for eachWindows in allWindows:
            if eachWindows!=ParentWindow:
                browser.switch_to.window(eachWindows)
                elementExist = browser.find_elements(by=By.ID,value="menuform:j_idt40")
                if len(elementExist)>0:
                  browser.find_element(by=By.ID, value="menuform:j_idt40").click()
                  browser.find_element(by=By.ID,value="menuform:m_input").click()
                  browser.find_element(by=By.ID,value="j_idt88:name").send_keys("FITA")
                  browser.switch_to.window(ParentWindow)
                  break
                browser.switch_to.window(ParentWindow)
        browser.quit()
        time.sleep(5)




obj = WindowsConcepts()
obj.lauch()
