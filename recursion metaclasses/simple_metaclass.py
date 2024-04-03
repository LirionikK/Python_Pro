class Meta(type):
    def __new__(cls, name, bases, attrs):
        print('Creating class object')
        return super().__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        super().__init__(name, bases, attrs)


class MyClass(metaclass=Meta):
    pass
