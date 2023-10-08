from odoo import fields, models, api


class EbProductCategory(models.Model):
    _name = 'ebproduct.category'
    _inherit = ['mail.thread']
    _order = 'category_id desc'
    # _rec_name = 'category_name'
    _description = 'Category'

    category_id = fields.Char(string="Category code", readonly=True)
    category_name = fields.Char(string="Category", tracking_visibility='always')

    @api.model
    def create(self, vals_list):
        records = super(EbProductCategory, self).create(vals_list)
        for record in records:
            record.category_id = self.env['ir.sequence'].next_by_code('ebproduct.category')
        return records

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.category_id}] {record.category_name}"
            result.append((record.id, name))
        return result
