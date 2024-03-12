tem = float(input("Enter the temperature:"))
uni = input("Enter the unit celsius or fahrenheit:")
if uni=="fahrenheit":
    convert_c=5/9*(tem-32)
    print("Celsius:",convert_c)
elif uni=="celsius":
    convert_f=(9/5*tem)+32
    print("Fahrenhiet:",convert_f)
else:
    print("Ivailed")