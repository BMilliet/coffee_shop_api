from flask_sqlalchemy import SQLAlchemy

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
