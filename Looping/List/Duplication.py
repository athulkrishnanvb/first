lis1 = []
lis2 = []
limit = int(input("Enter thr limit:"))
for i in range(limit):
    elem = int(input("Enter the number:"))
    lis1.append(elem)
for i in lis1:
    if i not in lis2:
        lis2.append(i) 
print(lis1)
print(lis2)