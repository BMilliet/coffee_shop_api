from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Coffee(db.Model):
    __tablename__ = 'coffee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Numeric(asdecimal=False))
    details = db.Column(db.String(200))
