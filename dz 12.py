import string
x = input('hashtag:  ')
list_1, list_2, list_3 = list(x), [], []
for i in list_1:
    if i in string.punctuation:
        list_2.append(i)
    else:
        list_3.append(i)
y = "".join(list_3)
y = y.title()
y = y.replace(' ', '')
if len(y) > 139:
    print(f'#{y[:139]}')
else:
    print(f'#{y}')
