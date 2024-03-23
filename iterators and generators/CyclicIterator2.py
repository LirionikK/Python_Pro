class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.buffer = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.buffer:
            self.buffer.append(next(self.iterator))
        value = self.buffer.pop(0)
        self.buffer.append(next(self.iterator))
        return value

    def peek(self):
        if not self.buffer:
            self.buffer.append(next(self.iterator))
        return self.buffer[0]


cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))
print(cycle_iter.peek())
print(next(cycle_iter))
