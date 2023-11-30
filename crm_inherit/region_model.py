from odoo import fields, models, api


class EbRegion(models.Model):
    _name = 'regions.model'
    _rec_name = 'region_name'
    _description = 'Region'
    _inherit = ['mail.thread']

    region_code = fields.Char(string="Region Code", readonly=True)
    region_name = fields.Char(string="Name of the Region", tracking=True)
    region_seq = fields.Integer(string="Region Sequence")

    @api.model
    def create(self, vals_list):
        records = super(EbRegion, self).create(vals_list)
        for record in records:
            record.region_code = self.env['ir.sequence'].next_by_code('regions.model')
        return records

    def action_regions_form(self):
        self.ensure_one()
        return {
            'name': "Region",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'regions.model',
            'res_id': self.id,
        }
