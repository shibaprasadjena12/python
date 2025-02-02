s1 = "I am learning Python programing language"
print(len(s1))
print(s1.find("Python"))
print(s1.find("i"))
print(s1.find("i", 12)) # index of first i after 12th index
print(s1.find("i", 12, 18)) # index of first i between 12th and 18th index
print(s1.count("i"))
print(s1.count('z'))    # returns 0 if the substring is not found
print(s1.count('i', 12, 18)) # count of i between 12th and 18th index
print(s1.replace("Python", "Java")) # replace Python with Java
print(s1) # original string is not modified
print(s1.upper())   # convert to uppercase
print(s1) # original string is not modified
print(s1.lower())   # convert to lowercase
print(s1.title())   # convert to title case
print(s1.capitalize())   # convert to title case
print(s1.swapcase())   # swap the case of each character
print(s1 * 3)   # repeat the string 3 times
print(s1 + "!!!")   # concatenate !!! to the string

# comments in python
# single line comment
"""
multi line comment
"""
'''
multi line comment
'''