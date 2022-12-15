def find_unique_value(x):
    for i in x:
        if x.count(i) <= 1:
            return i


print(find_unique_value([1, 7, 1, 1]))
