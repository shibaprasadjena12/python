# create two class battery and engine and let the ElectricCar class inherit from both of them


class Car:
    def __init__(self, brand, model): # Constructor
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "This is a car is a vehicle that is designed to transport passengers."
    @property
    def model(self):
        return self.__model
class Battery:
    def battery_info(self):
        return "This is a battery."
class Engine:
    @property
    def engine_info(self):
        return "This is an engine."

class ElectricCarTwo(Car, Battery, Engine):
    pass
# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

mycar = Car("Tata", "Nano")
mytesla = ElectricCar("Tesla", "Model S", "85kwh")

myelectriccar2 = ElectricCarTwo("Audi", "Q4")

print(myelectriccar2.engine_info) # This will work because engine_info is a property
print(myelectriccar2.battery_info())

