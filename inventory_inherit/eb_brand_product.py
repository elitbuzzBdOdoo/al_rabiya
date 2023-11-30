from odoo import fields, models, api


class EbProductBrand(models.Model):
    _name = 'ebproduct.brand'
    _inherit = ['mail.thread']
    _order = 'brand_id desc'
    _rec_name = 'brand_name'
    _description = 'Brand'

    brand_id = fields.Char(string="Brand code", readonly=True)
    brand_name = fields.Char(string="Brand", tracking=True)

    @api.model
    def create(self, vals_list):
        records = super(EbProductBrand, self).create(vals_list)
        for record in records:
            record.brand_id = self.env['ir.sequence'].next_by_code('ebproduct.brand')
        return records

    def action_brand_form(self):
        self.ensure_one()
        return {
            'name': self.display_name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ebproduct.brand',
            'res_id': self.id,
        }
