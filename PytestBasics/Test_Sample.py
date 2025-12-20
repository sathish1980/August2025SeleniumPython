import pytest


class Test_Sample():
    @pytest.mark.SIT
    def test_testcase1(self):
        print("First Test case")

    @pytest.mark.SIT
    def test_testcase2(self):
        print("Second Test case")
        print(2/0)

    @pytest.mark.SIT
    def test_testcase3(self):
        print("Third Test case")
        self.add()

    def add(self):
        print(3)
        return 3
