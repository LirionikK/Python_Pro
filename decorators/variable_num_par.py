def type_checker(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"No such type")
            return func(*args)
        return wrapper
    return decorator


@type_checker(int, bool)
def some_func(a, b):
    print(a, b)


some_func(2, "True")
