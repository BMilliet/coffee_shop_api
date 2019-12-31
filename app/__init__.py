from flask import Flask, jsonify

app = Flask(__name__)

from app.controllers import default
