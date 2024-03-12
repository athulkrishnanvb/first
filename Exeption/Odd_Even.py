try:
    n=int(input("Enter the number"))
    if n%2==0:
        print("Even")
    else:
        print("Odd")
except:
    print("error")
finally:
    print("Successs")