def pow_1(x):
    return x ** 2


def some_gen(begin, end, func):
    a = 0
    while end > a:
        yield begin
        begin = func(begin)
        a += 1


print(list(some_gen(2, 4, pow_1)))
