num = int(input("Enter the number:"))
sum = 0
while num!=0:
    d=num%10
    if d%2!=0:
        sum=sum+d
    num//=10
print(sum)
        

    
