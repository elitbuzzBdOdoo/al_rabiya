from odoo import fields, models, api


class InheritCRMLead(models.Model):
    _inherit = 'crm.lead'

    region = fields.Char("Region")
    emirates = fields.Many2one('emirates.model', string="Emirates")
    customer_type = fields.Many2one('customer.type', string="Customer Type")
    enquiry_source = fields.Many2one('enquiry.source', string="Enquiry Source")
