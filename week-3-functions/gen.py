def my_gen():
    i = 0
    j = 0
    while True:
        i += 2
        yield j
        j = i

ev_num = my_gen()

for ev in range(10) :
    print(next(ev_num))
