from odoo import fields, models, api


class InheritProductTemplateType(models.Model):
    _inherit = 'product.template'
    _order = 'product_template_code desc'

    product_template_code = fields.Char(string="Product Code", readonly=True)
    category_name = fields.Many2one('ebproduct.category', string="Category")

    @api.model
    def create(self, vals):
        record = super(InheritProductTemplateType, self).create(vals)
        record.product_template_code = self.env['ir.sequence'].next_by_code('product.template')
        # record.default_code = record.product_template_code
        return record
