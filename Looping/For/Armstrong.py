num = int(input("Enter the number:"))
st = str(num)
le = len(st)
armsum = 0
for i in st:
    inum=int(i)
    armsum+=inum**le
if armsum==num:
    print("Armstrong number")
else:
    print("Not armstrong number")

