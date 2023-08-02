from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    name = fields.Char(compute="_compute_name", store=True)

    @api.depends('product_id')
    def _compute_name(self):
        for serial in self:
            tmpl = serial.product_id.product_tmpl_id
            if tmpl.detailed_type == 'motorcycle' and serial.product_id.tracking != 'none':
                make = tmpl.make[:2].upper() if tmpl.make else 'XX'
                model =  tmpl.model[:2].upper() if tmpl.model else 'XX'
                year = str(tmpl.year)[-2:] if tmpl.year else '00'
                battery_capacity = tmpl.battery_capacity[:2].upper() if tmpl.battery_capacity else 'XX'
                serial_number = self.env["ir.sequence"].next_by_code("serial.number")

                serial.name = str(make)+str(model)+str(year)+str(battery_capacity)+str(serial_number)
            else:
                serial.name = self.env["ir.sequence"].next_by_code("serial.number")
