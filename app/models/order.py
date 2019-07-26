from app import db


class Order(db.Model):
    """A Order class"""

    __tablename__ = "orders"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    buyer_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    buyer = db.relationship("Company", back_populates="orders")
    seller_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    seller = db.relationship("Company", back_populates="orders")
    products = db.relationship("LineItem", back_populates="parent")


    def __repr__(self):
        """Display when printing a Product object"""

        return "<Product: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
