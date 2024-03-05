class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.get_count_calls = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def method_called(self):
        self.get_count_calls += 1
        return self.get_count_calls


c1 = Counter()
c2 = Counter()

print(c1.get_count())  # 2
print(c1.method_called())  # 1
