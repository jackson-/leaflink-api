from marshmallow import fields

from base import BaseSchema

class ProductSchema(BaseSchema):
    # Keys
    id = fields.Int()

    # Own properties
    description = fields.String()
    name = fields.String()

    # Relationships
    company = fields.Nested(
        'CompanySchema',
        many=False,
        only=('id', 'name', 'description')
    )