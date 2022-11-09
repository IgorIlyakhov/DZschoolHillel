digit = int(input('Введіть число: '))
x = 1000
left, right = divmod(digit, x)
print(left)
x = 100
left, right = divmod(right, x)
print(left)
x = 10
left, right = divmod(right, x)
print(left)
x = 1
left, right = divmod(right, x)
print(left)
