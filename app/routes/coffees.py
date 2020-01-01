from app import app
from flask import jsonify
from app.controllers import coffees as controller
import json


@app.route('/', methods=['GET'])
def welcome():
    return jsonify(controller.api_info()), 200


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/allCoffees')
def index() -> str:
    return json.dumps({'results': controller.all_coffees()})


@app.route('/CoffeeId/<int:coffee_id>')
def coffee_by_id(coffee_id) -> str:
    return json.dumps({'result': controller.coffees_id(coffee_id)})


@app.route('/DeleteWhereId/<int:coffee_id>')
def delete_where_id(coffee_id) -> str:
    return json.dumps({'result': controller.delete_from_id(coffee_id)})
