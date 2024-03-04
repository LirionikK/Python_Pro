class Vehicle:
    def __init__(self, name, speed, price) -> None:
        self.name = name
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        if isinstance(other, Vehicle):
            return self.speed == other.speed
        raise TypeError("Unsupported operand type for >")

    def __str__(self):
        return f"{self.name}: speed = {self.speed}, cost = {self.price}"


v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)
v3 = Vehicle("Name3", 90, 7000)
print(v1 > v2)

result = sorted([v1, v2, v3], key=lambda x: x.speed)
for i in result:
    print(i)
