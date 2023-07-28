from odoo import api,fields, models

class Repair(models.Model):
    _inherit = 'repair.order'

    vin = fields.Char(string='VIN', readonly=False, required=True)
    mileage = fields.Float(string='Milage', related="registry_id.current_mileage",readonly=False, required=True)
    registry_id = fields.Many2one('motorcycle.registry',string='Registry Id', store=True, compute="_generate_registry_id_")
    product_id = fields.Many2one('product.template',related="registry_id.lot_id.product_id.product_tmpl_id")
    partner_id = fields.Many2one(related='registry_id.owner_id')
    sale_order_id = fields.Many2one(related='registry_id.sale_order_id')


    @api.depends('vin')
    def _generate_registry_id_(self):
        for order in self:
            motorcycle = order.env['motorcycle.registry'].search([('vin', '=', order.vin)])
            if motorcycle:
                order.registry_id = motorcycle



