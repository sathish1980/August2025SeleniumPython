import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class css():

    def launch(self,totalAdults,totalchild):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.makemytrip.com/")
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))

        self.browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='menu_Homestays']//a")))

        self.browser.find_element(by=By.XPATH,value="//*[@data-cy='menu_Homestays']//a").click()
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='guest']")))

        self.browser.find_element(by=By.XPATH,value="//*[@for='guest']").click()
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='Adults']")))
        value = self.browser.find_element(by=By.XPATH,value="//*[@for='guest']//p[1]").value_of_css_property("color")
        print(value)
        if value =="rgba(0, 140, 255, 1)":
            print("Test Pass")
        actual_number = self.browser.find_element(by=By.XPATH,value="(//span[contains(@class,'counter__value')])[1]").text
        actualAdults = int(actual_number)
        actual_child_number = self.browser.find_element(by=By.XPATH,
                                                  value="(//span[contains(@class,'counter__value')])[2]").text
        actualchild= int(actual_child_number)

        i=actualAdults
        j=0
        if(actualAdults<totalAdults):
            while i<totalAdults:
                self.browser.find_element(by=By.XPATH,value="(//*[@class='counter'])[1]//button[contains(@class,'increment')]").click()
                i=i+1
        if (actualchild < totalchild):
            while j < totalchild:
                self.browser.find_element(by=By.XPATH,
                                          value="(//*[@class='counter'])[2]//button[contains(@class,'increment')]").click()
                j = j + 1
        time.sleep(4)


obj=css()
obj.launch(7,3)
