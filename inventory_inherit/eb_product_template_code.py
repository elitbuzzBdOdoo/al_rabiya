from odoo import fields, models, api


class InheritProductTemplateType(models.Model):
    _inherit = 'product.template'
    _order = 'default_code desc'

    category_name = fields.Many2one('ebproduct.category', string="Category")

    @api.model
    def create(self, vals):
        records = super(InheritProductTemplateType, self).create(vals)
        for record in records:
            record.default_code = self.env['ir.sequence'].next_by_code('product.template')
        return records
