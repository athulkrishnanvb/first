num = 369
sum = 0
while num!=0:
    d=num%10
    sum=sum+d
    num//=10
print(sum)