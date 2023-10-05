from odoo import fields, models, api, _


class InheritProductTemplateType(models.Model):
    _inherit = 'product.template'
    _order = 'product_template_code desc'

    product_template_code = fields.Char(string="Product Code", readonly=True)

    # @api.model
    # def create(self, vals):
    #     record = super().create(vals)
    #     if record:
    #         name_text = 'P-0' + str(record.id)
    #         record.update({'product_template_code': name_text})
    #     return record

    @api.model
    def create(self, vals_list):
        records = super(InheritProductTemplateType, self).create(vals_list)
        for record in records:
            record.product_template_code = self.env['ir.sequence'].next_by_code('product.template')
        return records
