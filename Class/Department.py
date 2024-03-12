class Department:
    def __init__(self,name,code,basicsalary):
        self.name=name
        self.code=code
        self.bsalary=basicsalary
    def calc(self):
        if self.bsalary<10000:
            self.da=self.bsalary*0.2
            self.hra=self.bsalary*0.25
            self.pf=self.bsalary*0.05
        else:
            self.da=self.bsalary*0.1
            self.hra=self.bsalary*0.15
            self.pf=self.bsalary*0.03
            self.net_sala=self.bsalary+self.da+self.hra-self.pf
    def disp(self):
        print("Name:",self.name)
        print("Empcode:",self.code)
        print("Base salary:",self.bsalary)
        print("DA:",self.da)
        print("HRA:",self.hra)
        print("PF:",self.pf)
        print("Net Salary:",self.net_sala)

class Teacher(Department):
    def __init__(self, name, code, basicsalary,dept):
        Department.__init__(self,name, code, basicsalary)
        self.department=dept
        self.student=[]
    def mark_attend(self,n):
        self.count=n
        print("Enter the attendance roll no wise(1-presant/0-apsent)")
        for i in range(0,n):
            att=int(input())
            self.student.append(att)
    def display_attend(self):
        print("List of presant students")
        for i in range(0,self.count):
            if self.student[i]==1:
                i+=1
                print("      ",i)
        print("List of apsent students")
        for i in range(0,self.count):
            if self.student[i]==0:
                print(i+1)
    def display(self):
        print("Name:",self.name)
        print("Empcode:",self.code)
        print("Base salary:",self.bsalary)
        print("DA:",self.da)
        print("HRA:",self.hra)
        print("PF:",self.pf)
        print("Net Salary:",self.net_sala)
teacher_list=[]
no_tech=int(input("Enter the number of teachers:"))
for i in range(0,no_tech):
    name=input("Enter the name of th teacher:")
    code=int(input("Enter the code:"))
    basicsalary=int(input("Enter the basicsalary:"))
    department=input("Enter the department:")
    no_std=int(input("Enter the number of students:"))
    tec=Teacher(name,code,basicsalary,department)
    tec.mark_attend(no_std)
    tec.calc()
    teacher_list.append(tec)
for i in range(0,no_tech):
    print("________________________")
    teacher_list[i].display()
    teacher_list[i].display_attend()
