from odoo import api, fields, models

class RepairOrders(models.Model):
    _name = "repair.order"
    _inherit = ['portal.mixin', 'repair.order', 'utm.mixin']
    _description = "Override Mixin"


    # portal.mixin override
    def _compute_access_url(self):
        super()._compute_access_url()
        for registry in self:
            registry.access_url = f'/repairs/orders{registry.id}'
    
    def _get_portal_return_action(self):
        self.ensure_one()
        return self.env.ref("repair_order.portal_my_repair_orders") 