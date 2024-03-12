limit = int(input("Enter the lmit:"))
i=0
while i<=limit:
    print("Multiple of:",i)
    n=0
    while n<10:
        print(i,"*",n,"=",i*n)
        n+=1
    i+=1
