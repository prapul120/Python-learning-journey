#OR
'''
temp = float(input("enter the temperature: "))
raining = False

if temp >= 35 or temp <= 0 or raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''


# and & not

temp = float(input("Enter the temprature"))
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("it is synny")
elif temp <=0 and is_sunny:
    print("It is cold outside")
    print("it is synny")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside")
    print("it is synny")
elif temp >= 28 and not is_sunny:
    print("It is Hot outside")
    print("it is cloudy")
elif temp <=0 and not is_sunny:
    print("It is cold outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside")
    print("it is cloudy")