import json

from app import app, db_manager, representer


def hello() -> str:
    return 'Hello World!'


def fetchAll() -> str:
    return json.dumps(db_manager.fetchAll())


def add() -> str:
    db_manager.add()
    return json.dumps("Added")


def remove(coffee_id) -> str:
    db_manager.remove()
    return json.dumps("Deleted")


def edit(coffee_id) -> str:
    db_manager.edit()
    return json.dumps("Edited")


def select(coffee_id) -> str:
    return json.dumps(db_manager.select(coffee_id))


def select_ids(coffee_ids) -> str:
    return json.dumps(db_manager.select_ids(coffee_ids))


def checkout() -> str:
    return representer.checkout()
