from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_new_customer = fields.Boolean('is new customer?', compute='_is_new_customer',default=False)

    @api.depends()
    def _is_new_customer(self):
        for partner in self:
            if('motorcycle' in partner.sale_order_ids.mapped('order_line').product_id.mapped('detailed_type')):
                partner.is_new_customer = False
            else:
                partner.is_new_customer = True
        return