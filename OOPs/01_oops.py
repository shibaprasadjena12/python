class Car:
    def __init__(self, brand, model): # Constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

mycar = Car("Tata", "Nano")
print(mycar.brand)
print(mycar.model)
print(mycar.full_name())

my_car2 = Car("Tata", "Nexon")
print(my_car2.brand)
print(my_car2.model)
print(my_car2.full_name())

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

mytesla = ElectricCar("Tesla", "Model S", "85kwh")
print(mytesla.model)
print(mytesla.full_name())

# Encapsulation
# Encapsulation is the bundling of data with the methods that operate on that data
# and restricting access to some components. This is a means of preventing unintended interference
# and misuse of the methods and data.
