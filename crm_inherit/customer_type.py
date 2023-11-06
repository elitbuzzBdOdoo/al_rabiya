from odoo import fields, models, api


class CustomerType(models.Model):
    _name = 'customer.type'
    _inherit = ['mail.thread']
    _order = 'customer_id desc'
    _rec_name = 'customer_type'
    _description = 'Customer type'

    customer_id = fields.Char(string="Customer Code", readonly=True)
    customer_type = fields.Char(string="Customer type", required=True, tracking=True)
    customer_seq = fields.Integer(string="Customer Sequence")

    @api.model
    def create(self, vals_list):
        records = super(CustomerType, self).create(vals_list)
        for record in records:
            record.customer_id = self.env['ir.sequence'].next_by_code('customer.type')
        return records

    def action_customer_type(self):
        self.ensure_one()
        return {
            'name': "Customer Type",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'customer.type',
            'res_id': self.id,
        }
