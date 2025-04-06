class Car:
    def __init__(self, brand, model): # Constructor
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "This is a car is a vehicle that is designed to transport passengers."

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

mycar = Car("Tata", "Nano")
print(mycar.general_description())
print(Car.general_description())