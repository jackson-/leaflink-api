from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from associations import products_to_orders_association_table

from db import db
Base = declarative_base()


class Order(db.Model):
    """A Order class"""

    __tablename__ = "orders"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    products = db.relationship("Product", secondary=products_to_orders_association_table,
                            backref=db.backref('orders', lazy='dynamic'))

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        """Display when printing a Product object"""

        return "<Product: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
