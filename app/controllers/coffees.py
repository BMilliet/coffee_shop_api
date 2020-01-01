from typing import List, Dict
from flask import request
from app.models import coffee
from app.services import db_manager, query_manager


def api_info() -> Dict:
    info = {
        'name':
        'Coffee shop Api',
        'description':
        'Welcome to the Coffee shop! This is an Api made in Python 3 with Flask'
    }
    return info


def all_coffees() -> List[Dict]:
    query = query_manager.select_all()
    results = db_manager.requestDB(db_manager.dbQuery, query)
    return results


def coffees_id(id) -> List[Dict]:
    query = query_manager.select_where(str(id))
    results = db_manager.requestDB(db_manager.dbQuery, query)
    return results


def delete_from_id(id) -> str:
    query = query_manager.delete_where(str(id))
    db_manager.requestDB(db_manager.dbChange, query)
    return 'delete coffee with id ' + str(id)


def insert_item() -> str:
    data = request.get_json(force=True)
    coffee_object = coffee.coffee_from_json(data)
    values = coffee_object.to_db_values()
    query = query_manager.insert_new(values)
    db_manager.requestDB(db_manager.dbChange, query)
    return 'added new coffee'
