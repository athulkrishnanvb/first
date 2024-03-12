class Account:
    def __init__(self,acc_hold,acc_num):
        self.acc_hold=acc_hold
        self.acc_num=acc_num
        self.amount=0

    def deposite(self):
        amount=int(input("Enter the Amount to deposite:"))
        self.amount=self.amount+amount
        print("\nDeposite Successful\n")

    def withdraw(self):
        withdr=int(input("Enter the Amount to withdraw:"))
        self.withdraw=withdr
        if self.withdraw>self.amount:
            print("\nNot enough balance\n")
        else:
            print("\nAmount Withdrawed\n")
            balance=self.amount-withdr
            self.amount=balance

    def balance(self):
        print("\nBalance:",self.amount)

accname=input("Enter the account holder name:")
accnum=int(input("Enter the Account number:"))
obj=Account(accname,accnum)
while True:
    print("1.Deposite Money")
    print("2.Withdraw Money")
    print("3.View Balance")
    print("4.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        obj.deposite()
    elif choice==2:
        obj.withdraw()
    elif choice==3:
        obj.balance()
    elif choice==4:
        print("\nExiting...\n")
        break
    else:
        print("Invalid")




    



    
