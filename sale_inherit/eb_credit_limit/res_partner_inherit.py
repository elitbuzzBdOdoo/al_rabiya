from datetime import timedelta

from odoo import fields, models, api
from odoo.exceptions import UserError


class EbResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    check_credit = fields.Boolean(string="Activate Credit Limit", tracking=True)
    credit_limit = fields.Float(string="Credit Limit", tracking=True)
    total_receivable = fields.Float(string="Receivable", compute="_calculate_total_credit")
    total_payable = fields.Float(string="Payable", compute="_calculate_total_debit")
    balance = fields.Float(string="Balance", compute="_calculate_balance", help="Receivable - Payable")
    amount_available = fields.Float(string="Amount Available", compute="_calculate_amount_available",
                                    help="Credit Limit - Balance")
    # date = fields.Datetime(string="Credit Period", tracking=True)
    credit_period = fields.Integer("Credit Period (Days)", tracking=True)
    credit_period_date = fields.Date(string="Credit Date", readonly=True)

    def _calculate_total_credit(self):
        self.total_receivable = self.credit

    def _calculate_total_debit(self):
        self.total_payable = self.debit

    def _calculate_balance(self):
        self.balance = self.total_receivable - self.total_payable

    def _calculate_amount_available(self):
        self.amount_available = self.credit_limit - self.balance

    @api.constrains('credit_period')
    def _onchange_credit_period(self):
        if self.credit_period > 0:
            self.credit_period_date = fields.Date.today() + timedelta(days=self.credit_period)
        elif self.credit_period < 0:
            raise UserError("Credit Period Can Not Be Negative")
        else:
            self.credit_period_date = False
