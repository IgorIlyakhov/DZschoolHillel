while True:
    x = float(input("Введіть значення числа x = "))
    c = input("Введіть функцію (+, -, *, /) = ")
    y = float(input("Введіть значення числа y = "))
    if c == "+":
        r = x + y
    elif c == "-":
        r = x - y
    elif c == "*":
        r = x * y
    elif y != 0:
        if c == "/":
            r = x / y
    elif y == 0:
        r = "Ділення на 0"
    print("Результат:", r)
    a = input('Рахуємо далі? ')
    if a == 'y' or a == 'yes':
        print('Продовжуємо:')
    else:
        break
