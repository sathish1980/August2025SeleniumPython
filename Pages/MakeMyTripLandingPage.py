from selenium.webdriver.common.by import By

from ElementUtils.CommonElements import CommonElements


class MakeMyTripLandingPage(CommonElements):

    def Close_AccountDetailsPopup(self,browser):
        self.ElementToBeClickable(browser,"//*[@data-cy='closeModal']")
        popup_element = browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']")
        self.ClickOnButton(popup_element)

    def ClickOnFlightMenu(self,browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='menu_Flights']")
        flight_Menu = browser.find_element(by=By.XPATH, value="//*[@data-cy='menu_Flights']")
        self.ClickOnButton(flight_Menu)

    def ClickOnHotelMenu(self,browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='menu_Hotels']")
        hotel_Menu = browser.find_element(by=By.XPATH, value="//*[@data-cy='menu_Hotels']")
        self.ClickOnButton(hotel_Menu)

    def ClickOnHomeStaysMenu(self,browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='menu_Homestays']")
        hotel_Menu = browser.find_element(by=By.XPATH, value="//*[@data-cy='menu_Homestays']")
        self.ClickOnButton(hotel_Menu)
