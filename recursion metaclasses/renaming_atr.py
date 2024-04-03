class RenameMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith('__'):
                new_attr_name = f'__private_{attr_name[2:]}'
                new_attrs[new_attr_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)


class MyClass(metaclass=RenameMeta):
    __private_var = 10
    public_var = 20
