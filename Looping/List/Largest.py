num = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the numbers:"))
    num.append(elem)
large=num[0]
for i in range(1,limit):
    if num[i]>large:
        large=num[i]
print(large)
    