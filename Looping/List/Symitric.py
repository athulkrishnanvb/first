list1 = []
rev = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem = int(input("Enter the numbers:"))
    list1.append(elem)
for i in list1:
    rev.insert(0,i)
    if list1==rev:
        print("Symetric")
        break
else:
    print("not")



