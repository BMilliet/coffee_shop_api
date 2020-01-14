import json

from app import app, db_manager, representer


def hello() -> str:
    return 'Hello World!'


def endpoints() -> str:
    return json.dumps({
        'endpoints': [
            '/allCaffee', '/allReceipt', '/select/1', '/addCoffee',
            '/addReceipt', '/checkout', '/receipt', '/remove/1', '/edit/1'
        ]
    })


def fetchAllCaffee() -> str:
    return json.dumps(db_manager.fetchAllCaffee())


def fetchAllReceipt() -> str:
    return json.dumps(db_manager.fetchAllReceipt())


def addCoffee() -> str:
    db_manager.addCoffee()
    return json.dumps("Added")


def addReceipt() -> str:
    db_manager.addReceipt()
    return json.dumps("Added")


def remove(coffee_id) -> str:
    db_manager.remove()
    return json.dumps("Deleted")


def edit(coffee_id) -> str:
    db_manager.edit()
    return json.dumps("Edited")


def select(coffee_id) -> str:
    return json.dumps(db_manager.select(coffee_id))


def checkout() -> str:
    return representer.checkout()


def receipt() -> str:
    return representer.receipt()
