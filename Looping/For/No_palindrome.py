num = int(input("Enter the numbers:"))
n=num
n1=str(num)
rev = 0
l=len(n1)
for i in range(l-1,-1,-1):
     d=int(n1[i])
     rev=(rev*10)+d
if rev==n:
     print("yes")
else:
     print("no")