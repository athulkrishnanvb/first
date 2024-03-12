num = int(input("Enter the number:"))
limit = int(input("Enter the limit: "))
pnum=[]
for n in range(num,limit+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            pnum.append(n)
print(pnum)