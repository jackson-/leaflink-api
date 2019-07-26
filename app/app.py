from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///leaflink_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init DB
db = SQLAlchemy(app)
db.app = app
db.init_app(app)
db.create_all()

from api import *

#####################################################
#                      Run App                      #
#####################################################
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
