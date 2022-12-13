def common_elements(a, b):
    import random
    list_3, list_5 = [], []
    for i in range(random.randrange(a, a + 1)):
        list_3.append(random.randrange(0, 1_000, 3))
        list_3 = list_3[:a]
    for i in range(random.randrange(b, b + 1)):
        list_5.append(random.randrange(0, 1_000, 5))
        list_5 = list_5[:b]
    list_3 = set(list_3)
    list_5 = set(list_5)
    r = list_3.intersection(list_5)
    return r


x = int(input('Кількість чисел кратні 3 (0:1000): '))
y = int(input('Кількість чисел кратні 5 (0:1000): '))
print(common_elements(x, y))
