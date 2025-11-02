# LCM finding program

a = int(input("Enter the vlaue to find LCM: "))

for b in range(2,101):

    if a / b:
        print(f"{b}|{a}")
    elif a % b == 0:
        print(f"{b}|{a}")
        break
