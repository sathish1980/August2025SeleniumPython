
"""print("My name is: ",name,"and my age is ",age,"my qualification is : ",qualification)
print("My name is: ",name,"and my age is ",age,"my qualification is : ",qualification)
print("My name is: ",name,"and my age is ",age,"my qualification is : ",qualification)"""

# def functionname(parameters/arguments)
"""

types of funcitons:
4 types
function with out paramter  --1
fucntion with paramter      --2 

function with out return type--3
function with return type   --4

function with out parameter and with out return type
function with out parameter and with  return type

function with parameter and with out return type

"""

course="Python"
fees = 15000
newname = "kumar" # global variable

def printmyname():
    name = "Sathish" #local variable
    age = 20
    qualification = "B.tech"
    print("My name is: ", name, "and my age is: ", age, "my qualification is : ", qualification)

def printmynamedynaimcally(name,age,qualification):
    print("My name is: ", name, "and my age is: ", age, "my qualification is : ", qualification)

def addtwonumbers(firstnumber, secondnumber):
    output = firstnumber+secondnumber
    print("sum of 2 number is: ", output)

def invoice(billing1,billing2):
    total_amount= billing1+billing2
    return total_amount

def gettax(amount1,amount2):
    print("Welcome ", newname)
    print("the course is : ",course)
    print("The fees is : ",fees)
    actualamount = invoice(amount1,amount2)
    taxamount = actualamount*0.13
    print("your tax amonut is: ",taxamount)
    final_amount = actualamount+taxamount
    print("final billing amount is : ", final_amount)




printmynamedynaimcally("FITa",45,"BSC")
printmynamedynaimcally("SAthish",35,"B.tech")
printmynamedynaimcally("Raja",25,"MBA")
addtwonumbers(10,15)
addtwonumbers(29,5)
gettax(700,10)


