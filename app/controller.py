import json

from app import app, db_manager


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
