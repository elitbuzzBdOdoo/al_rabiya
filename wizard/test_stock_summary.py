from odoo import models, fields, api
import datetime
from odoo.http import request


class StockSummaryWizard(models.TransientModel):
    _name = 'stock.summary.wizard'
    _description = 'Stock Summary Wizard'

    start_date = fields.Date(string="Start", required=True)
    end_date = fields.Date(string="End", required=True)
    location = fields.Many2one('stock.location', string='Location', required=True, domain=[
        ('active', '=', True), ('usage', '=', 'view'), ('location_id', '!=', False)])

    def print_report(self):
        product = "product"
        user_id = request.session.uid
        user = request.env['res.users'].browse(user_id)

        list_product_main = self.env['product.product'].search(
            [('active', '=', True) and ('detailed_type', '=', product)])

        todayDate = datetime.date.today()
        if todayDate.day > 25:
            todayDate += datetime.timedelta(7)
        data = {
            'model': 'stock.summary.wizard',
            'form_data': self.read()[0]
        }
        start_date = data['form_data']['start_date']
        end_date = data['form_data']['end_date']
        locations = self.location
        outgoing_move_list = locations['child_ids']['outgoing_move_line_ids']
        incoming_move_list = locations['child_ids']['incoming_move_line_ids']

        product_list = []

        total_opening_stock = 0
        total_closing_stock = 0
        total_stock_changes = 0

        total_export_at_beginning_period = 0
        total_opening_stock_quantity = 0
        total_outgoing_quantity = 0
        total_incoming_quantity = 0

        opening_stock = 0
        closing_stock = 0
        changes_stock = 0
        incoming_quantity = 0
        outgoing_quantity = 0
        total_quantity_in = 0
        total_quantity_out = 0

        if len(list_product_main) != 0:
            for i in list_product_main:
                vals = {
                    'name': i.name,
                    'product_code': i.default_code,
                    'opening_stock': 0,
                    'incoming_quantity': 0,
                    'outgoing_quantity': 0,
                    'closing_stock': 0,
                    'stock_changes': 0,
                }

                if len(outgoing_move_list) != 0:
                    for j in outgoing_move_list:
                        if j['date'].date() < start_date and j['product_id']['id'] == i.id:
                            total_export_at_beginning_period += j['qty_done']
                        if start_date <= j['date'].date() <= end_date and j['product_id']['id'] == i.id:
                            outgoing_quantity += j['qty_done']
                if len(incoming_move_list) != 0:
                    for j in incoming_move_list:
                        if j['date'].date() < start_date and j['product_id']['id'] == i.id:
                            total_opening_stock_quantity += j['qty_done']
                        if start_date <= j['date'].date() <= end_date and j['product_id']['id'] == i.id:
                            incoming_quantity += j['qty_done']

                    opening_stock = total_opening_stock_quantity - total_export_at_beginning_period
                    changes_stock = incoming_quantity - outgoing_quantity
                    closing_stock = opening_stock + changes_stock

                    incoming_quantity = incoming_quantity
                    outgoing_quantity = outgoing_quantity

                    total_opening_stock += opening_stock
                    total_closing_stock += closing_stock
                    total_stock_changes += changes_stock
                    vals = {
                        'name': i.name,
                        'product_code': i.default_code,
                        'opening_stock': opening_stock,
                        'incoming_quantity': incoming_quantity,
                        'outgoing_quantity': outgoing_quantity,
                        'closing_stock': closing_stock,
                        'stock_changes': changes_stock,
                    }

                    opening_stock = 0
                    closing_stock = 0
                    changes_stock = 0
                    total_export_at_beginning_period = 0
                    total_opening_stock_quantity = 0
                    incoming_quantity = 0
                    outgoing_quantity = 0

                product_list.append(vals)
                totalopening_stock = 0
                totalclosing_stock = 0
                totalquantity_in = 0
                totalquantity_out = 0
                totalstock_changes = 0

        if len(product_list) != 0:
            for i in product_list:
                totalopening_stock += i['opening_stock']
                totalquantity_in += i['incoming_quantity']
                totalquantity_out += i['outgoing_quantity']
                totalclosing_stock += i['closing_stock']
                totalstock_changes += i['stock_changes']

        print("Debug: product_list in Python code", product_list)

        data['product_list'] = product_list
        data['start_date'] = start_date.strftime('%d/%m/%Y')
        data['end_date'] = end_date.strftime('%d/%m/%Y')
        data['total_opening_stock'] = totalopening_stock
        data['total_closing_stock'] = totalclosing_stock
        data['total_quantity_in'] = totalquantity_in
        data['total_quantity_out'] = totalquantity_out
        data['total_stock_changes'] = totalstock_changes
        data['location'] = locations['complete_name']
        data['user_name'] = user.name

        return self.env.ref("al_rabiya.stock_summary_pdf_template_action").report_action(self, data=data)
