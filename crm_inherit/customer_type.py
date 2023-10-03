from odoo import fields, models, api


class CustomerType(models.Model):
    _name = 'customer.type'
    _rec_name = 'customer_type'
    _description = 'Customer type'

    customer_id = fields.Char(string="Customer Code", readonly=True)
    customer_type = fields.Char(string="Customer type", required=True)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record:
            name_text = 'CT-0' + str(record.id)
            record.update({'customer_id': name_text})
        return record
