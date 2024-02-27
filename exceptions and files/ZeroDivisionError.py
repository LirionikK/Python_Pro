def division(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return None
    except ValueError:
        print("Incorrect input.")
        return None


first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

print(division(first_num, second_num))
