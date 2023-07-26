
from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'
    registry_id = fields.Many2one('motorcycle.registry')