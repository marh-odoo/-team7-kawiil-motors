from odoo import api,fields, models

class Repair(models.Model):
    _inherit = 'repair.order'

    vin = fields.Char(string='VIN', compute="_generate_registry_vin_", readonly=False, required=True)
    milage = fields.Char(string='Milage')
    registry_id = fields.Many2one('motorcycle.registry',string='Registry Id', store=True, compute="_generate_registry_id_")
    lot_id = fields.Many2one(related='registry_id.lot_id', string="lots ids numbers", store=True)
    product_id = fields.Many2one('product.product',compute="_generate_product_id_", store=True)
    # partner_id = fields.Many2one(related='registry_id.owner_id', store=True)

    @api.depends('lot_id')
    def _generate_product_id_(self):
        for product in self:
            product.product_id = product.lot_id.product_id
            

    @api.depends('vin')
    def _generate_registry_id_(self):
        for order in self:
            motorcycle = order.env['motorcycle.registry'].search([('vin', 'ilike', order.vin)])
            if motorcycle:
                order.registry_id = motorcycle

    @api.depends('registry_id')
    def search_order_products(self):
        for sale in self:
            sale.product_id = sale.env['sale.order'].search([
                ('name', 'ilike', sale.registry_id.sale_order_id)
            ]).mapped('order_line').product_id.name



