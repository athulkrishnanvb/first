tem = float(input("Enter the temperature in celsius:"))
if tem<-273.15:
    print("Invailed temperature")
elif tem==-273.15:
    print("temperature is absolute Zero")
elif -273.15<tem<0:
    print("temperature is below freezing point")
elif tem==0:
    print("temperature at freezing point")
elif 0<tem<100:
    print("temperature is normal")
elif tem==100:
    print("Boiling point")
elif tem>100:
    print("Temperature above boiling point")