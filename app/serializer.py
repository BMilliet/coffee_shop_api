import json
from .models import *
from .db_manager import *


def checkoutTojson(coffees) -> str:
    coffee_list = list(select_ids(item['id']) for item in coffees)
    cart = list(coffeeFromJson(coffee) for coffee in coffee_list)
    total = sum(item.price for item in cart)
    checkout = {'cart': coffees, 'total': total}
    return json.dumps(checkout)


def coffeeFromJson(json) -> CoffeeModel:
    return CoffeeModel(name=json['name'], price=json['price'])
