import time

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from BrowserUtils.Browser import Browser
from ElementUtils.CommonElements import CommonElements
from Pages.FilghtSearchResultPage import FlightSearchResultPage
from Pages.FlightSearchPage import FlightSearchPage
from Pages.MakeMyTripLandingPage import MakeMyTripLandingPage
from Utils.FileDetails.ReadJsonData import ReadJsonData


class Test_MakeMyTripFlightSearch():


    def test_FlightSearchWithValidData_HardcodedData(self):
        env_details =ReadJsonData().GetEnvironmentDetails()
        url = env_details["url"]
        browser = Browser().OpenTheBrowser()
        CommonElements().EnterURL(browser,url)
        #browser.get(url)
        MakeMyTripLandingPage().Close_AccountDetailsPopup(browser)
        """
        Select From location
        Select To location
        Select deparute date
        Select Traveller
        Click on Search
        Valdidate the Search Result
        """
        time.sleep(5)
        FlightSearchPage().ClickOnFromCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser,"MAA")
        FlightSearchPage().ClickOnToCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser, "PNQ")
        FlightSearchPage().SelectDate(browser, "25")
        FlightSearchPage().ClickOnSearchButton(browser)
        time.sleep(3)
        from_code= FlightSearchResultPage().GetFromCodeFromCurrentUrl(browser)
        assert "MAAs" == from_code
        Browser().Close_Browser(browser)

    @pytest.mark.usefixtures("Get_FlightSearch_data")
    def tetest_FlightSearchWithValidData(self,Get_FlightSearch_data):
        env_details =ReadJsonData().GetEnvironmentDetails()
        url = env_details["url"]
        browser = Browser().OpenTheBrowser()
        CommonElements().EnterURL(browser,url)
        #browser.get(url)
        MakeMyTripLandingPage().Close_AccountDetailsPopup(browser)
        """
        Select From location
        Select To location
        Select deparute date
        Select Traveller
        Click on Search
        Valdidate the Search Result
        """
        #time.sleep(5)
        FlightSearchPage().ClickOnFromCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser,Get_FlightSearch_data[0])
        FlightSearchPage().ClickOnToCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser, Get_FlightSearch_data[1])
        FlightSearchPage().SelectDate(browser, Get_FlightSearch_data[2])
        FlightSearchPage().ClickOnSearchButton(browser)
        time.sleep(3)
        from_code= FlightSearchResultPage().GetFromCodeFromCurrentUrl(browser)
        assert Get_FlightSearch_data[0] == from_code
        Browser().Close_Browser(browser)


    @pytest.mark.usefixtures("Get_FlightSearch_data_multiple")
    def test_FlightSearchWithValidData_multipledata(self,Get_FlightSearch_data_multiple):
        env_details =ReadJsonData().GetEnvironmentDetails()
        url = env_details["url"]
        browser = Browser().OpenTheBrowser()
        CommonElements().EnterURL(browser,url)
        #browser.get(url)
        MakeMyTripLandingPage().Close_AccountDetailsPopup(browser)
        """
        Select From location
        Select To location
        Select deparute date
        Select Traveller
        Click on Search
        Valdidate the Search Result
        """
        time.sleep(5)
        FlightSearchPage().ClickOnFromCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser,Get_FlightSearch_data_multiple[0])
        FlightSearchPage().ClickOnToCityDropdown(browser)
        FlightSearchPage().SelectValueFromList(browser, Get_FlightSearch_data_multiple[1])
        FlightSearchPage().SelectDate(browser, Get_FlightSearch_data_multiple[2])
        FlightSearchPage().ClickOnSearchButton(browser)
        time.sleep(3)
        from_code= FlightSearchResultPage().GetFromCodeFromCurrentUrl(browser)
        assert Get_FlightSearch_data_multiple[0] == from_code
        Browser().Close_Browser(browser)
        browser.back()

    @pytest.mark.usefixtures("flightdataFromExecl")
    def test_validFlightsearchwithMultidata(self, flightdataFromExecl):
        try:
            env_details = ReadJsonData().GetEnvironmentDetails()
            url = env_details["url"]
            browser = Browser().OpenTheBrowser()
            CommonElements().EnterURL(browser, url)
            # browser.get(url)
            MakeMyTripLandingPage().Close_AccountDetailsPopup(browser)
            time.sleep(5)
            total_data = flightdataFromExecl
            print(total_data)
            size = len(total_data)
            print(size)
            totalcolumn = size / 3
            for i in range(1, int(totalcolumn) + 1):
                FlightSearchPage().ClickOnFromCityDropdown(browser)
                FlightSearchPage().SelectValueFromList(browser, flightdataFromExecl["From" + str(i)])
                FlightSearchPage().ClickOnToCityDropdown(browser)
                print("to city", flightdataFromExecl["To" + str(i)])
                FlightSearchPage().SelectValueFromList(browser, flightdataFromExecl["To" + str(i)])
                FlightSearchPage().SelectDate(browser, flightdataFromExecl["Date" + str(i)])
                FlightSearchPage().ClickOnSearchButton(browser)
                time.sleep(3)
                from_code = FlightSearchResultPage().GetFromCodeFromCurrentUrl(browser)
                assert flightdataFromExecl["From" + str(i)] == from_code
                #Browser().Close_Browser(browser)
                browser.back()
        finally:
            pass
            #Browser().Close_Browser()