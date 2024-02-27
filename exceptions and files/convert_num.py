num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    number1 = int(num1)
    number2 = int(num2)
except ValueError:
    print("Incorrect data entered. You need to enter numbers.")
else:
    print("First number:", number1)
    print("Second number:", number2)
