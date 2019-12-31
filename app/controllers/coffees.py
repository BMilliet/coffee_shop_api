from app import app
from typing import List, Dict
from flask import jsonify
import mysql.connector
import json


def api_info() -> Dict:
    info = {
        'name':
        'Coffee shop Api',
        'description':
        'Welcome to the Coffee shop! This is an Api made in Python 3 with Falsk'
    }
    return info


def db_config() -> Dict:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_db'
    }
    return config


def all_coffees() -> List[Dict]:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM coffees')
    results = [{
        name: description,
        id: id
    } for (name, description, id) in cursor]
    cursor.close()
    connection.close()

    return results


def coffees_id(id) -> List[Dict]:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM coffees where id= ' + str(id))
    results = [{
        name: description,
        id: id
    } for (name, description, id) in cursor]
    cursor.close()
    connection.close()

    return results
