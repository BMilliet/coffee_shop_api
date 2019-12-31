from typing import List, Dict
from flask import jsonify
import mysql.connector
import json


def resultFormat(cursor) -> List[Dict]:
    resultFormat = [{
        name: description,
        id: id
    } for (name, description, id) in cursor]
    return resultFormat


def executeDBQuery(query) -> List[Dict]:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    results = resultFormat(cursor)
    cursor.close()
    connection.close()

    return results


def db_config() -> Dict:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_db'
    }
    return config
