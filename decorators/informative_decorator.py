def function_info(func):

    def inner(*args, **kwargs):
        print(f"{func.__name__} is been called with parameters: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} return this value: {result}")
        return result
    return inner


@function_info
def add_func(a, b):
    return a+b


print(add_func(3, 5))
