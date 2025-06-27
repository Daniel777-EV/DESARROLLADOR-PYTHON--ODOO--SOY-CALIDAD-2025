# -*- coding: utf-8 -*-
import qrcode
import io
import base64
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    qr_code_string = fields.Char(string="QR String", compute='_compute_qr_code_string', store=True)
    x_qr_invoice = fields.Binary(string="QR Code", compute='_compute_qr_code', store=True) # [cite: 6]

    # Campo compute para la sumatoria de cantidades de línea
    total_line_quantities = fields.Float(string="Total Line Quantities", compute='_compute_total_line_quantities', store=True) # [cite: 7]

    @api.depends('invoice_line_ids.quantity')
    def _compute_total_line_quantities(self):
        for move in self:
            move.total_line_quantities = sum(move.invoice_line_ids.mapped('quantity')) # [cite: 7]

    @api.depends('name', 'partner_id.name', 'invoice_date', 'total_line_quantities', 'amount_total')
    def _compute_qr_code_string(self):
        for move in self:
            if move.name and move.partner_id and move.invoice_date and move.total_line_quantities is not None and move.amount_total is not None:
                invoice_number = move.name
                client_name = move.partner_id.name
                invoice_date = move.invoice_date.strftime('%d/%m/%Y') if move.invoice_date else ''
                total_quantities = str(move.total_line_quantities) # [cite: 7]
                total_to_pay = str(move.amount_total)

                qr_data = f"{invoice_number}|{client_name}|{invoice_date}|{total_quantities}|{total_to_pay}" # [cite: 7]
                move.qr_code_string = qr_data
            else:
                move.qr_code_string = False

    @api.depends('qr_code_string')
    def _compute_qr_code(self):
        for move in self:
            if move.qr_code_string:
                move.x_qr_invoice = self.env['account.move'].generate_qr_code(move.qr_code_string)['x_qr_invoice'] # [cite: 6]
            else:
                move.x_qr_invoice = False

    @api.model
    def generate_qr_code(self, qr_string): # [cite: 11]
        qr = qrcode.QRCode(version=4, box_size=4, border=1) # [cite: 11]
        qr.add_data(qr_string) # [cite: 11]
        qr.make(fit=True) # [cite: 11]
        img = qr.make_image() # [cite: 11]
        buffer = io.BytesIO() # [cite: 11]
        img.save(buffer, format="PNG") # [cite: 11]
        img_str = base64.b64encode(buffer.getvalue()) # [cite: 11]
        return {'x_qr_invoice': img_str} # [cite: 11]