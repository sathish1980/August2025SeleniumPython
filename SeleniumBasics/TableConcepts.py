import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TableConcepts():

    def lauch(self,expectedCountry):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.leafground.com/table.xhtml")
        print(browser.title)
        print(browser.current_url)
        print(browser.current_window_handle)
        ParentWindow=browser.current_window_handle
        allPages = browser.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        for eachPages in range(1, len(allPages) + 1):
            browser.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachPages)+"]").click()
            time.sleep(3)
            classname = browser.find_element(by=By.XPATH,
                                 value="//*[@class='ui-paginator-pages']//a[" + str(eachPages) + "]").get_attribute("class")
            print(classname)
            if classname.__contains__("ui-state-active"):
                print("Page no: ",eachPages," is selected")
            allRows = browser.find_elements(by=By.XPATH,value="//tbody[@id='form:j_idt89_data']//tr")
            for eachRows in range(1,len(allRows)+1):
                actualCountry = browser.find_element(by=By.XPATH, value="//tbody[@id='form:j_idt89_data']//tr["+str(eachRows)+"]//td[2]//span[contains(@style,'vertical-align:')]").text
                if expectedCountry == actualCountry:
                    actualRepresentative = browser.find_element(by=By.XPATH, value="//tbody[@id='form:j_idt89_data']//tr[" + str(
                        eachRows) + "]//td[3]//span[contains(@style,'vertical-align:')]").text
                    print(actualRepresentative)

        time.sleep(5)
        browser.quit()

obj = TableConcepts()
obj.lauch("India")
