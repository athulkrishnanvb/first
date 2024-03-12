def palin(n):
    pal = n
    rev = 0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n//=10
    if rev==pal:
        print("Palindrome")
    else:
        print("not")
num = int(input("Enter the number:"))
palin(num)
