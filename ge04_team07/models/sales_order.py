from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_new_customer = fields.Boolean(related='partner_id.is_new_customer')
    
    def apply_new_customer_discount(self):
        for order in self.filtered(lambda o: o.order_line.product_id.mapped('detailed_type') != False):
            if('motorcycle' in order.order_line.product_id.mapped('detailed_type')):
                order.pricelist_id = self.pricelist_id.mapped('item_ids').search([('price_surcharge','=','-2500')]).mapped('pricelist_id').id
                order.action_update_prices()
            else:
                order.pricelist_id = 1
                order.action_update_prices()
        return

#orders =env['sale.order'].search([])
#orders.search([('id','=','35')]).order_line.product_id.mapped('detailed_type')