from odoo import fields, models, api


class PurchaseType(models.Model):
    _name = 'purchase.type'
    _rec_name = 'purchase_type'
    _description = 'purchase type'

    purchase_id = fields.Char(string="Purchase Code", readonly=True)
    purchase_type = fields.Char(string="Purchase type", required=True)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record:
            name_text = 'PT-0' + str(record.id)
            record.update({'purchase_id': name_text})
        return record
