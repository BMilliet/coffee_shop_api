import json

from flask import request
from .serializer import *


def checkout() -> str:
    coffees = request.get_json(force=True)
    return checkoutTojson(coffees)


# def receipt() -> str:
