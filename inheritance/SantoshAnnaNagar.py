from inheritance.ItemAmounts import ItemAmount
from inheritance.SantoshMainBranch import SantoshMainBranch


class SantoshAnnanagar(SantoshMainBranch,ItemAmount):

    items = ["apple","orange","Banana"]

    def GetItem(self,itemname):
        if itemname in self.items:
            print("item exist", itemname)
        else:
            print("item not exist")

SA = SantoshAnnanagar()
#SA.GetItem("orange")
#SA.PrintMainBranchName(45)
#print(SA.GetItemAmount("apple"))

