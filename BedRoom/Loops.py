global Atm_Balance


def Withdrwal():
    Atm_Balance = 5000
    while(Atm_Balance>0):
        amount= input("Enter the with Amount")
        if(amount=="Exit"):
            break
        if(Atm_Balance>=int(amount)):
            Atm_Balance= Atm_Balance-int(amount)
            print("You can withdraw: ",amount)
        else:
            print("Atm does not have a enough money to dispence")

def forloop():
    for name in range(10,21): #0,1,2,3,4,5,6,7,8,9
        if name == 15:
            continue
        print(name)



forloop()
#Withdrwal()

