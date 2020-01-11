class CoffeeModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Checkout:
    def __init__(self, cart, total):
        self.cart = cart
        self.total = total
