from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID


class invoice_legal(models.Model):
    _inherit = 'res.partner'
    nombre = fields.Integer()
    c_nit = fields.Char(string="NIT")
    c_dui = fields.Char(string="DUI")
    c_giro = fields.Char(string= "Giro de la empresa")