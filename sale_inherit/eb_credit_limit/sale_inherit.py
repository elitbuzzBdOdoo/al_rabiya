from odoo import fields, models, api, _

from odoo.exceptions import AccessDenied


class SaleInherit(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(
        selection=[
            ('draft', "Quotation"),
            ('sent', "Quotation Sent"),
            ('sales_approval', "Sales Approval"),
            ('finance_approval', "Finance Approval"),
            ('approved', "Credit Approved"),
            ('reject', "Credit Rejected"),
            ('sale', "Sales Order"),
            ('done', "Locked"),
            ('cancel', "Cancelled"),
        ], string="Status", readonly=True, copy=False, index=True, tracking=3, default='draft')
    partner_id = fields.Many2one("res.partner")
    check_credit = fields.Boolean(string="Activate Credit Limit", related="partner_id.check_credit")
    credit_limit = fields.Float(string="Credit Limit", related="partner_id.credit_limit")
    total_receivable = fields.Float(string="Expended", related="partner_id.total_receivable")
    total_payable = fields.Float(string="Payable", related="partner_id.total_payable")
    balance = fields.Float(string="Balance", related="partner_id.balance")
    amount_available = fields.Float(string="Amount Available", related="partner_id.amount_available")
    # date = fields.Datetime(string="Credit Period", related="partner_id.date")
    credit_period_date = fields.Date(string="Credit Period", related="partner_id.credit_period_date")
    is_credit_limit_approval = fields.Boolean(compute='_compute_customer_credit_limit')
    is_credit_limit_final_approved = fields.Boolean()
    check_credit_period_date = fields.Boolean()

    def get_so_for_approval(self):
        web = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        so_base_url = self.env['ir.config_parameter'].sudo().get_param(
            'web.base.url') + '/web#id=%d&menu_id=%d&cids=%d&action=%d&model=sale.order&view_type=form' % (
                          self.id, self.env.ref('sale.sale_menu_root').id,
                          self.env.company.id,
                          self.env.ref('sale.action_quotations_with_onboarding').id)
        return so_base_url

    @api.depends('balance')
    def _compute_customer_credit_limit(self):
        self.is_credit_limit_approval = False
        if self.check_credit == True:
            # date_order_date = fields.Date.to_datetime(self.date_order)
            # credit_period_date = fields.Date.to_datetime(self.credit_period_date)
            if str(self.credit_period_date) < str(self.date_order):
                self.check_credit_period_date = True
            else:
                self.check_credit_period_date = False
            if self.partner_id or self.balance:
                if (self.balance + self.amount_total) > self.credit_limit and \
                        not self.is_credit_limit_final_approved:
                    self.is_credit_limit_approval = True
                if self.partner_id.credit_limit <= self.balance and self.state in ['draft', 'sent']:
                    self.is_credit_limit_approval = True
                elif self.amount_total and (self.balance + self.amount_total) > self.credit_limit:
                    self.is_credit_limit_approval = True
            else:
                self.is_credit_limit_approval = False

    def action_confirm(self):
        partner_id = self.partner_id
        total_amount = self.balance
        if partner_id.check_credit:
            existing_move = self.env['account.move'].search(
                [('partner_id', '=', self.partner_id.id), ('state', '=', 'posted')])
            if (self.balance + self.amount_total) > self.credit_limit and \
                    not self.is_credit_limit_final_approved:
                difference_amount = round((self.balance + self.amount_total) - self.credit_limit, 2)
                raise AccessDenied(_('Can not confirm the respective S.O as Customer has crossed their Approved credit limit by %s Please seek for approval to proceed' \
                                     % difference_amount))
            elif partner_id.credit_limit <= total_amount and not existing_move:
                view_id = self.env.ref('al_rabiya.view_warning_wizard_form')
                context = dict(self.env.context or {})
                context[
                    'message'] = "Customer Blocking limit exceeded without having a recievable, Do You want to continue?"
                context['default_sale_id'] = self.id
                if not self._context.get('warning'):
                    return {
                        'name': 'Warning',
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'res_model': 'warning.wizard',
                        'view_id': view_id.id,
                        'target': 'new',
                        'context': context,
                    }
            elif partner_id.credit_limit <= total_amount and not self.is_credit_limit_final_approved:
                raise AccessDenied(_('Customer credit limit exceeded.'))
        res = super(SaleInherit, self).action_confirm()
        return res

    def send_credit_limit_approval(self):
        template_id = self.env.ref(
            'al_rabiya.sale_order_credit_limit_approval_sales_manager')
        template_id.with_context().send_mail(self._origin.id, force_send=True)
        msg = "Send For Credit Limit Approval To: %s" % self.partner_id.user_id.name or ""
        self.message_post(body=msg)
        self.state = 'sales_approval'
        self.is_credit_limit_approval = False

    def approved_credit_limit_from_sales_manager(self):
        if self.state == 'sales_approval':
            template_id = self.env.ref(
                'al_rabiya.sale_order_credit_limit_approval_account_manager')
            template_id.with_context().send_mail(self._origin.id, force_send=True)
            msg = "Send For Credit Limit Approval To Finance Team"
            self.message_post(body=msg)
            self.state = 'finance_approval'

    def approved_credit_limit_from_account_manager(self):
        if self.state == 'finance_approval':
            self.state = 'approved'
            self.is_credit_limit_final_approved = True

    def reject_sale_order(self):
        if self.state == 'sales_approval':
            template_data = {
                'subject': 'Customer credit limit/credit period request rejected',
                'body_html': """<p>
                        Hello %s, <br/><br/>
                        </p>
                        <p>
                        This email is to notify that Quotation number %s which belongs to %s 
                        has been rejected by %s (Customer Account Manager), <br/> please reach him for further clarifications </p>
                        """ % (self.user_id.name, self.name, self.partner_id.name, self.env.user.name),
                'email_from': self.env.user.partner_id.email or self.env.user.email,
                'email_to': self.user_id.email or self.user_id.partner_id.email,
                'record_name': self.name,
            }
            template_id = self.env['mail.mail'].create(template_data)
            template_id.sudo().send()
            self.state = 'reject'
            msg = "Rejected By Sales Manager: %s" % self.env.user.name
            self.message_post(body=msg)
        elif self.state == 'finance_approval':
            template_data = {
                'subject': 'Customer credit limit rejected',
                'body_html': """<p>
                        Hello %s, <br/><br/>
                        </p>
                        <p>
                        This email is to notify that Quotation number %s which belongs to %s 
                        has been rejected by Finance team, <br/>

                        please reach him for further clarifications</p> 
                        """ % (self.user_id.name, self.name, self.partner_id.name),
                'email_from': self.env.user.partner_id.email or self.env.user.email,
                'email_to': self.user_id.email or self.user_id.partner_id.email,
                'record_name': self.name,
            }
            template_id = self.env['mail.mail'].create(template_data)
            template_id.sudo().send()
            self.state = 'reject'
            msg = "Rejected By Finance Team: %s" % self.env.user.name
            self.message_post(body=msg)
