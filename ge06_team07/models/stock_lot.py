from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    name = fields.Char(default="P00000", store=True, copy=False, required=True, readonly=True)

    @api.model_create_multi
    def create(self,vals_batch):
        motorcycles = self.env['product.product'].search([('detailed_type','=','motorcycle')])
        for vals in vals_batch:
            if vals.get('name',('P00000')) == ('P00000'):
                if vals.get('product_id') in motorcycles.mapped('id'):
                    motorcycle = motorcycles.search([('id','=',vals.get('product_id'))])
                    make = motorcycle.make[:2].upper() if motorcycle.make else 'XX'
                    model =  motorcycle.model[:2].upper() if motorcycle.model else 'XX'
                    year = str(motorcycle.year)[-2:] if motorcycle.year else '00'
                    battery_capacity = motorcycle.battery_capacity[:2].upper() if motorcycle.battery_capacity else 'XX'
                    lot_number = self.env["ir.sequence"].next_by_code("motorcycle.number")
                    vals['name'] = str(make)+str(model)+str(year)+str(battery_capacity)+str(lot_number)
                else:
                    vals['name'] = self.env["ir.sequence"].next_by_code("stock.lot.serial")
        return super(StockLot, self.with_context(mail_create_nosubscribe=True)).create(vals_batch)