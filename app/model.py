from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Coffee(db.Model):
    __tablename__ = 'coffee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Numeric(asdecimal=False))
    details = db.Column(db.String(200))

    def representation(this) -> dict:
        return {
            "id": this.id,
            "name": this.name,
            "price": this.price,
            "details": this.details
        }


class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True)
    coffee_ids = db.Column(db.ARRAY(db.Integer))
    total = db.Column(db.Numeric(asdecimal=False))
    payment = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.now())

    def representation(this) -> dict:
        return {
            "id":
            this.id,
            "coffee_ids":
            this.coffee_ids,
            "total":
            this.total,
            "payment":
            this.payment,
            "date":
            datetime.utcfromtimestamp(
                this.date.timestamp()).strftime('%Y-%m-%d %H:%M:%S')
        }
