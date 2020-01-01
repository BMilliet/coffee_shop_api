from typing import List, Dict
from flask import jsonify
import mysql.connector
import json


def resultFormat(cursor) -> List[Dict]:
    resultFormat = [{
        'name': name,
        'description': description,
        'id': id
    } for (id, name, description) in cursor]
    return resultFormat


def requestDBChange(query) -> None:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return None


def executeDBQuery(query) -> List[Dict]:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    results = resultFormat(cursor)
    cursor.close()
    connection.close()
    return results


def requestDB(query, callback) -> None:
    config = db_config()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    callback(cursor, connection)
    cursor.close()
    connection.close()


def db_config() -> Dict:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_db'
    }
    return config
