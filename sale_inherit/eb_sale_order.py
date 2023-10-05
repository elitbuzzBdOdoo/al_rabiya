from odoo import api, fields, models
from odoo.exceptions import UserError


class EbSaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float(string="On Hand Quantity",
                                 help='Count of On Hand quantity')
    forecast_quantity = fields.Float(string="Forecast Quantity",
                                     help='Count of Forecast quantity')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        product_restriction = self.env['ir.config_parameter'].sudo().get_param(
            'sale_stock_restrict.product_restriction')
        check_stock = self.env[
            'ir.config_parameter'].sudo().get_param(
            'sale_stock_restrict.check_stock')
        if product_restriction:

            if check_stock == 'on_hand_quantity':
                self.qty_available = self.product_id.qty_available
            if check_stock == 'forecast_quantity':
                self.forecast_quantity = self.product_id.virtual_available


class EbSaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    onhand_check = fields.Boolean(string='Enable OnHand',
                                  help='To check whether it is based on'
                                       ' on hand quantity')
    forecast_check = fields.Boolean(string='Enable Forecast',
                                    help='To check whether it is based on'
                                         ' Forecast quantity')

    def action_confirm(self):
        res = super(EbSaleOrderInherit, self).action_confirm()
        low_qty = ["Can't confirm the sale order due to: \n"]
        for rec in self.order_line:
            product_restriction = self.env[
                'ir.config_parameter'].sudo().get_param(
                'sale_stock_restrict.product_restriction')
            check_stock = self.env[
                'ir.config_parameter'].sudo().get_param(
                'sale_stock_restrict.check_stock')
            if product_restriction:
                if rec.product_id.detailed_type == 'product':
                    if check_stock == 'on_hand_quantity':
                        if rec.product_uom_qty > rec.qty_available:
                            self.onhand_check = True
                            onhand_qty_list = "You have added %s units of %s" \
                                              " but you only have %s units" \
                                              " available.\n" % (
                                                  rec.product_uom_qty,
                                                  rec.product_id.name,
                                                  rec.qty_available)
                            low_qty.append(onhand_qty_list)

                    if check_stock == 'forecast_quantity':
                        if rec.product_uom_qty > rec.forecast_quantity:
                            self.forecast_check = True
                            forecast_qty_list = "You have added %s" \
                                                " units of %s but you only have" \
                                                " %s units available.\n" % (
                                                    rec.product_uom_qty,
                                                    rec.product_id.name,
                                                    rec.forecast_quantity)
                            low_qty.append(forecast_qty_list)

        listToStr = ' '.join(map(str, low_qty))
        if self.onhand_check:
            raise UserError(listToStr)
        if self.forecast_check:
            raise UserError(listToStr)
        return res
