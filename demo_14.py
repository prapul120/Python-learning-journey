unit = input(" Is this temperature in celsius or fahrenheit (c/f) : ")
temp1 = float(input("Enter the temperature: "))

if unit == "c" or "C":
    temp = round((9 * temp1) / 5 + 32,1)
    print(f"The temperature in Fahrenheit is:{temp}")
elif unit == "f" or "F":
    temp = round((temp1 - 32) * 5 / 9,1)
    print(f"The temperature in celsius is:{temp}")
else:
    print(f"{unit} is an invalid unit of measurement !")