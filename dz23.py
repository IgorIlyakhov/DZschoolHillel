def popular_words(x, y):

    x = x.lower().split()
    a = {}

    for i in y:
        if i in x:
            a[i] = x.count(i)
        else:
            a[i] = 0
    return a


print(popular_words('''When I was One I had just begun When I was Two I was nearly new''', ['i', 'was', 'three', 'near']))
