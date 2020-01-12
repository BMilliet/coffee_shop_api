import json
from .models import *
from .db_manager import *


def checkoutTojson(coffees) -> str:
    coffee_list = list(select(item['id']) for item in coffees)
    total = sum(item['price'] for item in coffee_list)
    checkout = {'cart': coffee_list, 'total': total}
    return json.dumps(checkout)
