class BankAccount:
    def __init__(self,available):
        self.available=available
    def deposit(self,money):
        self.available+=money
        print(f"money deposited is {money} and total avaiable balamce is {self.available}")
    def withdraw(self,money):
        if(self.available>money):
            print("insufficient balance")
        else:
            self.available-=money
            print(f"money withdrawn is {money} and total avaiable balamce is {self.available}")

obj=BankAccount(1000)
operation=input("enter the operation deposit or withdraw or exit")
exit=False;
while(True):
    if(operation=="deposit"):
        money=int(input("enter money to deposit"))
        obj.deposit(money)
    elif(operation=="withdraw"):
        money=int(input("enter money to withdraw"))
        obj.withdraw(money)
    elif(operation=="exit"):
        break
    else:
        print("invalid input")
