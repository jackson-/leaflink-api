from app import db
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class Company(db.Model):
    """A Company class"""

    __tablename__ = "companies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    products = db.relationship("Product", back_populates="company")
    orders = db.relationship("Product", back_populates="company")
    company_type = db.Column(db.Text, nullable=False)


    def __repr__(self):
        """Display when printing a Company object"""

        return "<Company: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
