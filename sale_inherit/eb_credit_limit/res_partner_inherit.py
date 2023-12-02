from odoo import fields, models


class EbResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(string="Credit Limit", tracking=True)
    total_receivable = fields.Float(string="Receivable", compute="_calculate_total_credit")
    total_payable = fields.Float(string="Payable", compute="_calculate_total_debit")
    balance = fields.Float(string="Balance", compute="_calculate_balance", help="Receivable - Payable")
    amount_available = fields.Float(string="Amount Available", compute="_calculate_amount_available",
                                    help="Credit Limit - Balance")
    # date = fields.Datetime(string="Credit Period", tracking=True, required=True)
    date = fields.Datetime(string="Credit Period", tracking=True)

    def _calculate_total_credit(self):
        self.total_receivable = self.credit

    def _calculate_total_debit(self):
        self.total_payable = self.debit

    def _calculate_balance(self):
        self.balance = self.total_receivable - self.total_payable

    def _calculate_amount_available(self):
        self.amount_available = self.credit_limit - self.balance
