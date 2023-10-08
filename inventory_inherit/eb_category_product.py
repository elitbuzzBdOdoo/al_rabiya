from odoo import fields, models, api


class EbProductCategory(models.Model):
    _name = 'ebproduct.category'
    _description = 'Category'

    name = fields.Char(string="Category code", readonly=True)
    category_name = fields.Char(string="Category")

    @api.model
    def create(self, vals_list):
        records = super(EbProductCategory, self).create(vals_list)
        for record in records:
            record.product_template_code = self.env['ir.sequence'].next_by_code('product.template')
        return records
