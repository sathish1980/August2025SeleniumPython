class ItemAmount():

    ItemAmounts={"apple":100,"Banana":70,"orange":120}

    def GetItemAmount(self,itemName):
        if itemName in self.ItemAmounts:
            return self.ItemAmounts.get(itemName)
