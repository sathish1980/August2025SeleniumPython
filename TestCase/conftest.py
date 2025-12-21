import pytest

from FileHandling.ExcelRead import ExcelRead
from Utils.FileDetails.ExcelRead import Excel_Read


@pytest.fixture
def input_value():
    username = "Sathish kumar"
    return username
@pytest.fixture
def Get_URL():
    url = "https://www.google.com/"
    return url

@pytest.fixture
def Get_FaceBook_URL():
    url = "https://www.facebook.com"
    return url

@pytest.fixture
def Get_FaceBook_credentails():
    return ["kumars.sathish189@gmail.com","password"]

@pytest.fixture(params=[("kumars.sathish189@gmail.com","pass"),("fita@gmail.com","pass")])
def facebookLoginWithMultipleData(request):
    return request.param

@pytest.fixture
def Get_FlightSearch_data():
    return ["MAA","BOM","27"]

@pytest.fixture(params=[("MAA","PNQ","23"),("BOM","PNQ","27")])
def Get_FlightSearch_data_multiple(request):
    return request.param

credential_excel_dic = [Excel_Read().retrundicvalue("ValidFlight")]

@pytest.fixture(params=credential_excel_dic)
def flightdataFromExecl(request):
    return request.param
