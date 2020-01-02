from typing import List, Dict
import psycopg2


def dbChange(query, cursor, connection) -> None:
    cursor.execute(query)
    connection.commit()
    return None


def dbQuery(query, cursor, connection) -> List[Dict]:
    cursor.execute(query)
    results = resultFormat(cursor)
    return results


def requestDB(callback, query) -> List[Dict]:
    config = db_config()
    connection = psycopg2.connect(**config)
    cursor = connection.cursor()
    result = callback(query, cursor, connection)
    cursor.close()
    connection.close()
    return result


def resultFormat(cursor) -> List[Dict]:
    resultFormat = [{
        'name': name,
        'description': description,
        'id': id
    } for (id, name, description) in cursor]
    return resultFormat


def db_config() -> Dict:
    config = {
        'user': 'postgres',
        'password': 'root',
        'host': 'db',
        'database': 'coffee_db'
    }
    return config
