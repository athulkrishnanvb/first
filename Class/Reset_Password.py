class Person:
    def __init__(self,password):
        self.password1=password
    def login(self):
        pas=input("Enter the password:")
        if self.password1==pas:
          print("\nLogin Successful\n")
        else:
          print("\nLogin Failed\n")
    def resetpas(self):
        newpas=input("Enter New password:")
        self.pas=newpas
        print("\nPassword reset successful\n")

password2=input("Enter the Password:")
obj=Person(password2)
while True:
    print("1.Login")
    print("2.Reset Password")
    print("3.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
       obj.login()
    elif choice==2:
       obj.resetpas()
    elif choice==3:
       print("\nExiting...\n")
       break
    else:
       print("\nInvalid\n")
       