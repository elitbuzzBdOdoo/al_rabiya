from odoo import fields, models, api


class EbProductSubCategory(models.Model):
    _name = 'ebproduct.subcategory'
    _inherit = ['mail.thread']
    _order = 'sub_category_id desc'
    _rec_name = 'sub_category_name'
    _description = 'Sub Category'

    sub_category_id = fields.Char(string="Sub Category code", readonly=True)
    sub_category_name = fields.Char(string="Sub Category", tracking=True)
    category_name = fields.Many2one('ebproduct.category', string="Category", tracking=True)

    @api.model
    def create(self, vals_list):
        records = super(EbProductSubCategory, self).create(vals_list)
        for record in records:
            record.sub_category_id = self.env['ir.sequence'].next_by_code('ebproduct.subcategory')
        return records

    def action_sub_category_form(self):
        self.ensure_one()
        return {
            'name': "Sub Category",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ebproduct.subcategory',
            'res_id': self.id,
        }