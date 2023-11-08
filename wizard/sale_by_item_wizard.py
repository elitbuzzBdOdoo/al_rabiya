from odoo import fields, models


class SaleByItemWizard(models.TransientModel):
    _name = 'sale.item.wizard'
    _description = 'Sale By Item Wizard'

    customer_name = fields.Many2many('res.partner', string="Customers")
    from_date = fields.Datetime(string="From Date")
    to_date = fields.Datetime(string="To Date")

    def pdf_sale_by_item_report(self):
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
        }
        return self.env.ref('al_rabiya.action_sale_by_item_report').report_action(self, data=data)

    def excel_sale_by_item_report(self):
        print("Printed")
