import json

from flask import request

from app import app, database
from app.models import Coffee


def fetchAll() -> list:
    coffees = database.get_all(Coffee)
    all_coffees = []
    for coffee in coffees:
        new_coffee = coffee.representation()
        all_coffees.append(new_coffee)
    return all_coffees


def add() -> str:
    data = request.get_json(force=True)
    database.add_instance(Coffee,
                          name=data['name'],
                          price=data['price'],
                          details=data['details'])


def remove(coffee_id):
    database.delete_instance(Coffee, id=coffee_id)


def edit(coffee_id):
    data = request.get_json(force=True)
    database.edit_instance(Coffee, id=coffee_id, price=data['price'])
