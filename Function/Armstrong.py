def arm(n):
    num = n
    st=str(n)
    l=len(st)
    armsum = 0
    for i in st:
        inum=int(i)
        armsum+=inum**l
    if armsum==num1:
        print("Armstrong")
    else:
        print("Not armstrong")
num1=int(input("Enter the number:"))
arm(num1)
