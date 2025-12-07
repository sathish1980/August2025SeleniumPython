import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class uplod:
    driver = webdriver.Edge()
    def upl(self):
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH,value="(//div[@class='input-file-upload-hover-placeholder']//parent::div)[1]").click()
        pyperclip.copy("D:\\Sathish\\JAVA\\Java basics.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print("uploaded sucessfully")
        time.sleep(2)


e =uplod()
e.upl()