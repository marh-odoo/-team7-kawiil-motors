from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    @api.model_create_multi
    def create(self,vals_list):
        res = super().create(vals_list)

        for registry in res:
            
            is_user_created = self.env['res.users'].search([('email','=',registry.owner_id.email)])

            if is_user_created:
                continue
            
            user = self.env['res.users'].create({
                "name": registry.owner_id.name,
                "login": registry.owner_id.email,
                "email": registry.owner_id.email
            })
            
            self._grant_portal_access(user)
        return res
    

    def _grant_portal_access(self,user):
        user.ensure_one()
        group_portal = self.env.ref('base.group_portal')
        group_user = self.env.ref('base.group_user')

        user_sudo = user.sudo()

        user_sudo.write({'active': True, 'groups_id': [(4, group_portal.id), (3, group_user.id)]})
        # prepare for the signup process
        user_sudo.partner_id.signup_prepare()


        self._send_email(user)

    def _send_email(self, user):
        user.ensure_one()
        # determine subject and body in the portal user's language
        template = self.env.ref('ge12_team07.mail_template_base_welcome_new_customers')
        if not template:
            raise UserError(_('The template "Portal: new user" not found for sending email to the portal user.'))

        lang = user.sudo().lang
        partner = user.sudo().partner_id
        portal_url = partner.with_context(signup_force_type_in_url='', lang=lang)._get_signup_url_for_action()[partner.id]
        partner.signup_prepare()

        template.with_context(dbname=self._cr.dbname, portal_url=portal_url, lang=lang).send_mail(user.id, force_send=True)

        return True