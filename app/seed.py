from . import database
from .migration import Coffee


def populate_db():
    coffee_list = [{
        'name':
        'Espresso',
        'price':
        3.80,
        'details':
        'Espresso is made by forcing very hot water under high pressure through finely ground compacted coffee. Tamping down the coffee promotes the waters even penetration through the grounds.'
    }, {
        'name':
        'Double Espresso',
        'price':
        4.20,
        'details':
        'Espresso is made by forcing very hot water under high pressure through finely ground compacted coffee. Tamping down the coffee promotes the waters even penetration through the grounds.'
    }, {
        'name':
        'Capuccino',
        'price':
        4.50,
        'details':
        'When a barista vaporizes milk for cappuccino, it creates a "micro-foam" by introducing small air bubbles into the milk, giving it a velvety, creamy and shiny texture.'
    }, {
        'name':
        'Mocha',
        'price':
        4.25,
        'details':
        'Like a coffee latte, coffee mocha is based on espresso and hot milk but with added chocolate flavouring and sweetener, typically in the form of cocoa powder and sugar.'
    }]

    for coffee in coffee_list:
        database.add_instance(Coffee,
                              name=coffee['name'],
                              price=coffee['price'],
                              details=coffee['details'])
