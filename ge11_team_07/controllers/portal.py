from odoo import http, _
from odoo.addons.portal.controllers import portal
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.http import request

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.osv.expression import OR


class PortalRepairOrder(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        RepairOrder = request.env["repair.order"]
        if "repair_count" in counters:
            values["repair_count"] = RepairOrder.search_count([])
            values["create_count"] = "New!"
        return values

    def _prepare_order_domain(self, search_domain):
        domain = []
        if search_domain:
            domain.append(search_domain[0])
        return domain

    def _prepare_repair_order_portal_rendering_values(self, search_domain, search,search_in, search_list):
        RepairOrder = request.env["repair.order"]

        domain = self._prepare_order_domain(search_domain)

        url = "/my/repairs/"
        values = self._prepare_portal_layout_values()

        pager_values = portal_pager(
            url=url,
            total=RepairOrder.search_count(domain),
            step=self._items_per_page,
        )

        # if search and search_in:
        #     domain += self._get_search_domain(search_in, search)

        registries = RepairOrder.search(
            domain, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            "registries": registries.sudo(),
            "page_name": "repair_order",
            "pager": pager_values,
            "default_url": url,
            "search": search,
            "searchbar_inputs":search_list,
            "search_in": search_in,
        })

        return values

    def _prepare_create_order_portal_rendering_values(self, page=1, sortby=None, search_in="all", search=None):
        RepairOrder = request.env["repair.order"]

        domain = []
        url = "/my/repairs"
        values = self._prepare_portal_layout_values()

        pager_values = portal_pager(
            url=url,
            total=RepairOrder.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={"sortby": sortby,
                      "search_in": search_in, "search": search}
        )

        if search and search_in:
            domain += self._get_search_domain(search_in, search)

        registries = RepairOrder.search(
            domain, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            "registries": registries.sudo(),
            "page_name": "repair_order",
            "pager": pager_values,
            "default_url": url,
            "search": search,
            "search_in": search_in,
            "sortby": sortby,
        })

        return values

    @http.route("/my/repairs/", type="http", auth="user", website=True)
    def portal_my_repair_orders(self,search="",search_in="all", **kwargs):
        search_list = {
            'all' : {'label':'All', 'input':'all', 'domain':[]},
            "name" : {'label': "Repair's name", 'input':"name", 'domain':[('name', 'ilike', search)]},
            "vin" : {'label': "Repair's vin", 'input':"vin", 'domain':[('vin', 'ilike', search)]},
        }
        
        search_domain = search_list[search_in]['domain']

        values = self._prepare_repair_order_portal_rendering_values(search_domain, search,search_in, search_list)
        return http.request.render("ge11_team_07.portal_my_repair_order_list", values)

    @http.route("/new-order/", type="http", auth="user", website=True)
    def portal_my_create_orders(self, **kwargs):
        values = self._prepare_create_order_portal_rendering_values(
            **kwargs)
        return http.request.render("ge11_team_07.portal_my_new_repair_order_list", values)

    @http.route(['/new-order/submit'], type='http', auth="public", website=True)
    def repair_form_submit(self, **post):
        try:
            request.env['repair.order'].create({
            'vin': post.get('vin'),
            'description': post.get('description'),
            })
            return request.render("portal.portal_my_home")
        except:
            raise ValidationError("Odoopsie, please enter a valid vin")
        
        
    
    @http.route(['/my/repairs/form/<int:id>'], type='http', auth="user", website=True)
    def portal_repair_page(self, id, access_token=None):
        try:
            order_sudo = self._document_check_access('repair.order', id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        backend_url = f'/web#model={order_sudo._name}'\
                    f'&id={order_sudo.id}'\
                    f'&action={order_sudo._get_portal_return_action().id}'\
                    f'&view_type=form'
        
        values = {
            'repair': order_sudo,
            'report_type': 'html',
            'backend_url': backend_url,
        }

        history_session_key = 'my_registry_history'
        values = self._get_page_view_values(order_sudo, access_token, values, history_session_key, False)


        return request.render('ge11_team_07.repair_order_portal_template', values)