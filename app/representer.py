import json

from flask import request
from .db_manager import *


def checkout() -> str:
    coffees = request.get_json(force=True)
    coffee_list = list(select(item['id']) for item in coffees)
    total = sum(item['price'] for item in coffee_list)
    checkout = {'cart': coffee_list, 'total': total}
    return json.dumps(checkout)


def receipt() -> str:
    data = request.get_json(force=True)
    checkout = {'cart': data['cart'], 'total': data['total']}
    payment = data['form_of_payment']
    receipt = {
        'checkout': checkout.representation(),
        'form_of_payment': payment
    }
    return json.dumps(receipt)
