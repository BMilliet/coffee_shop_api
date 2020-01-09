import json

from flask import request

from app import app, database
from app.models import Coffee


def hello() -> str:
    return 'Hello World!'


def fetchAll() -> str:
    coffees = database.get_all(Coffee)
    all_coffees = []
    for coffee in coffees:
        new_coffee = {
            "id": coffee.id,
            "name": coffee.name,
            "price": coffee.price,
            "details": coffee.details
        }

        all_coffees.append(new_coffee)
    return json.dumps(all_coffees)


def add() -> str:
    data = request.get_json(force=True)
    name = data['name']
    price = data['price']
    details = data['details']

    database.add_instance(Coffee, name=name, price=price, details=details)
    return json.dumps("Added")


def remove(coffee_id) -> str:
    database.delete_instance(Coffee, id=coffee_id)
    return json.dumps("Deleted")


def edit(coffee_id) -> str:
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Coffee, id=coffee_id, price=new_price)
    return json.dumps("Edited")
