num = int(input("Enter the number:"))
for i in range(num,0,-1):
    for j in range(i,num):
        print(j,end=" ")
    print()