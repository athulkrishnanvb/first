num = int(input("Enter numbers:"))
n = num
rev = 0
while num!=0:
    d=num%10
    rev=(rev*10)+d
    num//=10
if rev==n:
    print("Palindrome")
else:
    print("Not palindrome")
