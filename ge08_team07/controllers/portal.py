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
        partner = request.env.user.partner_id

        MotorcycleRegistry = request.env['motocycle.registry']
        if 'registry_count' in counters:
            values['registry_count'] = MotorcycleRegistry.search_count(self._prepare_registry_domain(partner)) \
                if MotorcycleRegistry.check_access_rights('read', raise_exception=False) else 0
        return values

    def _prepare_registry_domain(self, partner):
        return [
            #Think in domain
        ]
    
    def _get_sale_searchbar_sortings(self):
        return {
        #    'date': {'label': _('Order Date'), 'order': 'date_order desc'},
            'name': {'label': _('Reference'), 'order': 'name'},
        #    'stage': {'label': _('Stage'), 'order': 'state'},                  Think new searchbarsorting
        }


    def _prepare_registry_portal_rendering_values(
        self, page=1, date_begin=None, date_end=None, sortby=None, registry_page=False, **kwargs
    ):
        MotorcycleRegistry = request.env['motorcycle.registry']

        if not sortby:
            sortby = 'date'

        partner = request.env.user.partner_id
        values = self._prepare_portal_layout_values()

        if registry_page:
            url = "/my/home"
            domain = self._prepare_quotations_domain(partner)
        #else:
        #    url = "/my/orders"
        #    domain = self._prepare_orders_domain(partner)

        searchbar_sortings = self._get_sale_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]['order']   

        #if date_begin and date_end:
        #    domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        pager_values = portal_pager(
            url=url,
            total=MotorcycleRegistry.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
        )
        orders = MotorcycleRegistry.search(domain, order=sort_order, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            'date': date_begin,
            'quotations': orders.sudo() if registry_page else MotorcycleRegistry,
            'page_name': 'registry' if registry_page else 'order',
            'pager': pager_values,
            'default_url': url,
            'searchbar_sortings': registry_page,
            'sortby': sortby,
        })

        return values
    
    @http.route(['/my/page'], type='http', auth="user", website=True)
    def portal_my_quotes(self, **kwargs):
        values = self._prepare_registry_portal_rendering_values(quotation_page=True, **kwargs)
        request.session['my_quotations_history'] = values['quotations'].ids[:100]
        return request.render("sale.portal_my_quotations", values)
