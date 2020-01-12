class CoffeeModel:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Checkout:
    def __init__(self, cart, total):
        self.cart = cart
        self.total = total
