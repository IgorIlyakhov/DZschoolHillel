def difference(*x):
    if not x:
        return 0
    else:
        y = max(*x) - min(*x)
        return y


print(round(difference(5, -5), 2))
