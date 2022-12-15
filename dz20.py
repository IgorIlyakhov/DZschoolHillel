def add_one(x):
    x = int(''.join(map(str, x))) + 1
    y = []
    while x > 0:
        y.append(x % 10)
        x //= 10
        y.reverse()
    return y


list_1 = [9, 9, 9, 9]
print(add_one(list_1))
