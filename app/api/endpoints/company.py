from flask import jsonify, abort
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from webargs import fields
from flask_apispec import doc, use_kwargs, marshal_with

from models import Company

from schemas.company import CompanySchema
from app import app, db

@app.route("/companies", methods=["GET"])
def route_company_get_all():
    companies = Company.query.all
    return jsonify({"companies":[i.as_dict() for i in companies()]})

@app.route("/companies/<int:company_id>", methods=["GET"])
def route_company_get_by_id(company_id):
    company = Company.query.filter(Company.id == company_id).first()
    if not company:
      return abort(400, "The company with id: {0} does not exists".format(company_id))
    return jsonify(company.as_dict())


@app.route("/companies", methods=["POST"])
@marshal_with(CompanySchema())
@use_kwargs(
    {
        "name": fields.Str(),
        "description": fields.Str(),
        "company_type": fields.Str(),
    }
)
def route_company_create(name, description, company_type):
    if company_type.lower() not in ["buyer", "seller"]:
        return abort(400, "{0} is not a valid company type. Please choose buyer or seller.".format(company_type))
    company = Company(
        name=name,
        description=description,
        company_type=company_type,
    )
    db.session.add(company)
    db.session.commit()
    db.session.refresh(company)
    return company


@app.route("/companies/<int:company_id>", methods=["PUT"])
@marshal_with(CompanySchema())
@use_kwargs(
    {
        "company_id": fields.Int(),
        "name": fields.Str(),
        "description": fields.Str(),
    }
)
def route_company_update(company_id, **kwargs):
    company = Company.query.filter(Company.id == company_id).first()
    for key, val in kwargs.items():
        if val is not None:
            setattr(company, key, val)
    db.session.add(company)
    db.session.commit()
    db.session.refresh(company)
    return company
