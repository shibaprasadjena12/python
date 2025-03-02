print(range(10))

print(list(range(10)))

myrng = iter(range(10))

print(next(myrng))

print(next(myrng))

print(next(myrng))

for i in myrng:
    print(i)