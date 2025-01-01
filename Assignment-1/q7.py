# What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# Solution:
# Mutable data types can be changed after they are created, and immutable data types cannot be changed after they are created.
# Mutable data types: list
# Immutable data types: string
# Example:
mutable = [1, 2, 3, 4, 5]
print(mutable)
mutable[0] = 10
print(mutable)
immutable = "Hello"
print(immutable)
immutable[0] = "h" # This will give an error
print(immutable)
