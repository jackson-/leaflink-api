from app import db


products_to_orders_association_table = db.Table('products_to_orders',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
)