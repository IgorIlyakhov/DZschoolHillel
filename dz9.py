import random
list_1 = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print(list_1)
print([list_1[0]] + [list_1[3]] + [list_1[-2]])
