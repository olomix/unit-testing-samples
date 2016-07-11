from time import time


def timeit(cb):
    def timeit_(f):
        def wrapped(*args, **kwargs):
            start = time()
            res = f(*args, **kwargs)
            cb(time() - start)
            return res

        return wrapped
    return timeit_

def print_total(total):
    print(total)

@timeit(print_total)
def x():
    return 42

if __name__ == '__main__':
    print(x())