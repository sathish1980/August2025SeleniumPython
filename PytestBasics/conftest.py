import pytest


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
