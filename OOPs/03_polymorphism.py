class Car:
    car_count = 0 # Class variable
    def __init__(self, brand, model): # Constructor
        self.__brand = brand
        self.model = model
        Car.car_count += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol"

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"

# mycar = Car("Tata", "Nano")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.full_name())

my_car2 = Car("Tata", "Nexon")
# print(my_car2.brand)
# print(my_car2.model)
# print(my_car2.full_name())

mytesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(mytesla.model)
# print
# print(mytesla.full_name())
# print(mytesla.__brand) # This will raise an error
print(mytesla.get_brand())

print(mytesla.fuel_type())

print(my_car2.fuel_type())
mycar3 = ElectricCar("Tata", "Nexon EV", "30kwh")
mycar4 = ElectricCar("Tata", "Nexon EV", "40kwh")
mycar5 = Car("Tata", "Nexon EV")

print(my_car2.car_count)