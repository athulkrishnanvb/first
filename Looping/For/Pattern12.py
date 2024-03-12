num = int(input("Enter the number: "))

for i in range(num):
    for j in range(num-i):
        print(num-j, end=" ")
    print()

for i in range(1,num):
    for j in range(i+1):
        print(num-j, end=" ")
    print()