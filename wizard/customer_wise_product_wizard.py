from odoo import fields, models, api


class CustomerWiseProductWizard(models.TransientModel):
    _name = 'customer.product.wizard'
    _description = 'Customer Wise Product Wizard'

    customer_name = fields.Many2one('res.partner', string="Customer Name")
    date_from = fields.Datetime(string="From Date")
    date_to = fields.Datetime(string="To Date")

    def pdf_action_print_customer_wise_product(self):
        print("PDF printed")

    # def xlsx_action_print_customer_wise_product(self):
    #     print("XLSX printed")
