user_list = input("Enter a comma-separated list of numbers: ")

try:
    get_index = int(input("Enter index: "))
    int_list = [int(i) for i in user_list.split(',')]
    print(int_list[get_index])
except ValueError:
    print("Incorrect input. You must enter an integer")
except IndexError:
    print("Invalid list index")
