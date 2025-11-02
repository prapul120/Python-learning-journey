# While loop = Execute some code while some condition remains True

# name = input("Enter you name: ")

'''
while name == "":
    print("You did not enter your name")
    name = input("Enter you name: ")
print(f"hello {name}")


food = input("Enter your fav food (q to quit):")
while not food == 'q':
    print(f"Your fav food is {food}")
    food = input("Enter your another fav food (q to quit):")
print(f"bye")
'''

num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print(f"{num} is an invalid number")
    num = int(input("Enter the number between 1 and 10: "))
print(f"Your number is {num}")
