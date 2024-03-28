class Vehacle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка - {self.make}, модель - {self.model}"


class Car(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class Moto(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


car = Car("Toyota", "Camry", 4)
moto = Moto("Honda", "CB400", 2)
print(car.get_info())
print(moto.get_info())
