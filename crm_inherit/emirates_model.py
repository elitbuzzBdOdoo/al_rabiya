from odoo import fields, models, api


class EbEmirates(models.Model):
    _name = 'emirates.model'
    _rec_name = 'emirate_name'
    _description = 'Emirates'
    _inherit = ['mail.thread']

    emirate_code = fields.Char(string="Emirate Reference Code", readonly=True)
    emirate_name = fields.Char(string="Name of the Emirate", tracking=True)
    emirates_seq = fields.Integer(string="Emirates Sequence")


    @api.model
    def create(self, vals_list):
        records = super(EbEmirates, self).create(vals_list)
        for record in records:
            record.emirate_code = self.env['ir.sequence'].next_by_code('emirates.model')
        return records

    def action_emirates_form(self):
        self.ensure_one()
        return {
            'name': "Emirates",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'emirates.model',
            'res_id': self.id,
        }
