from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_new_customer = fields.Boolean('is new customer?', compute='_is_newcustomer',default=False,store=True)

    @api.depends('name')
    def _is_newcustomer(self):
        #domain = env['sale.order.line'].search_read([('order_partner_id','ilike','hitachi'),('product_type','=','motorcycle')])
        for partner in self:
            if True:
                partner.is_new_customer=True