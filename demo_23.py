# Python Compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle <=0:
        print("Principal can't be less than or equal to zero")
    else:
        break

while rate <= 0:
    rate =float(input("Enter the intrest rate: "))
    if rate <=0:
        print("Intrest rate can't be less than or equal to zero")

while time <= 0:
    time =int(input("Enter the time in years: "))
    if time <=0:
        print("Time rate can't be less than or equal to zero")

total = principle * pow(( 1 + rate / 100 ),time)
print(f"Balance after {time} year/s : {total:.2f}")

