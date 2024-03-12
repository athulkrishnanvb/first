class Employee:
    def __init__(self,name,code,bsalary):
        self.name=name
        self.code=code
        self.bsalary=bsalary
    def cal(self):
        da=0.10*self.bsalary
        hra=0.15*self.bsalary
        pf=0.03*self.bsalary
        net_sala=self.bsalary+da+hra-pf
        print("Name:",self.name)
        print("Empcode:",self.code)
        print("Base salary:",self.bsalary)
        print("DA:",da)
        print("HRA:",hra)
        print("PF:",pf)
        print("Net Salary:",net_sala)

empname1=input("Enter the name of first employee:")
empcode1=int(input("Enter the code of first employee"))
bsalary1=int(input("Enter the basesalary of first employee:"))
empname2=input("Enter the name of second employee:")
empcode2=int(input("Enter the code of second employee"))
bsalary2=int(input("Enter the basesalary of second employee:"))

obj=Employee(empname1,empcode1,bsalary1)
obj1=Employee(empname2,empcode2,bsalary2)
obj.cal()
print("__________________________________")
obj1.cal()



