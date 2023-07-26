from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(compute="_compute_name",store=True)
    @api.depends('make','model','year','detailed_type')
    def _compute_name(self):
        for record in self.filtered_domain([('detailed_type','=','motorcycle')]):
            record.name= str(record.year)[:2] + str(record.make)[:2] + str(record.model)[:2]
