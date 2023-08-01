from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'
    lot_ids = fields.One2many('stock.lot','registry_id', string="lots ids numbers")
    lot_id = fields.Many2one('stock.lot',compute="_compute_lot_id",store=True)
    sale_order_id = fields.Many2one("sale.order", ondelete="restrict")

    vin = fields.Char(string='VIN', related = "lot_id.name", required = False, readonly=False)
    owner_id = fields.Many2one(comodel_name="res.partner", ondelete="restrict", related="sale_order_id.partner_id")

    @api.constrains('lot_ids')
    def _check_lot_ids(self):
        for registry in self:
            if len(registry.lot_ids) > 1:
                raise ValidationError("It is not possible to add more that one stock lot")

    @api.depends('lot_ids')
    def _compute_lot_id(self):
        if len(self.lot_ids)>0:
            self.lot_id = self.lot_ids[0]
        else:
            self.lot_id = False
