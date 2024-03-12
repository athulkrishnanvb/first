list1 = []
prime = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    elem = int(input("Enter the numbers:"))
    list1.append(elem)
for num in list1:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            prime.append(num)
print("Prime number:",prime)