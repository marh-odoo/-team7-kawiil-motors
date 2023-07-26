from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(compute="_compute_name",store=True,readonly=False)

    @api.depends('make','model','year','detailed_type')
    def _compute_name(self):
        for record in self:
            if record.detailed_type == 'motorcycle' and all((record.year, record.make, record.model)):
                record.name = str(record.year)[0:2] + str(record.make)[0:2] + str(record.model)[0:2]
            else:
                record.name =""