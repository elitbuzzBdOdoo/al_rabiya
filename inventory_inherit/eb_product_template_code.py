from odoo import fields, models, api


class InheritProductTemplateType(models.Model):
    _inherit = 'product.template'
    _order = 'product_template_code desc'

    product_template_code = fields.Char(string="Internal Reference", readonly=True)
    category_name = fields.Many2one('ebproduct.category', string="Category")

    @api.model
    def create(self, vals):
        records = super(InheritProductTemplateType, self).create(vals)
        for record in records:
            record.product_template_code = self.env['ir.sequence'].next_by_code('product.template')
        return records
