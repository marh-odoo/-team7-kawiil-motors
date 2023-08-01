from odoo import http

class SnippetControllers(http.Controller):
    @http.route('/get_mileage_count',type='json',website=True)
    def get_mileage_count(self):
        return sum(http.request.env['motorcycle.registry'].search([]).mapped('current_mileage'))