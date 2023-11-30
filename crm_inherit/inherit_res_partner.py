from odoo import fields, models, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    region = fields.Many2one('regions.model', string="Region")
    emirates = fields.Many2one('emirates.model', string="Emirates")
    customer_type = fields.Many2one('customer.type', string="Customer Type")
    source_id = fields.Many2one('utm.source', string="Enquiry Source")
    country_id = fields.Many2one('res.country', string='Country',
                                 default=lambda self: self.env['res.country'].search([('code', '=', 'AE')], limit=1)
                                 )
