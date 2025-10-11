# Python weight converter

weight = float(input("Enter the weight: "))
unit = input("kilograms or pounds ? (K or L):")

if unit == 'K' or 'k':
    weight = weight * 2.205
    unit = 'kg'
    print(f"your weight is: {round(weight, 3)}{unit}")
elif unit == 'L' or 'l':
    weight = weight / 2.205
    unit = 'lbs'
    print(f"your weight is: {round(weight, 3)}{unit}")
else:
    print(f"{unit} is not valid")

