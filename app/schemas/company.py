from marshmallow import fields

from base import BaseSchema

class CompanySchema(BaseSchema):
    # Keys
    id = fields.Int()

    # Own properties
    description = fields.String()
    name = fields.String()