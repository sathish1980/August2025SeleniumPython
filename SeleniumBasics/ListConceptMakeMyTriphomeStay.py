import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MK():


    def launch(self,expectedCountry):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.makemytrip.com/")
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))

        self.browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='menu_Homestays']//a")))

       # self.browser.find_element(by=By.XPATH,value="//*[@data-cy='menu_Homestays']//a").click()
       # WebDriverWait(self.browser, 20).until(
        #    EC.element_to_be_clickable((By.XPATH, "//*[@for='city']")))

        #self.browser.find_element(by=By.XPATH,value="//*[@for='city']").click()

        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))

        self.browser.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()
        time.sleep(5)
        WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']//li[last()]")))

        allCities = self.browser.find_elements(by=By.XPATH,value="//*[starts-with(@class,'react-autosuggest__section-container')]//ul//li")
        print(len(allCities))
        for eachvalue in range(1,len(allCities)+1):
            WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']//li["+str(eachvalue)+"]//*[contains(@class,'lightGreyText')]")))

            actualCountry = self.browser.find_element(by=By.XPATH, value="//ul[@role='listbox']//li["+str(eachvalue)+"]//*[contains(@class,'lightGreyText')]").text
            print(actualCountry)
            if expectedCountry==actualCountry:
                self.browser.find_element(by=By.XPATH, value="//ul[@role='listbox']//li[" + str(
                    eachvalue) + "]").click()
                break

        time.sleep(4)


obj=MK()
obj.launch("CCU")
