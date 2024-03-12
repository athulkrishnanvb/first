length = float(input("Enter a length in centimeters:"))
if length<0:
    print("Invalid")
else:
    con=length/2.54
    print(f"{length} centimeters is converted to {con:.3f} inches.")