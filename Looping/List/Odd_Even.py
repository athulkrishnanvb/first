list1 = []
list2 = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem = int(input("Enter the numbers:"))
    list1.append(elem)
lim = int(input("Enetr the limit2:"))
for i in range(lim):
    elem1 = int(input("Enter the numbers:"))
    list2.append(elem1)
list1.extend(list2)
list2.clear()
for i in list1:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
        list1.remove(i)
print("even list:",list1)
print("odd list:",list2)