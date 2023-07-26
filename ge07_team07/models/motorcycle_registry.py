from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'
    lot_ids = fields.One2many('stock.lot','motorcycle_registry_id')

    @api.constrains('lot_ids')
    def _validate_one2one_lot_ids(self):
        for registry in self:
            if len(registry.lot_ids) > 1:
                raise ValidationError("It is not possible to add more that one stock lot")


    