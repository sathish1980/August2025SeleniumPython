class ExceptionHandling():

    def div(self,a,b):
        try:
            c=a/b
            print("output is :",c)
        except ArithmeticError:
            print(Exception )
            if(a>0 and b>0):
                c=a/b
            else:
                print("b values is <=0")
        except:
            print(Exception )
        finally:
            print("this is finally block")

    def add(self,a,b):
        c=a+b
        print("output is :",c)

    def sub(self,a,b):
        c=a-b
        print("output is :",c)

    def mul(self,a,b):
        c=a*b
        print("output is :",c)

obj= ExceptionHandling()
obj.div(10,0)
obj.add(10,2)
obj.sub(10,2)
obj.mul(10,2)
