import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class download:
    option = webdriver.ChromeOptions()
    pref = {"download.default_directory": "C:\\Users\\DELL\\PycharmProjects\\August2025SeleniumPython\\Download\\"}
    option.add_experimental_option("prefs", pref)
    option.add_argument("--start-maximized")
    option.add_argument("--incognito")
    driver = webdriver.Chrome(options=option)


    def downdefaultlocation(self):
        #driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.leafground.com/grid.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,value="form:j_idt93").click()
        time.sleep(5)

    def downspecificlocation(self):
        self.driver.get("https://www.leafground.com/grid.xhtml")
        #self.driver.maximize_window()
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "form:j_idt93")))

        self.driver.find_element(by=By.ID,value="form:j_idt93").click()




D = download()
D.downspecificlocation()
