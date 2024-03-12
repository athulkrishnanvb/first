num = int(input("Enter the number:"))
fib = [0,1]
for i in range(2,num):
    new = fib[-1]+fib[-2]
    fib.append(new)
print(fib)
