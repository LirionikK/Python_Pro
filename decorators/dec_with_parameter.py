import time


def sleeper(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            func(*args, **kwargs)
        return wrapper
    return decorator


@sleeper(5)
def some_func(num):
    for i in range(num):
        print("Hello")


some_func(3)
