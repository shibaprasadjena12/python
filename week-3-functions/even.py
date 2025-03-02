def test_even():
    a = 0
    while True:
        yield a
        a += 2

ev_num =  test_even()

for i in range(100):
    print(next(ev_num))