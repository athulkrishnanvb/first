def prime(n):
    for i in range(2,num):
        if num%2==0:
            print("not prime")
            break
    else:
        print("Prime")
num = int(input("Enter the number:"))
prime(num)