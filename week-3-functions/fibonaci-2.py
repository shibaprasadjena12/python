def test_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

c = test_fib()

for i in range(10):
    print(next(c))