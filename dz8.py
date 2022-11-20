list_1 = [1, 3, 5]
x = len(list_1)
y = sum(list_1[::2])
if x == 0:
    print(0)
else:
    print(y * list_1[-1])
