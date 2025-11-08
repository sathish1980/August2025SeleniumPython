from BedRoom.OOPS1 import firstClass


class OOPS4(firstClass):

    def sub(self):
        print("sub")

    def add1(self,x,y):
        print("output: ",x+y)

obj =OOPS4()
obj.sub()
obj.add1(11,12)
obj = firstClass()
obj.add1(10,11)

