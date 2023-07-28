from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    repair_ids = fields.One2many(string = "Repair orders", comodel_name="repair.order", inverse_name="registry_id")

    def get_action_view_repairs(self):
        actions = self.env['ir.actions.actions']._for_xml_id('repair.action_repair_order_tree')
        return actions