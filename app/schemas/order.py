from marshmallow import fields

from base import BaseSchema

class OrderSchema(BaseSchema):
    # Keys
    id = fields.Int()

    # Own properties
    description = fields.String()
    name = fields.String()