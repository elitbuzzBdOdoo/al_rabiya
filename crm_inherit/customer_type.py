from odoo import fields, models, api


class CustomerType(models.Model):
    _name = 'customer.type'
    _inherit = ['mail.thread']
    _order = 'customer_id desc'
    _rec_name = 'customer_type'
    _description = 'Customer type'

    customer_id = fields.Char(string="Customer Code", readonly=True)
    customer_type = fields.Char(string="Customer type", required=True, track_visibility='always')

    # @api.model
    # def create(self, vals):
    #     record = super().create(vals)
    #     if record:
    #         name_text = 'CT-0' + str(record.id)
    #         record.update({'customer_id': name_text})
    #     return record

    @api.model
    def create(self, vals_list):
        records = super(CustomerType, self).create(vals_list)
        for record in records:
            record.customer_id = self.env['ir.sequence'].next_by_code('customer.type')
        return records
