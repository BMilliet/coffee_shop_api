import json

from flask import request

from app import app, database
from app.migration import Coffee


def fetchAll() -> list:
    coffees = database.get_all(Coffee)
    return list(coffee.representation() for coffee in coffees)


def add() -> str:
    data = request.get_json(force=True)
    database.add_instance(Coffee,
                          name=data['name'],
                          price=data['price'],
                          details=data['details'])


def remove(coffee_id):
    database.delete_instance(Coffee, id=coffee_id)


def select(coffee_id):
    coffee = database.select(Coffee, coffee_id)
    return coffee.representation()


def select_ids(coffee_ids):
    selecteds = database.select_ids(Coffee, coffee_ids)
    return list(item.representation() for item in selecteds)


def edit(coffee_id):
    data = request.get_json(force=True)
    database.edit_instance(Coffee, id=coffee_id, price=data['price'])
