def generate_cube_numbers(x):
    p = 2
    while True:
        y = p**3
        p += 1
        if x > y:
            yield y
        else:
            break


print(list(generate_cube_numbers(100)))
