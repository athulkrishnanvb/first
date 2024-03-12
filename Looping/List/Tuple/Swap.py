n1 = (2,3,4)
n2 = (5,6,7)
a = list(n1)
b = list(n2) 
a,b=b,a
a=tuple(a)
b=tuple(b)
print(a)
print(b)