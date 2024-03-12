list1 = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem = int(input("Enter the datas:"))
    list1.append(elem)
print(list1)
oddlist=[]
evenlist=[]
for i in list1:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even=",evenlist)
print("odd=",oddlist)