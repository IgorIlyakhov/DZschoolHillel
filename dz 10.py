import string
import keyword
list_1 = input('Введіть строку:  ')
x = list_1[0]
if list_1.isdigit():
    list_1 = False
    print(list_1)
elif list_1 in keyword.kwlist:
    print(False)
elif x.isdigit():
    print(False)
elif not list_1.islower() and list_1 != '_':
    print(False)
else:
    y = True
    for i in string.punctuation:
        if i in list_1 and i != '_':
            y = False
    print(y)
