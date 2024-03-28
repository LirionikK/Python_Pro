class Vehacle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка - {self.make}, модель - {self.model}"


class Electric:
    def __init__(self):
        self.__battery = 0

    def charge(self):
        self.__battery = 100


class Car(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class Moto(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class ElectricCar (Vehacle, Electric):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class ElectricMoto (Vehacle, Electric):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


car = Car("Toyota", "Camry", 4)
moto = Moto("Honda", "CB400", 2)
elec_car = ElectricCar("Tesla", "Model S", 4)
elec_moto = ElectricMoto("Zero", "SR", 2)
print(car.get_info())
print(moto.get_info())
print(elec_car.get_info())
print(elec_moto.get_info())

print(Car.mro())
print(Moto.mro())
print(ElectricCar.mro())
print(ElectricCar.mro())
