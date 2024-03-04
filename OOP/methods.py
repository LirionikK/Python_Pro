class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, num):
        return cls(num / 2)

    @staticmethod
    def check_radius(rad_number):
        return rad_number > 0


circle = Circle.from_diameter(20)
area = circle.area()
print(f"Area = {area}")

valid = Circle.check_radius(25)
print(valid)
