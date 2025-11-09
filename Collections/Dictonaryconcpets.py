class dictonaryConcepts():

    sathishDetails={"name":"Sathish","age":18,"qualification":"B.tech","Exp":13,"accno":"123123123"}
    kumarDetails = {"name": "kumar", "age": 28, "qualification": "B.tech", "Exp": 13, "accno": "111222333"}
    RajaDetails = {"name": "raja", "age": 38, "qualification": "B.tech", "Exp": 13, "accno": "333222111","name1":"raja"}
    bankDetails={123123123:sathishDetails,111222333:kumarDetails,333222111:RajaDetails}

    def getDetails(self):
        print(self.sathishDetails)
        print(self.bankDetails)
        print(type(self.bankDetails))
        print(self.bankDetails.get(333222111))
        print(len(self.bankDetails))
        print(self.bankDetails[111222333])
        print(self.bankDetails.keys())
        print(type(self.bankDetails.keys()))
        print(self.sathishDetails.values())
        for eachvalue in self.bankDetails.items():
            for eachaccount in eachvalue:
                print(eachaccount)

        if "name1" in self.sathishDetails:
            print(self.sathishDetails["name"])
        else:
            print("account doesnot exist")
        self.sathishDetails["Exp"]=15
        print(self.sathishDetails)
        self.sathishDetails.update({"age":25})
        print(self.sathishDetails)
        #self.sathishDetails.pop()
        self.sathishDetails.popitem()
        del self.sathishDetails["qualification"]
        print(self.sathishDetails)



obj = dictonaryConcepts()
obj.getDetails()
