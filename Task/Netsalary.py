bsalary = int(input("enter the Basic salary :"))
if bsalary > 10000:
    hra = 0.02 * bsalary
    pf = 0.03 * bsalary
    da = 0.05 * bsalary
    gsalary = bsalary + hra + da - pf
else:
    hra = 0.05 * bsalary
    pf = 0.07 * bsalary
    da = 0.09 * bsalary
    gsalary = bsalary + hra + da - pf
print("basic salary : ", bsalary)
print("HRA : ", hra)
print("PF : ", pf)
print("DA : ", da)
print("NET SALARY : ",gsalary)