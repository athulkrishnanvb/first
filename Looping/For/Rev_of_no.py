num = 167
rev = 0
n = str(num)
l = len(n)
for i in range(l-1,-1,-1):
    d=int(n[i])
    rev=(rev*10)+d
print(rev)