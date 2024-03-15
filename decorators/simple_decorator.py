def called_decorator(func):

    def inner(*args, **kwargs):
        print("Function is been called")
        func(*args, **kwargs)
        print("Function is been called")

    return inner


@called_decorator
def some_func(a, b):
    print(f"a + b = {a+b}")


some_func(3, 5)
