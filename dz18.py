def second_index(sent, ind):
    if sent.count(ind) > 1:
        x = sent.find(ind)
        x = sent.find(ind, x + 1)
        return x
    else:
        x = None
        return x


a = input('Ваш текст: ')
b = input('Потрібний індекс: ')
print(f'{second_index(a, b)}')
