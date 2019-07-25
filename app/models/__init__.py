
from flask_sqlalchemy import SQLAlchemy

from db import db
from .associations import products_to_orders_association_table
from company import Company
from product import Product
from order import Order



def connect_to_db(app, db_uri="postgresql:///leaflink_dev"):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)
    print("YES")
    db.create_all()

# def load_example_data():
#     """Example data for testing"""

#     company = Company(name="Buy groceries",
#                 description="Buy eggs and spinach")

#     db.session.add(company)
#     db.session.commit()