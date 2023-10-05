from odoo import fields, models, api


class EbResConfigInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    product_restriction = fields.Boolean(
        string='Out Of Stock Product Restriction',
        help='Enable Out Of Stock Product Restriction')
    check_stock = fields.Selection(
        [('on_hand_quantity', 'On Hand Ouantity'),
         ('forecast_quantity', 'Forecast Ouantity')], string="Based On",
        help='Choose the type of restriction')

    @api.model
    def get_values(self):
        res = super(EbResConfigInherit, self).get_values()
        params = self.env['ir.config_parameter'].sudo().get_param
        product_restriction = params('sale_stock_restrict.product_restriction')
        check_stock = params('sale_stock_restrict.check_stock')
        res.update(
            product_restriction=product_restriction,
            check_stock=check_stock
        )
        return res

    def set_values(self):
        super(EbResConfigInherit, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'sale_stock_restrict.product_restriction', self.product_restriction)
        self.env['ir.config_parameter'].sudo().set_param(
            'sale_stock_restrict.check_stock', self.check_stock)
