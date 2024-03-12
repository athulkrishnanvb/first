list1 = "athuleoi"
vawlist = []
nonvaw = []
for  i in list1:
    if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i" or i=="O" or i=="o" or i=="U" or i=="u":
        vawlist.append(i)
    else:
        nonvaw.append(i)
print("vawals:",vawlist)
print("nonvawals:",nonvaw)