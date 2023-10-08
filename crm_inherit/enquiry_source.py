from odoo import fields, models, api


class EnquirySource(models.Model):
    _name = 'enquiry.source'
    _rec_name = 'enquiry_source'
    _description = 'Enquiry Source'

    enquiry_source_id = fields.Char(string="Source ID", readonly=True)
    enquiry_source = fields.Char(string="Enquiry Source", required=True)

    # @api.model
    # def create(self, vals):
    #     record = super().create(vals)
    #     if record:
    #         name_text = 'ES-0' + str(record.id)
    #         record.update({'enquiry_source_id': name_text})
    #     return record

    @api.model
    def create(self, vals_list):
        records = super(EnquirySource, self).create(vals_list)
        for record in records:
            record.enquiry_source_id = self.env['ir.sequence'].next_by_code('enquiry.source')
        return records
