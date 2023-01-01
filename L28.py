def prime_generator(x):
    p = 2
    while p < x:
        y = True
        for num in range(2, p):
            if p % num == 0:
                y = False
                break
        if y:
            yield p
        p += 1


print(list(prime_generator(10)))
