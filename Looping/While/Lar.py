num = 278
lar = 0
while num!=0:
    d=num%10
    if lar<=d:
        lar=d
    num//=10
print(lar)


    