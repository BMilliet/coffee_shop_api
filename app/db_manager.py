import json

from flask import request

from app import app, database
from app.migration import Coffee, Receipt


def fetchAllCaffee() -> list:
    coffees = database.get_all(Coffee)
    return list(coffee.representation() for coffee in coffees)


def fetchAllReceipt() -> list:
    receipts = database.get_all(Receipt)
    return list(receipt.representation() for receipt in receipts)


def addCoffee() -> str:
    data = request.get_json(force=True)
    database.add_instance(Coffee,
                          name=data['name'],
                          price=data['price'],
                          details=data['details'])


def addReceipt() -> str:
    data = request.get_json(force=True)
    database.add_instance(Receipt,
                          coffee_ids=list(
                              item['id'] for item in data['checkout']['card']),
                          total=data['checkout']['total'],
                          payment=data['form_of_payment'])


def remove(coffee_id):
    database.delete_instance(Coffee, id=coffee_id)


def select(coffee_id):
    coffee = database.select(Coffee, coffee_id)
    return coffee.representation()


def edit(coffee_id):
    data = request.get_json(force=True)
    database.edit_instance(Coffee, id=coffee_id, price=data['price'])
