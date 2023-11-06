from odoo import fields, models, api


class PurchaseType(models.Model):
    _name = 'purchase.type'
    _inherit = ['mail.thread']
    _order = 'purchase_id desc'
    _rec_name = 'purchase_type'
    _description = 'purchase type'

    purchase_id = fields.Char(string="Purchase Code", readonly=True)
    purchase_type = fields.Char(string="Purchase type", required=True, tracking=True)

    @api.model
    def create(self, vals):
        records = super(PurchaseType, self).create(vals)
        for record in records:
            record.purchase_id = self.env['ir.sequence'].next_by_code('purchase.type')
        return records
