from odoo import fields, models


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = "Real Estate Property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    type = fields.Selection(
        string="Type",
        selection=[
            ('house', "House"),
            ('apartment', "Apartment"),
            ('office', "Office Building"),
            ('retail', "Retail Space"),
            ('warehouse', "Warehouse"),
        ],
        required=True,
        default='house',
    )
    selling_price = fields.Float(
        string="Selling Price", help="The selling price excluding taxes.", required=True
    )
    floor_area = fields.Integer(
        string="Floor Area", help="The floor area in square meters excluding the garden."
    )
    bedrooms = fields.Integer(string="Number of bedrooms", default=2)
    has_garden = fields.Boolean(string="Garden")
    has_garage = fields.Boolean(string="Garage")
    availability_date = fields.Date(string="Availability Date")
