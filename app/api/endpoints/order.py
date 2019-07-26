from flask import jsonify, abort
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from webargs import fields
from flask_apispec import doc, use_kwargs, marshal_with

from models import Order, Product, Company, LineItem

from schemas.order import OrderSchema
from app import app, db

@app.route("/orders", methods=["GET"])
def route_order_get_all():
    orders = Order.query.all
    return jsonify({"orders":[i.as_dict() for i in orders()]})

@app.route("/orders/<int:order_id>", methods=["GET"])
def route_order_get_by_id(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    if not order:
      return abort(400, "The order with id: {0} does not exists".format(order_id))
    return jsonify(order.as_dict())


@app.route("/orders", methods=["POST"])
@marshal_with(OrderSchema())
@use_kwargs(
    {
        "name": fields.Str(),
        "description": fields.Str(),
        "buyer_id": fields.Int(),
        "seller_id": fields.Int(),
        "lineitems": fields.List(fields.Dict(), required=True),
    }
)
def route_order_create(name, description, buyer_id, seller_id, lineitems):
    buyer = Company.query.filter(Company.id == buyer_id).first()
    seller = Company.query.filter(Company.id == seller_id).first()
    order_items = []
    order = Order(
        name=name,
        description=description,
        buyer=buyer,
        seller=seller,
    )
    for l in lineitems:
        item = LineItem(
            quantity=l['quantity'], unit_price=l['unit_price'],
        )
        item.product = Product.query.filter(Product.id == l['product_id']).first()
        order.products.append(item)
    db.session.add(order)
    db.session.commit()
    db.session.refresh(order)
    return order


@app.route("/orders/<int:order_id>", methods=["PUT"])
@marshal_with(OrderSchema())
@use_kwargs(
    {
        "order_id": fields.Int(),
        "name": fields.Str(),
        "description": fields.Str(),
    }
)
def route_order_update(**kwargs):
    order = Order.query.filter(Order.id == kwargs['order_id']).first()
    for key, val in kwargs.items():
        if val is not None:
            setattr(order, key, val)
    db.session.add(order)
    db.session.commit()
    db.session.refresh(order)
    return order
