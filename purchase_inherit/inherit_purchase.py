from odoo import fields, models, api


class InheritCRMLead(models.Model):
    _inherit = 'purchase.order'

    purchase_type = fields.Many2one('purchase.type', string="Purchase Type")
