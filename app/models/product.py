from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from associations import products_to_orders_association_table

from db import db

class Product(db.Model):
    """A Product class"""

    __tablename__ = "products"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Company", back_populates="products")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """Display when printing a Product object"""

        return "<Product: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
