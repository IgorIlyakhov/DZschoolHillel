def correct_sentence(y):
    x = y[0].upper() + y[1:]
    if y[-1] == '.':
        return x
    else:
        y = x + '.'
        return y


a = input('Enter your sentence: ')
print(f'=> {correct_sentence(a)}')
