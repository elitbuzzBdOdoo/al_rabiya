from odoo import fields, models, api


class InheritCRMLead(models.Model):
    _inherit = 'crm.lead'

    region = fields.Many2one('regions.model', string="Region")
    emirates = fields.Many2one('emirates.model', string="Emirates")
    customer_type = fields.Many2one('customer.type', string="Customer Type")
    country_id = fields.Many2one('res.country', string='Country',
                                 default=lambda self: self.env['res.country'].search([('code', '=', 'AE')], limit=1)
                                 )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        partner = self.partner_id
        if partner:
            self.region = partner.region
            # self.emirates = partner.emirates
            self.customer_type = partner.customer_type
            self.source_id = partner.source_id
