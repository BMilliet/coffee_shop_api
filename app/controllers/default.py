from app import app
from flask import jsonify

info = {
    'name':
    'Coffee shop Api',
    'description':
    'Welcome to the Coffee shop! This is an Api made in Python 3 with Falsk'
}


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify(info), 200
