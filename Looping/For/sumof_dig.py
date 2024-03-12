num = int(input("Enter the number:"))
st = str(num)
sum = 0
for i in st:
    inum=int(i)
    sum+=inum 
    if sum>9:
        stsum=str(sum)
        sum=0
        for i in stsum:
            inu=int(i)
            sum+=inu
print(sum)
