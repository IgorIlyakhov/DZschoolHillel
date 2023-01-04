class Item:

    def __init__(self, name, price, decription, demensions):
        self.price = price
        self.decription = decription
        self.demensions = demensions
        self.name = name

    def __str__(self):
        return f'Item: {self.name} at {self.price}$ per pcs, color: {self.decription}; size: {self.demensions}'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'Buyer: {self.name} {self.surname} (number: {self.numberphone})'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        name = ''
        for x, y in self.products.items():
            name += f'\n\t{x.name}: {y} pcs.'
        return f'{self.user.name} {self.user.surname}:{name}'

    def get_total(self):
        total = 0
        for x, y in self.products.items():
            total += x.price * y
        return f'The price of your items: {total}$'


lemon = Item('lemon', 5, "yellow", "small",)
apple = Item('apple', 2, "red", "middle", )

print(lemon)
print(apple)

buyer = User("Ivan", "Ivanov", "123456789")
print(buyer)

cart_1 = Purchase(buyer)
cart_1.add_item(lemon, 4)
cart_1.add_item(apple, 50)
print(cart_1)
print(cart_1.get_total())
