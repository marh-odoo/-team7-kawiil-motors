from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(compute="_compute_name",store=True,readonly=False)

    @api.depends('make','model','year','detailed_type')
    def _compute_name(self):
        for product in self:
            if product.detailed_type == 'motorcycle' and all((product.year, product.make, product.model)):
                product.name = str(product.year) + " " + str(product.make) + " " +str(product.model)
            else:
                product.name = ""