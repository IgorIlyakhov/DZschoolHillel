import string


def is_palindrome(x):

    x = x.lower().replace(' ', '')
    for i in string.punctuation:
        x = x.replace(i, '')
    y = x[::-1]
    return x == y


print(is_palindrome('OP'))
