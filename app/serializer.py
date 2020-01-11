import json
from .models import *


def checkoutTojson(coffees) -> str:
    cart = list(coffeeFromJson(coffee) for coffee in coffees)
    total = sum(item.price for item in cart)
    checkout = {'cart': coffees, 'total': total}
    return json.dumps(checkout)


def coffeeFromJson(json) -> CoffeeModel:
    return CoffeeModel(name=json['name'], price=json['price'])


# def receiptToJson() -> str:

#     return json.dumps("")


# def checkoutFromJson() -> Checkout:
#     json = request.get_json(force=True)
#     return Checkout(cart=json['cart'], total=json['total'])
