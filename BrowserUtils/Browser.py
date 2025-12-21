from contextlib import nullcontext

from selenium import webdriver

from Utils.FileDetails.ReadJsonData import ReadJsonData


class Browser():


    def OpenTheBrowser(self):
        env_details = ReadJsonData().GetEnvironmentDetails()
        browser_name = env_details["browser"]
        if browser_name=="chrome":
            self.browser = webdriver.Chrome()
        elif browser_name == "edge":
            self.browser = webdriver.Edge()
        self.browser.maximize_window()
        return self.browser

    def Close_Browser(self,browser):
        browser.quit()

