from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.fields import Command
from odoo.http import request

from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.payment import utils as payment_utils
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        RepairOrder = request.env['repair.order']
        values['repairs_count'] = RepairOrder.search_count([])
        return values
    

    def _prepare_repair_portal_rendering_values(
        self, page=1, registry_page=False, **kwargs
    ):
        RepairsOrders = request.env['repair.order']

        partner = request.env.user.partner_id
        values = self._prepare_portal_layout_values()


        url = "/repairs/orders"
        domain = []
            
        pager_values = portal_pager(
            url=url,
            total=RepairsOrders.search_count(domain),
            page=page,
            step=self._items_per_page,
        )

        motorcycles = RepairsOrders.search(domain,limit=self._items_per_page, offset=pager_values['offset']) #<--- order=sort_order 

        values.update({
            'registry': motorcycles.sudo(),
            'page_name': 'registry',
            'pager': pager_values,
            'default_url': url,
        })

        return values
    
    @http.route('/repairs/orders', type='http', website=True)
    def handler(self, **kwargs):
        values = self._prepare_registry_portal_rendering_values(registry_page=True, **kwargs)
        request.session['my_registry_history'] = values['registry'].ids[:100]
        return request.render("ge11_team_07.portal_my_repair_orders", values)
        # return request.render("purchase.portal_my_purchase_order", values)