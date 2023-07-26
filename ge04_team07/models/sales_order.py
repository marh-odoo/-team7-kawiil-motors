from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'sale.order'

    is_new_customer = fields.Boolean(related='partner_id.is_new_customer')
    
    def apply_new_customer_discount(self):
        print('Im working')