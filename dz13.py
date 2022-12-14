import string
ascii_letters = string.ascii_letters
user_input = input('Type text: ')
x = ascii_letters.find(user_input[0])
y = ascii_letters.find(user_input[-1]) + 1
print(ascii_letters[x:y])
