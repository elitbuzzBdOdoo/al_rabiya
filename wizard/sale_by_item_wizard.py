from odoo import fields, models
from collections import defaultdict


class SaleReportAdvance(models.TransientModel):
    _name = "sale.report.analysis"

    customer_ids = fields.Many2many('res.partner', string="Customers")
    product_ids = fields.Many2many('product.product', string='Products')
    from_date = fields.Date(string="Start Date", required=True)
    to_date = fields.Date(string="End Date", required=True)
    today_date = fields.Date(default=fields.Date.today())

    def get_analysis_report(self):
        datas = self._get_data()
        return self.env.ref('al_rabiya.action_sales_analysis').report_action([], data=datas)

    def _get_data(self):
        result = defaultdict(lambda: {'quantity': 0, 'total': 0})

        sale_order_line = self.env['sale.order.line'].search([('order_id.state', '!=', 'cancel')])
        filtered = self._get_filtered_order_line(sale_order_line)

        for rec in filtered:
            key = (rec.order_id.partner_id, rec.product_id)
            result[key]['quantity'] += rec.product_uom_qty
            result[key]['total'] += rec.price_subtotal
            result[key]['sku'] = rec.product_id.default_code

        res_list = []
        for (partner, product), values in result.items():
            res = {
                'so': rec.order_id.name,
                'date': rec.order_id.date_order,
                'sku': values['sku'],
                'product_id': product.name,
                'price': product.list_price,
                'quantity': values['quantity'],
                # 'discount': rec.discount,
                # 'tax': product.taxes_id.amount,
                'total': values['total'],
                'partner_id': partner,
                'currency_symbol': rec.order_id.currency_id.symbol
            }
            res_list.append(res)

        datas = {
            'ids': self,
            'model': 'sale.report.analysis',
            'form': res_list,
            'partner_id': self._get_customers(),
            'start_date': self.from_date,
            'end_date': self.to_date,
        }
        return datas

    def _get_total_paid_amount(self, invoices):
        total = 0
        for inv in invoices:
            if inv.payment_state == 'paid':
                total += inv.amount_total
        return total

    def _get_filtered_order_line(self, sale_order_line):
        if self.from_date and self.to_date:
            filtered = list(filter(lambda
                                       x: x.order_id.date_order.date() >= self.from_date and x.order_id.date_order.date() <= self.to_date and x.order_id.partner_id in self.customer_ids and x.product_id in self.product_ids,
                                   sale_order_line))
        else:
            filtered = list(filter(lambda
                                       x: x.order_id.partner_id in self.customer_ids and x.product_id in self.product_ids,
                                   sale_order_line))
        return filtered

    def _get_filtered(self, sale_order):

        if self.from_date and self.to_date:
            filtered = list(filter(lambda
                                       x: x.date_order.date() >= self.from_date and x.date_order.date() <= self.to_date and x.partner_id in self.customer_ids,
                                   sale_order))
        else:
            filtered = list(filter(lambda
                                       x: x.partner_id in self.customer_ids,
                                   sale_order))
        return filtered

    def _get_customers(self):
        customers = []
        for rec in self.customer_ids:
            a = {
                'id': rec,
                'name': rec.name
            }
            customers.append(a)
        return customers
