from odoo import models, fields, api

class StockSummaryWizard(models.TransientModel):
    _name = "stock.summary.wizard"
    _description = "Stock Summary Report"

    start_date = fields.Date(string="Start", required=True)
    end_date = fields.Date(string="End", required=True)
    location = fields.Many2one('stock.location', string='Location', required=True, domain=[
        ('active', '=', True), ('usage', '=', 'view'), ('location_id', '!=', False)])

    def print_report(self):
        product = "product"
        user = self.env.user

        list_product_main = self.env['product.product'].search(
            [('active', '=', True), ('detailed_type', '=', product)])

        data = {
            'model': 'stock.summary.wizard',
            'form_data': self.read()[0]
        }
        start_date, end_date, locations = data['form_data']['start_date'], data['form_data']['end_date'], self.location
        outgoing_move_list, incoming_move_list = locations.child_ids.outgoing_move_line_ids, locations.child_ids.incoming_move_line_ids

        total_opening_stock, total_closing_stock, total_stock_changes, total_quantity_in, total_quantity_out = (0,) * 5
        product_list = []

        for product in list_product_main:
            outgoing_moves = outgoing_move_list.filtered(
                lambda x: start_date <= x.date.date() <= end_date and x.product_id.id == product.id
            )
            incoming_moves = incoming_move_list.filtered(
                lambda x: start_date <= x.date.date() <= end_date and x.product_id.id == product.id
            )

            opening_stock = sum(move.qty_done for move in incoming_moves if move.date.date() < start_date)
            outgoing_quantity = sum(move.qty_done for move in outgoing_moves)
            incoming_quantity = sum(move.qty_done for move in incoming_moves)

            changes_stock = incoming_quantity - outgoing_quantity
            closing_stock = opening_stock + changes_stock

            total_opening_stock += opening_stock
            total_closing_stock += closing_stock
            total_stock_changes += changes_stock
            total_quantity_in += incoming_quantity
            total_quantity_out += outgoing_quantity

            product_list.append({
                'name': product.name,
                'product_code': product.default_code,
                'opening_stock': opening_stock,
                'incoming_quantity': incoming_quantity,
                'outgoing_quantity': outgoing_quantity,
                'closing_stock': closing_stock,
                'stock_changes': changes_stock,
            })

        data['product_list'], data['start_date'], data['end_date'] = product_list, start_date.strftime('%d/%m/%Y'), end_date.strftime('%d/%m/%Y')
        data['total_opening_stock'], data['total_closing_stock'], data['total_quantity_in'], data['total_quantity_out'], data['total_stock_changes'] = total_opening_stock, total_closing_stock, total_quantity_in, total_quantity_out, total_stock_changes
        data['location'], data['user_name'] = locations.complete_name, user.name

        return self.env.ref("al_rabiya.stock_summary_pdf_template_action").report_action(self, data=data)
