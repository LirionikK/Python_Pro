class Rectangle:
    def __init__(self, sid1, sid2) -> None:
        self.side1 = sid1
        self.side2 = sid2

    def square(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (self.side1 + self.side2) * 2


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()
print(f"Square: {square}")
print(f"Perimeter: {perimeter}")
