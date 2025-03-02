myRandomlist = [721, -82, "chiku", 99.67, 34 + 7j, "jeena", 72, -98.6, [34, "Kandhei", "Lona", 66,-34 + 7j], 0, 0.0, 0j, "Kandhei", "Lona", 66, -34 + 7j]

myIntList = []
def extarctInt(mylist):
    '''This function accepts a list as argument and extracts all the integers and floats from a list'''
    for i in mylist:
        if type(i) == int or type(i) == float:
            myIntList.append(i)
        elif type(i) == list:
            extarctInt(i)

extarctInt(myRandomlist)

print(myIntList)