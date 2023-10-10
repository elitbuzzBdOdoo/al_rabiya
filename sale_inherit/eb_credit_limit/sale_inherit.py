from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleInherit(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    credit_limit = fields.Float(string="Credit Limit", related="partner_id.credit_limit")
    total_receivable = fields.Float(string="Credit", related="partner_id.total_receivable")
    total_payable = fields.Float(string="Debit", related="partner_id.total_payable")
    balance = fields.Float(string="Balance", related="partner_id.balance")
    amount_available = fields.Float(string="Amount Available", related="partner_id.amount_available")
    date = fields.Datetime(string="Credit Period", related="partner_id.date")

    @api.constrains("amount_total")
    def _check_amount_available(self):
        for record in self:
            date_order_date = fields.Datetime.from_string(record.date_order)
            date = fields.Datetime.from_string(record.date)
            if date < date_order_date:
                msg = 'Your Credit Period Has Expired. \n Credit Period was "%s". Please Contact Administrator.' % (
                    record.date)
                raise UserError(_('You cannot confirm the Sale Order. \n' + msg))

            if record.amount_available < record.amount_total:
                msg = ('Your Available Credit Limit Amount = %s \n Check "%s" Accounts or Credit Limits. \n Credit '
                       'Period is "%s"') % (
                          record.amount_available,
                          record.partner_id.name,
                          record.date)
                raise UserError(_('You cannot confirm the Sale Order. \n' + msg))
