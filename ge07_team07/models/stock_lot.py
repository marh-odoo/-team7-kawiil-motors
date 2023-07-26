
from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = ['stock.lot']
    motorcycle_registry_id = fields.Many2one('motorcycle.registry')