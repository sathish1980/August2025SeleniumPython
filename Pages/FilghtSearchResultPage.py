from ElementUtils.CommonElements import CommonElements


class FlightSearchResultPage(CommonElements):

    def GetFromCodeFromCurrentUrl(self,browser):
        current_URL = self.GetCurrentURL(browser)
        FromCode_split = current_URL.split("=")[1]
        searchDetails =FromCode_split.split("&")[0]
        fromCode= searchDetails.split("-")[0]
        return fromCode