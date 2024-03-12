num = int(input("Enter the number:"))
sum = 0
while num!=0:
    d=num%10
    sum=sum+d
    num//=10
    if num==0 and sum>9:
        num=sum
        sum=0
print(sum)