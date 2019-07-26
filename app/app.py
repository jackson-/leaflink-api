from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from api import *

app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init DB
db = SQLAlchemy(app)
db.app = app
db.init_app(app)
from models import *
db.create_all()
db.session.commit()

classes = [cls for cls in db.Model._decl_class_registry.values()
 if isinstance(cls, type) and issubclass(cls, db.Model)]
print(classes)
#####################################################
#                      Run App                      #
#####################################################
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
