from odoo import api, fields, models


class RepairOrder(models.Model):
    _name = "repair.order"
    _inherit = ["repair.order", "portal.mixin"]

    is_public = fields.Boolean("Public", default=True)

    def _get_portal_return_action(self):
        self.ensure_one()
        return self.env.ref("repair.view_repair_order_form")

    def _compute_access_url(self):
        super()._compute_access_url()
        for registry in self:
            print("-----------------", registry)
            registry.access_url = f"/repair-order/form/{registry.registry_id.id}"

    def _set_is_public(self):
        self.ensure_one()
        self.is_public = not self.is_public
