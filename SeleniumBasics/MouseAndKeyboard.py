import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MouseAndKeyboard():

    def lauch(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.ebay.com/")
        mouseAction = ActionChains(self.browser)
        mouseAction.move_to_element(self.browser.find_element(by=By.XPATH,value="(//*[@class='vl-flyout-nav__container']//li//a)[3]")).perform()
        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Computers and tablets']")))

        mouseAction.move_to_element(self.browser.find_element(by=By.XPATH,value="//*[text()='Computers and tablets']")).click().perform()
        time.sleep(5)
        self.browser.close()

    def mouseAction2(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        mouseAction = ActionChains(self.browser)
        mouseAction.move_to_element(self.browser.find_element(by=By.ID,value="email")).send_keys("FITA_Annanagar").double_click().context_click().perform()
        time.sleep(5)
        self.browser.close()

    def mouseAction3(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.leafground.com/drag.xhtml")
        mouseAction = ActionChains(self.browser)
        #mouseAction.move_to_element(self.browser.find_element(by=By.ID,value="form:drag")).drag_and_drop(self.browser.find_element(by=By.ID,value="form:drag"),self.browser.find_element(by=By.ID,value="form:drop_content")).perform()
        mouseAction.move_to_element(self.browser.find_element(by=By.ID, value="form:conpnl")).drag_and_drop_by_offset(self.browser.find_element(by=By.ID, value="form:conpnl"),150,0).perform()
        mouseAction.move_to_element(self.browser.find_element(by=By.ID, value="form:conpnl")).drag_and_drop_by_offset(
            self.browser.find_element(by=By.ID, value="form:conpnl"), -100, 0).perform()

        time.sleep(5)
        self.browser.close()

    def KeyboardAction(self):
        #self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        mouseAction = ActionChains(self.browser)
        mouseAction.move_to_element(self.browser.find_element(by=By.ID,value="email")).send_keys("FITA Annanagar").double_click().perform()
        mouseAction.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(5)
        self.browser.close()

obj = MouseAndKeyboard()
obj.KeyboardAction()
