BalanceAmount = 5000
LimitPerDay = 10000
CustomerType = "Premium"
AtmBalance =3000;
def condition_check(withdrawlamount,CustomerType):

    if(withdrawlamount>=LimitPerDay):
        pass
        #print("Max you can withdraw 10000 per day")
    elif(withdrawlamount <= BalanceAmount): # elif(withdrawlamount <= BalanceAmount and AtmBalance>=withdrawlamount):
        if(AtmBalance>=withdrawlamount):
            newbalance = BalanceAmount-withdrawlamount
            print("Your are good to withdraw , ", withdrawlamount)
            print("Your current balance is: ",newbalance)
        else:
            print("Atm doesnot have a enough money to dispence please try with Rs. ",AtmBalance)
    elif (withdrawlamount <= BalanceAmount or CustomerType=="Premium"):
        newbalance = BalanceAmount - withdrawlamount
        print("Your are good to withdraw , ", withdrawlamount)
        print("Your current balance is: ", newbalance)
    else:
        print("your requested amount Rs. ",withdrawlamount," is greater than balance amount ")

condition_check(3000,"Premium")

