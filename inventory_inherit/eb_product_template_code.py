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



from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    common_product_code = fields.Char(string="Common Product Code", readonly=True)

    @api.model
    def create(self, vals):
        vals['common_product_code'] = self.env['ir.sequence'].next_by_code('common.product.code.sequence')
        return super(ProductTemplate, self).create(vals)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _get_variant_default_code(self, product_template, product_attribute_value_ids):
        return product_template.common_product_code
