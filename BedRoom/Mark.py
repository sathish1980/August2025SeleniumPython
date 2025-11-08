class mark():
    status="fail"
    def getMark(self):
        mark = input("Enter studentmark: ")
        for value in range(1,101):
            if int(mark)>=40 and value>=40:
                self.status = "pass"
        if self.status == "pass":
            print("You are pass")
        else:
            print("you are fail : ",mark)


obj= mark()
obj.getMark()