# list is a collection which is ordered and changeable. Allows duplicate members.
# it is a non-primitive data structure in python
# list is defined by using square brackets []
# list can have different data types
# list can have duplicate elements
# list can have nested lists
# list can have mutable elements

l1 = [23, 12, -34, "chiku", 23.45, True, 23, 45+6j, [12, 34, 56]]
print(type(l1)) # Output: <class 'list'>
print(l1[4]) # Output: 23.45
# print(l1[90]) # IndexError: list index out of range
print(l1[8][2]) # Output: 56
print(l1[:5])
l2 = [True, False, True]

print(l1+l2) # Output: [23, 12, -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], True, False, True]
l1.append(l2)
print(l1) # Output: [23, 12, -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], [True, False, True]]
l1.extend(l2)
print(l1) # [23, 12, -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], [True, False, True], True, False, True]
l1.insert(2, "Jeena")
print(l1) # Output: [23, 12, 'Jeena', -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], [True, False, True], True, False, True]
print(l1.__len__()) # Output: 14
print(len(l1)) # Output: 14
l1.pop()
print(l1) # Output: [23, 12, 'Jeena', -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], [True, False, True], True, False]
l1.pop(12)
print(l1) # Output: [23, 12, 'Jeena', -34, 'chiku', 23.45, True, 23, (45+6j), [12, 34, 56], [True, False, True], False]
l1.remove(True)
print(l1) # Output: [23, 12, 'Jeena', -34, 'chiku', 23.45, 23, (45+6j), [12, 34, 56], [True, False, True], False]
l1.reverse()
print(l1) # Output: [True, [True, False, True], [12, 34, 56], (45+6j), 23, 23.45, 'chiku', -34, 'Jeena', 12, 23]
# l1.sort()
# print(l1) # TypeError: '<' not supported between instances of 'list' and 'str'
l4 = [23, 12, -34, 23, 45]
l4.sort()
print(l4) # Output: [-34, 12, 23, 23, 45]
l4.sort(reverse = True)
print(l4) # Output: [45, 23, 23, 12, -34]   
l5 = ["Chiku", "Jeena", "Pinku", "Lona"]
l5.sort()
print(l5) # Output: ['Chiku', 'Jeena', 'Lona', 'Pinku']
l5.sort(reverse = True)
print(l5) # Output: ['Pinku', 'Lona', 'Jeena', 'Chiku']
print(l5.index("Jeena")) # Output: 2

s = "Rituparna"
s = s.replace("Ritu", "Chiku")
print(s) # Output: Chikuparna