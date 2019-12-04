from app import app
from flask import jsonify

coffees = [{
    'name': 'espresso',
    'type': 1,
    'price': 3.50
}, {
    'name': 'double espresso',
    'type': 1,
    'price': 6.00
}, {
    'name': 'cappuccino',
    'type': 2,
    'price': 6.00
}]


@app.route('/coffees', methods=['GET'])
def allCoffees():
    return jsonify(coffees), 200
