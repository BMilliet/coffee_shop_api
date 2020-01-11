import json
from .models import *


def checkoutTojson(coffees) -> str:
    total = sum(coffee['price'] for coffee in coffees)
    checkout = {'cart': coffees, 'total': total}
    return json.dumps(checkout)


# def coffeeFromJson() -> CoffeeModel:
#     json = request.get_json(force=True)
#     return CoffeeModel(name=json['name'], price=json['price'])

# def checkoutFromJson() -> Checkout:
#     json = request.get_json(force=True)
#     return Checkout(cart=json['cart'], total=json['total'])
