from . import app, controller


@app.route('/hello', methods=['GET'])
def hello() -> str:
    return 'Hello World!', 200


@app.route('/all', methods=['GET'])
def fetchAll() -> str:
    return controller.fetchAll(), 200


@app.route('/add', methods=['POST'])
def add() -> str:
    return controller.add(), 200


@app.route('/remove/<coffee_id>', methods=['DELETE'])
def remove(coffee_id) -> str:
    return controller.remove(coffee_id), 200


@app.route('/edit/<coffee_id>', methods=['PATCH'])
def edit(coffee_id) -> str:
    return controller.edit(coffee_id), 200


@app.route('/checkout', methods=['POST'])
def checkout() -> str:
    return controller.checkout(), 200
