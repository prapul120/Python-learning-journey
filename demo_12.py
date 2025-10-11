#python calculator

operator = input("Enter an operator (+ - x /): ")
num1 = float(int(input("Enter the first number: ")))
num2 = float(int(input("Enter the second number: ")))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if operator == '+':
    print(sum)
elif operator == '-':
    print(sub)
elif operator == 'x':
    print(mul)
elif operator == '/':
    print(div)
else:
    print("Enter an valid operator")