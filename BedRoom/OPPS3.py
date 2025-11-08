from BedRoom.OOPS1 import firstClass
from BedRoom.OPPS2 import secondclass

class OOPS3(firstClass,secondclass): # Multiple

    def div(self):
        print("div")

obj = OOPS3()
obj.div()
obj.add1(10,11)
obj.mul(11,12)