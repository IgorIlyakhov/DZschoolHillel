l1 = [12, 3, 4, 10, 8]
x = len(l1)
print(l1)
if x == 0:
    print(l1)
else:
    a = l1.pop()
    l1.insert(0, a)
    print(l1)
