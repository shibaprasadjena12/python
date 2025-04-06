class Farmer:
    def __init__(self, name, age, village):
        self.__name = name
        self.__age = age
        self.__village = village
        self.__crop = None
        self.__lone = None

    def set_crop(self, crop):
        self.__crop = crop

    def get_crop(self):
        return self.__crop
    def set_lone(self, lone):
        self.__lone = lone
    def get_lone(self):
        return self.__lone
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_village(self):
        return self.__village
    
myfarmer = Farmer("John", 35, "Green Valley")
myfarmer.set_crop("Wheat")
myfarmer.set_lone(1000)
print(f"Farmer Name: {myfarmer.get_name()}")
print(f"Farmer Age: {myfarmer.get_age()}")
print(f"Farmer Village: {myfarmer.get_village()}")
print(f"Farmer Crop: {myfarmer.get_crop()}")
print(f"Farmer Lone: {myfarmer.get_lone()}")
# Output:
# Farmer Name: John
# Farmer Age: 35
# Farmer Village: Green Valley
# Farmer Crop: Wheat
# Farmer Lone: 1000
# The code defines a Farmer class with private attributes for name, age, village, crop, and lone.
# It provides methods to set and get these attributes, demonstrating encapsulation in Python.
# The Farmer object is created and its attributes are set and retrieved using the provided methods.
# This encapsulation helps to protect the data and restrict direct access to the attributes.
# The code also demonstrates the use of getter and setter methods to access and modify private attributes.
