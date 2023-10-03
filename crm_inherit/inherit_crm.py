from odoo import fields, models, api


class InheritCRMLead(models.Model):
    _inherit = 'crm.lead'

    region = fields.Char("Region")
    emirates = fields.Char("Emirates")
    customer_type = fields.Many2one('customer.type', string="Customer Type")
    enquiry_source = fields.Many2one('enquiry.source', string="Enquiry Source")

    # customer_type = fields.Char(string="Customer Type")
    # enquiry_source = fields.Char(string="Enquiry Source")

