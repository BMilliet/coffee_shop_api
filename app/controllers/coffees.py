from flask import request
from app.models import coffee
from app.support import app_strings
from app.services import db_manager, query_manager
import json


def api_info() -> str:
    return jsonify(app_strings.api_info())


def all_coffees() -> str:
    query = query_manager.select_all()
    results = db_manager.requestDB(db_manager.dbQuery, query)
    return json.dumps({'results': results})


def coffees_id(id) -> str:
    query = query_manager.select_where(str(id))
    results = db_manager.requestDB(db_manager.dbQuery, query)
    return json.dumps({'result': results})


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
    result = {
        'status': 'new coffee added',
        'coffee': coffee_object.represent()
    }
    return json.dumps(result)
