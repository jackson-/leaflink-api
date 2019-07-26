from flask import jsonify, abort
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from webargs import fields
from flask_apispec import doc, use_kwargs, marshal_with

from models import Product, Company

from schemas.product import ProductSchema
from app import app, db


@app.route("/products", methods=["GET"])
def route_product_get_all():
    products = Product.query.all
    return jsonify({"products":[i.as_dict() for i in products()]})

@app.route("/products/<int:product_id>", methods=["GET"])
def route_product_get_by_id(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    if not product:
      return abort(400, "The product with id: {0} does not exists".format(product_id))
    return jsonify(product.as_dict())


@app.route("/products", methods=["POST"])
@marshal_with(ProductSchema())
@use_kwargs(
    {
        "name": fields.Str(),
        "description": fields.Str(),
        "company_id": fields.Int(),
    }
)
def route_product_create(name, description, company_id):
    company = Company.query.filter(Company.id == company_id).first()
    product = Product(
        name=name,
        description=description,
        company=company
    )
    db.session.add(product)
    db.session.commit()
    db.session.refresh(product)
    return product


@app.route("/products/<int:product_id>", methods=["PUT"])
@marshal_with(ProductSchema())
@use_kwargs(
    {
        "product_id": fields.Int(),
        "name": fields.Str(),
        "description": fields.Str(),
    }
)
def route_product_update(**kwargs):
    product = Product.query.filter(Product.id == kwargs['product_id']).first()
    for key, val in kwargs.items():
        if val is not None:
            setattr(product, key, val)
    db.session.add(product)
    db.session.commit()
    db.session.refresh(product)
    return product
