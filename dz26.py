import string


def first_word(x):
    string.punctuation = string.punctuation.replace("'", '')
    for i in string.punctuation:
        x = x.replace(i, ' ')
    x = x.split()[0]
    return x


print(first_word("Hello world"))