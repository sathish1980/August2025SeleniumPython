from inheritance.SantoshAnnaNagar import SantoshAnnanagar


class SantoshAnnanagarInvoice(SantoshAnnanagar):

    def invoice(self,amount):
        print("Invoice ",amount)

SAI = SantoshAnnanagarInvoice()
SAI.GetItem("orange")
SAI.PrintMainBranchName(45)
SAI.invoice(SAI.GetItemAmount("apple"))