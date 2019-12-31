from app import app
from typing import List, Dict
from flask import jsonify
import mysql.connector
import json

info = {
    'name':
    'Coffee shop Api',
    'description':
    'Welcome to the Coffee shop! This is an Api made in Python 3 with Falsk'
}


def all_coffees() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM coffees')
    results = [{name: description} for (name, description) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/', methods=['GET'])
def welcome():
    return jsonify(info), 200


@app.route('/allCoffees')
def index() -> str:
    return json.dumps({'coffees': all_coffees()})


@app.route('/hello')
def hello():
    return 'Hello World!'
