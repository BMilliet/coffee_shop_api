class CoffeeModel:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Checkout:
    def __init__(self, cart, total):
        self.cart = cart
        self.total = total

    def representation(this) -> str:
        return {'card': this.cart, 'total': this.total}


class Receipt:
    def __init__(self, checkout, payment):
        self.checkout = checkout
        self.payment = payment
