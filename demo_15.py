temp = float(input("enter the temperature: "))
raining = False

if temp >= 35 or temp <= 0 or raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")