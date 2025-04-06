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

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

mycar = Car("Tata", "Nano")
mytesla = ElectricCar("Tesla", "Model S", "85kwh")
print(mycar.get_brand())
print(mycar.general_description())
print(Car.general_description())

mycar.__model = "XUV"
print(mycar.__model) # This will raise an error because __model is private
print(mycar.model) # This will work because model is a property

print(isinstance(mycar, Car)) # True
print(isinstance(mytesla, ElectricCar)) # True
print(isinstance(mytesla, Car)) # True
print(isinstance(mycar, ElectricCar)) # False