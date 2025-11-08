from inheritance.SantoshMainBranch import SantoshMainBranch


class Overloading(SantoshMainBranch):

    __names ="sathish"

    def set_Name(self,name):
        self.__names=name

    def get_Name(self):
        return self.__names


    def amount(selfa,a,b):
        print(a+b)

    def amount(self,a,b):
        print(a-b)

    def PrintMainBranchName(self,g):
        print("test")

ol= Overloading()
ol.amount(3,4)
ol.PrintMainBranchName(45)