import pytest


class Test_sample2():

    @pytest.mark.run(order=2)
    #@pytest.mark.SIT
    def test_LoginTestcase(self):
        print("Login sucessfully")

    @pytest.mark.run(order=1)
    #@pytest.mark.Sanity
    #@pytest.mark.SIT
    def test_craLoginTestcase(self):
        print("CRA Login sucessfully")

    @pytest.mark.run(order=3)
    #@pytest.mark.Sanity
    def test_TransactionTestcase(self):
        print("Login sucessfully")