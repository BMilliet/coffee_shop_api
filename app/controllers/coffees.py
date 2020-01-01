from app import app
from typing import List, Dict
from flask import jsonify
from app.services import db_manager, db_query
import mysql.connector
import json


def api_info() -> Dict:
    info = {
        'name':
        'Coffee shop Api',
        'description':
        'Welcome to the Coffee shop! This is an Api made in Python 3 with Flask'
    }
    return info


def all_coffees() -> List[Dict]:
    results = db_manager.executeDBQuery(db_query.SELECTALL)
    return results


def coffees_id(id) -> List[Dict]:
    results = db_manager.executeDBQuery(db_query.SELECTWHEREID + str(id))
    return results


def delete_from_id(id) -> str:
    db_manager.requestDBChange(db_query.DELETEWHEREID + str(id))
    return 'delete coffee with id ' + str(id)
