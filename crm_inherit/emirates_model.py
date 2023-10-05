from odoo import fields, models, api


class EbEmirates(models.Model):
    _name = 'emirates.model'
    _description = 'Emirates'

    name = fields.Char()
