list1 = [1,2,4,8,9,10]
l=len(list1)
list2 = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem = int(input("Enter the numbers:"))
    list2.append(elem)
for i in range(0,l-limit+1):
    if list1[i:i+limit]==list2:
        print("yes")
        break
else:
    print("No")