class Testdata():

    def method1(self,a,b):
        try:
            div =a/b
            print("mehtod1: ",div)
        except ZeroDivisionError:
            print(" you have given the denominator as 0 ")
        except :
            print("invalida data")
        finally:
            print("methos executed sucessfully")

    def method2(self,a,b):
        div =a/b
        print("mehtod2: ",div)

    def method3(self,a,b):
        div =a/b
        print("mehtod3: ",div)

    def method4(self,a,b):
        div =a/b
        print("mehtod4: ",div)

obj =Testdata()
obj.method1(2,0)
obj.method2(10,10)
obj.method3(3,6)
obj.method4(5,10)
