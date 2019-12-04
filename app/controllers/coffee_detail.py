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


@app.route('/coffees/<int:type>', methods=['GET'])
def coffeesByType(type):
    coffee_list = [coffee for coffee in coffees if coffee['type'] == type]
    return jsonify(coffee_list), 200
