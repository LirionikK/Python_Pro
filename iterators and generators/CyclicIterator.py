class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


cyclic_iter = CyclicIterator([1, 2, 3])
for i in cyclic_iter:
    print(i)
