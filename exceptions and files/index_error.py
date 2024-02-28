my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[10])
except IndexError:
    print("Invalid list index")
