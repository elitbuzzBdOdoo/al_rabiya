from odoo import fields, models


class SaleByItemWizard(models.TransientModel):
    _name = 'sale.item.wizard'
    _description = 'Sale By Item Wizard'

    partner_id = fields.Many2many('res.partner', string="Customers")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")

    def pdf_sale_by_item_report(self):
        # sale_items = self.env['sale.order'].search_read([])
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('al_rabiya.action_sale_by_item_report').report_action(self, data=data)

    def excel_sale_by_item_report(self):
        print("Printed")
