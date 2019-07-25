from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from db import db

class Company(db.Model):
    """A Company class"""

    __tablename__ = "companies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    products = db.relationship("Product", back_populates="company")

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products 

    def __repr__(self):
        """Display when printing a Company object"""

        return "<Company: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
