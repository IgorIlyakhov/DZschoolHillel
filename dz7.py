list_1 = [0, 1, 0, 3, 12]
list_2, list_3 = [], []
for i in list_1:
    if i == 0:
        list_3.append(i)
    else:
        list_2.append(i)
list_2 += list_3
print(list_2)