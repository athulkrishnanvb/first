num = int(input("Enter the numbers:"))
sum = 0
while num!=0:
    d=num%10
    sum=sum+d
    num//=10
while sum>=10:
    newsum=0
    while sum>0:
        newsum+=sum%10
        sum//=10
    sum=newsum
print(sum)

    