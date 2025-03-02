myRandomlist = [721, -82, "chiku", 99.67, 34 + 7j, "jeena", 72, -98.6, [34, "Kandhei", "Lona", 66,-34 + 7j], 0, 0.0, 0j, "Kandhei", "Lona", 66, -34 + 7j]

myIntList = []
def extarctInt(mylist):
    for i in myRandomlist:
        if type(i) == int or type(i) == float:
            myIntList.append(i)
        elif type(i) == list:
            for j in i:
                if type(j) == int or type(j) == float:
                    myIntList.append(j)

extarctInt(myRandomlist)

print(myIntList)