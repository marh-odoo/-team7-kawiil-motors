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

        MotorcycleRegistry = request.env['motorcycle.registry']
        
        values['registry_count'] = MotorcycleRegistry.search_count(['|',("owner_id", "=", partner.id),('is_public','=',True)]) \
            if MotorcycleRegistry.check_access_rights('read', raise_exception=False) else 0
        return values

    def _prepare_registry_domain(self, partner, search_domain):
        domain = ['|',("owner_id", "=", partner.id),('is_public','=',True)]
        if search_domain:
            domain.append(search_domain[0])  
        return domain  

    def _prepare_registry_portal_rendering_values(
        self, search_domain, search_in, search, search_list):
        MotorcycleRegistry = request.env['motorcycle.registry']

        partner = request.env.user.partner_id
        values = self._prepare_portal_layout_values()

        url = "/my/motorcycles"
        domain = self._prepare_registry_domain(partner, search_domain)

            
        pager_values = portal_pager(
            url=url,
            total=MotorcycleRegistry.search_count(domain),
            step=self._items_per_page,
        )

        motorcycles = MotorcycleRegistry.search(domain)

        values.update({
            'registry': motorcycles.sudo(),
            'page_name': 'registry',
            'pager': pager_values,
            'default_url': url,
            "search_in": search_in,
            "searchbar_inputs": search_list,
            "search": search,
            })

        return values
    

    @http.route(['/my/motorcycles', '/my/motorcycles/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_registry(self, search="", search_in="all", **kwargs):

        search_list = {
            'all' : {'label':'All', 'input':'all', 'domain':[]},
            "name" : {'label': "Owner's Name", 'input':"name", 'domain':[('owner_id.name', 'ilike', search)]},
            "state" : {'label': "Owner's State", 'input':"state", 'domain':[('owner_id.state_id.name', 'ilike', search)]},
            "country" : {'label': "Owner's Country", 'input':'country', 'domain':[('owner_id.country_id.name', 'ilike', search)]},
            'make' : {'label':'Make', 'input':'make', 'domain':[('make', 'ilike', search)]},
            'model' : {'label':'Model', 'input':'model', 'domain':[('model', 'ilike', search)]},
        }

        search_domain = search_list[search_in]['domain']

        values = self._prepare_registry_portal_rendering_values(search_domain, search_in, search, search_list)
        request.session['my_registry_history'] = values['registry'].ids[:100]
        return request.render("ge08_team07.portal_my_motorcycles", values)


    @http.route(['/my/motorcycles/<int:registry_number>'], type='http', auth="public", website=True)
    def portal_registry_page(self, registry_number, access_token=None, message=False, download=False, **kw):
        try:
            order_sudo = self._document_check_access('motorcycle.registry', registry_number, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if request.env.user.share and access_token:
            today = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % order_sudo.id)
            if session_obj_date != today:
                request.session['view_quote_%s' % order_sudo.id] = today
                # The "Registry viewed by customer" log note is an information
                # dedicated to the salesman and shouldn't be translated in the customer/website lgg
                context = {'lang': order_sudo.user_id.partner_id.lang or order_sudo.company_id.partner_id.lang}
                msg = _('Quotation viewed by customer %s', order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
                del context
                _message_post_helper(
                    "motorcycle.registry",
                    order_sudo.id,
                    message=msg,
                    token=order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=order_sudo.user_id.sudo().partner_id.ids,
                )

        backend_url = f'/web#model={order_sudo._name}'\
                    f'&id={order_sudo.id}'\
                    f'&action={order_sudo._get_portal_return_action().id}'\
                    f'&view_type=form'
        
        values = {
            'motorcycle_registry': order_sudo,
            'message': message,
            'report_type': 'html',
            'backend_url': backend_url,
            'res_company': order_sudo.vin,  # Used to display correct company logo
            'user': request.env.user.partner_id,
        }

        history_session_key = 'my_registry_history'
        values = self._get_page_view_values(order_sudo, access_token, values, history_session_key, False)


        return request.render('ge08_team07.sale_order_portal_template', values)
    
    @http.route(['/edit/registry'], type='http', auth="public", website=True)
    def portal_edit_registry(self ,redirect=None, **post):

        if post and request.httprequest.method == 'POST':
            registry = request.env['motorcycle.registry'].browse(post['id'])

            try:
                registry.sudo().write({'registry_number':post['rn'], 'license_plate':post['license'],'is_public':post['public']})
            except KeyError as error:
                registry.sudo().write({'registry_number':post['rn'], 'license_plate':post['license'],'is_public':False})
                
            if redirect:
                return request.redirect(redirect)
            return request.redirect('/my/motorcycles')