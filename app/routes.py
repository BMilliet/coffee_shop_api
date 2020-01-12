from . import app, controller


@app.route('/hello', methods=['GET'])
def hello() -> str:
    return 'Hello World!', 200


@app.route('/allCaffee', methods=['GET'])
def fetchAllCaffee() -> str:
    return controller.fetchAllCaffee(), 200


@app.route('/allReceipt', methods=['GET'])
def fetchAllReceipt() -> str:
    return controller.fetchAllReceipt(), 200


@app.route('/select/<coffee_id>', methods=['GET'])
def select(coffee_id) -> str:
    return controller.select(coffee_id), 200


@app.route('/addCoffee', methods=['POST'])
def addCoffee() -> str:
    return controller.addCoffee(), 200


@app.route('/addReceipt', methods=['POST'])
def addReceipt() -> str:
    return controller.addReceipt(), 200


@app.route('/checkout', methods=['POST'])
def checkout() -> str:
    return controller.checkout(), 200


@app.route('/receipt', methods=['POST'])
def receipt() -> str:
    return controller.receipt(), 200


@app.route('/remove/<coffee_id>', methods=['DELETE'])
def remove(coffee_id) -> str:
    return controller.remove(coffee_id), 200


@app.route('/edit/<coffee_id>', methods=['PATCH'])
def edit(coffee_id) -> str:
    return controller.edit(coffee_id), 200
