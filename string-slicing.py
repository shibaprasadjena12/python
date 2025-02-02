myString = "My name is chiku"
print(myString[0:6]) # Output: 'My nam'
print(myString[11:16]) # Output: 'chiku'
print(myString[11:]) # Output: 'chiku'
print(myString[:10]) # Output: 'My name is'
print(myString[:]) # Output: 'My name is chiku'
print(myString[0:16:2]) # Output: 'M aei hku'
print(myString[::2]) # Output: 'M aei hku'
print(myString[::-1]) # Output: 'ukihc si eman yM'
print(myString[15:10:-1]) # Output: 'ukihc'
print(myString[-1:-17:-1]) # Output: 'ukihc si eman yM'

# String Slicing with step
# Syntax: [start:stop:step]
# start: Starting index of the substring
# stop: Ending index of the substring
# step: Step size of the slicing
# If the step value is not provided, it is considered as 1.

# Convert int to string

myInt = 103
myString = str(myInt)
print(type(myString)) # Output: <class 'str'>