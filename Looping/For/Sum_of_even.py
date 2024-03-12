num = int(input("Entr the numbers:"))
evensum = 0
for i in range(0,num+1):
    if i%2==0:
        evensum+=num
print("Sum of even :",evensum)
