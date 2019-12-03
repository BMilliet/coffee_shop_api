from flask import Flask, jsonify

app = Flask(__name__)

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


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/coffees', methods=['GET'])
def allCoffees():
    return jsonify(coffees), 200


@app.route('/coffees/<int:type>', methods=['GET'])
def coffeesByType(coffeeType):
    coffee_list = [
        coffee for coffee in coffees if coffee['type'] == coffeeType
    ]
    return jsonify(coffee_list), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
