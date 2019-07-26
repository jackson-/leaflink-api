from app import db


class LineItem(db.Model):
    """A LineItem class"""

    __tablename__ = 'lineitems'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    product = db.relationship("Product", back_populates="products")
    order = db.relationship("Order", back_populates="orders")


    def __repr__(self):
        """Display when printing a Product object"""

        return "<Product: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
