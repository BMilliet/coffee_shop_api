from app import app
from flask import jsonify
from app.controllers import coffees as controller
import json


@app.route('/', methods=['GET'])
def welcome():
    return jsonify(controller.api_info()), 200


@app.route('/allCoffees')
def index() -> str:
    return json.dumps({'coffees': controller.all_coffees()})


@app.route('/hello')
def hello():
    return 'Hello World!'
