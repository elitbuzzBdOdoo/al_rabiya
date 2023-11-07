from odoo import fields, models, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    region = fields.Char("Region")
    emirates = fields.Many2one('emirates.model', string="Emirates")