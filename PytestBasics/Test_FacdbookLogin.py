import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("Get_FaceBook_URL")
class Test_FacebookLogin():

    #@pytest.mark.usefixtures("Get_FaceBook_URL")
    @pytest.mark.usefixtures("Get_FaceBook_credentails")
    def test_FBLoginValidation(self,Get_FaceBook_URL,Get_FaceBook_credentails):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(Get_FaceBook_URL)
        browser.find_element(by=By.ID,value="email").send_keys(Get_FaceBook_credentails[0])
        browser.find_element(by=By.ID, value="pass").send_keys(Get_FaceBook_credentails[1])
        browser.find_element(by=By.NAME,value="login").click()
        browser.quit()

    #@pytest.mark.usefixtures("Get_FaceBook_URL")
    @pytest.mark.usefixtures("facebookLoginWithMultipleData")
    def test_FBLoginWithParametrization(self,Get_FaceBook_URL,facebookLoginWithMultipleData):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(Get_FaceBook_URL)
        print(facebookLoginWithMultipleData[0])
        print(facebookLoginWithMultipleData[1])
        browser.find_element(by=By.ID, value="email").send_keys(facebookLoginWithMultipleData[0])
        browser.find_element(by=By.ID, value="pass").send_keys(facebookLoginWithMultipleData[1])
        browser.find_element(by=By.NAME, value="login").click()
        browser.quit()

