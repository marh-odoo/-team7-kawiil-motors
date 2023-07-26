from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = ['motorcycle.registry']
    lot_ids = fields.One2many('stock.lot','motorcycle_registry_id')

    @api.constrains('lot_ids')
    def _validate_one2one_lot_ids(self):
        number_lot_ids = self.search()
    