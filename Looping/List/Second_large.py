num = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the numbers:"))
    num.append(elem)
large=num[0]
for i in range(1,limit):
    if num[i]>large:
        large=num[i]
print("big",large)
i=0
while(1):
    if num[i]!=large:
        sbig=num[i]
        break
    i+=1
for i in range(i+1,limit):
    if num[i]<large and num[i]>sbig:
        sbig=num[i]
print("second big",sbig)
    