def fib():
    x, y = 0, 1
    yield x
    while True:
        yield y
        t = y; y = x+y; x = t


if __name__ == '__main__':
    f = fib()
    print([next(f) for _ in range(11)])