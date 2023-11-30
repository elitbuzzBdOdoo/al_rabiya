from odoo import fields, models, api


class EbProductCategory(models.Model):
    _name = 'ebproduct.category'
    _inherit = ['mail.thread']
    _order = 'category_id desc'
    _rec_name = 'category_name'
    _description = 'Category'

    category_id = fields.Char(string="Category code", readonly=True)
    category_name = fields.Char(string="Category", tracking=True)
    brand_name = fields.Many2one('ebproduct.brand', string="Brand Name")

    @api.model
    def create(self, vals_list):
        records = super(EbProductCategory, self).create(vals_list)
        for record in records:
            record.category_id = self.env['ir.sequence'].next_by_code('ebproduct.category')
        return records

    def action_category_form(self):
        self.ensure_one()
        return {
            'name': self.display_name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ebproduct.category',
            'res_id': self.id,
        }