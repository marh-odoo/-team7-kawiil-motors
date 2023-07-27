from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _inherit = ['portal.mixin', 'motorcycle_registry', 'utm.mixin']


    def _compute_access_url(self):
        super()._compute_access_url()
        for product in self:
            product.access_url = f'/my/home'