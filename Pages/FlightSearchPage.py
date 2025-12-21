from selenium.webdriver.common.by import By

from ElementUtils.CommonElements import CommonElements


class FlightSearchPage(CommonElements):

    def ClickOnFromCityDropdown(self, browser):
        self.ElementToBeClickable(browser, "//*[@for='fromCity']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        city_Fromdropdown_element = browser.find_element(by=By.XPATH, value="//*[@for='fromCity']")
        self.ClickOnButton(city_Fromdropdown_element)

    def ClickOnToCityDropdown(self, browser):
        self.ElementToBeClickable(browser, "//*[@for='toCity']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        city_Todropdown_element= browser.find_element(by=By.XPATH, value="//*[@for='toCity']")
        self.ClickOnButton(city_Todropdown_element)

    def SelectValueFromList(self, browser, expectedCountry):
        self.ElementToBeClickable(browser, "//*[@id='react-autowhatever-1']//ul//li[last()]")
        allElements = browser.find_elements(by=By.XPATH, value="//*[@id='react-autowhatever-1']//ul//li")
        for eachelement in range(1, len(allElements) + 1):
            actualCountry = browser.find_element(by=By.XPATH,
                                                 value="//*[@id='react-autowhatever-1']//ul//li[" + str(
                                                     eachelement) + "]//div[starts-with(@class,'font14')]").text
            print(actualCountry)
            if expectedCountry == actualCountry:
                browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//ul//li[" + str(
                    eachelement) + "]").click()
                break

    def SelectDate(self, browser, expectedDate):
        self.ElementToBeClickable(browser, "//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")
        allRows = browser.find_elements(by=By.XPATH,
                                        value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")
        for eachelement in range(1, len(allRows) + 1):
            allcolumns = browser.find_elements(by=By.XPATH,
                                               value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                                   eachelement) + "]//*[@class='DayPicker-Day']")
            for eachcolumn in range(1, len(allcolumns) + 1):
                actualDate = browser.find_element(by=By.XPATH,
                                                  value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                                      eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                                      eachcolumn) + "]//p[1]").text
                print(actualDate)
                if expectedDate == actualDate:
                    browser.find_element(by=By.XPATH,
                                         value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                             eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                             eachcolumn) + "]").click()
                    return

    def SelectHotelDate(self, browser, expectedDate):
        self.ElementToBeClickable(browser, "//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")
        allRows = browser.find_elements(by=By.XPATH,
                                        value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")
        for eachelement in range(1, len(allRows) + 1):
            allcolumns = browser.find_elements(by=By.XPATH,
                                               value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                                   eachelement) + "]//*[@class='DayPicker-Day']")
            for eachcolumn in range(1, len(allcolumns) + 1):
                actualDate = browser.find_element(by=By.XPATH,
                                                  value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                                      eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                                      eachcolumn) + "]").text
                print(actualDate)
                if expectedDate == actualDate:
                    browser.find_element(by=By.XPATH,
                                         value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                             eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                             eachcolumn) + "]").click()
                    return

    def ClickOnSearchButton(self, browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='submit']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser.find_element(by=By.XPATH, value="//*[@data-cy='submit']").click()