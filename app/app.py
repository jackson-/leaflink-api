from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_apispec import doc, use_kwargs, marshal_with
from flask.json import jsonify

from models import Company, db, connect_to_db
from schemas.company import CompanySchema

app = Flask(__name__)


#####################################################
#                Add resources to API               #
#####################################################
# api.add_resource(CompanyView,
#                  '/company/',
#                  '/company/<int:company_id>')

# Get all
# @docs.register
# @doc(description="Retrieve all companies", security=security_params, tags=["companies"])
@marshal_with(CompanySchema(many=True))
@app.route("/", methods=["GET"])
def route_company_get_all():
    companies = Company.query.all()
    return jsonify({'companies': companies})

#####################################################
#                      Run App                      #
#####################################################
if __name__ == '__main__':

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
