def rev(n):
    rev = 0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev)
num = int(input("Enter the number:"))
rev(num)