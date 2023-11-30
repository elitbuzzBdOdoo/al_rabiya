from odoo import fields, models, api, _


class InheritProductTemplateType(models.Model):
    _inherit = 'product.template'
    _order = 'default_code desc'

    category_name = fields.Many2one('ebproduct.category', string="Category")
    sub_category_name = fields.Many2one('ebproduct.subcategory', string="Sub Category")
    brand_name = fields.Many2one('ebproduct.brand', string="Brand")

    @api.model
    def create(self, vals):
        records = super(InheritProductTemplateType, self).create(vals)
        for record in records:
            record.default_code = self.env['ir.sequence'].next_by_code('product.template')
        return records

    # brand, category, subcategory relation

    # @api.onchange('brand_name')
    # def _onchange_brand_name(self):
    #     if self.brand_name:
    #         return {'domain': {'category_name': [('brand_name', '=', self.brand_name.id)]}}
    #     return {'domain': {'category_name': []}}
    #
    # @api.onchange('category_name', 'brand_name')
    # def _onchange_category_name(self):
    #     if self.brand_name and self.category_name \
    #             and self.category_name.brand_name.id != self.brand_name.id:
    #         self.category_name = False
    #         return {
    #             'warning': {
    #                 'title': _("Warning!"),
    #                 'message': _("The selected 'Category' does not belong to the selected 'Brand'. "
    #                              "Select the Brand First.")
    #             }
    #         }
    #
    # @api.onchange('category_name')
    # def _onchange_category_name(self):
    #     if self.category_name:
    #         return {'domain': {'sub_category_name': [('category_name', '=', self.category_name.id)]}}
    #     return {'domain': {'sub_category_name': []}}
    #
    # @api.onchange('sub_category_name', 'category_name')
    # def _onchange_sub_category_name(self):
    #     if self.category_name and self.sub_category_name \
    #             and self.sub_category_name.category_name.id != self.category_name.id:
    #         self.sub_category_name = False
    #         return {
    #             'warning': {
    #                 'title': _("Warning!"),
    #                 'message': _("The selected 'Sub Category' does not belong to the selected 'Category'.")
    #             }
    #         }