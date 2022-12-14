x = input('type digit: ')
while len(x) > 1:
    y = 1
    for i in x:
        y = y * int(i)
    x = str(y)
print(x)
