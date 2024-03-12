num = int(input("Enter the number of rows: "))

for i in range(1,num+1):
    for j in range(num+2,i+1,-1):
        print(i, end=" ")
    print()

for i in range(1,num):
    for j in range(i+1):
        print(num-i, end=" ")
    print()