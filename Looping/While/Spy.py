num =input("Enter a number:")
l = len(num)
n = int(num)
sum=0
p=1
while n!=0:
    d=n%10
    sum=sum+d
    p=p*d
    n//=10
if p==sum:
    print("Spy")
else:
    print("Not spy")