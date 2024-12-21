import time


def t_l(f):
    def w(*a, **k):
        s = time.time()
        try:
            r = f(*a, **k)
        except Exception as e:
            r = f"err: {e}"
        t = time.time() - s
        with open("log.txt", "a") as log:
            log.write(f"{f.__name__}: {t:.4f}s\n")
        return r

    return w


@t_l
def c(a, b):
    time.sleep(1)
    return a + b


@t_l
def d(a, b):
    return a / b


@t_l
def fail(x):
    return x / 0


@t_l
def square(x):
    return x * x




print(c(3, 4))
print(d(10, 2))
print(fail(5))
print(square(5))
