def test_fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a # yield is a keyword that is used like return, except the function will return a generator.
        a, b = b, a + b

for i in test_fib(10):
    print(i)
