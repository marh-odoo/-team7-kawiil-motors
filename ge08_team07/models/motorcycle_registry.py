from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _inherit = ['portal.mixin', 'motorcycle.registry', 'utm.mixin']
    _description = "Override Mixin"


    # portal.mixin override
    def _compute_access_url(self):
        super()._compute_access_url()
        for registry in self:
            registry.access_url = f'/my/motorcycles/{registry.id}'
    
    def _get_portal_return_action(self):
        self.ensure_one()
        return self.env.ref("motorcycle_registry.registry_list_action")
