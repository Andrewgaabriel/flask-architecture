from pydaria.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(140))
        price = db.Column(db.Float)
        description = db.Column(db.Text())