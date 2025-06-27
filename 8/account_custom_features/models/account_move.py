# -*- coding: utf-8 -*-
# ... (imports y clase AccountMove existente)
from datetime import datetime # Asegúrate de importar datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    # ... (Campos existentes)

    # Odoo ya tiene 'invoice_date' (date) y 'date' (datetime para el asiento contable)
    # Vamos a usar un campo nuevo o modificar el existente si es posible sin conflictos.
    # Es más seguro crear un nuevo campo datetime si invoice_date debe ser solo fecha.
    # Si invoice_date es tipo Date, lo extenderemos y haremos invisible.

    # Nuevo campo para fecha y hora de emisión
    date_issue_datetime = fields.Datetime(
        string="Fecha de Emisión", [cite: 14]
        default=fields.Datetime.now, # Por defecto la fecha y hora actual
        copy=False
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'date_issue_datetime' not in vals:
                # Si no se proporciona, usa la fecha de la factura si existe, sino la actual
                if 'invoice_date' in vals and vals['invoice_date']:
                    vals['date_issue_datetime'] = fields.Datetime.to_string(fields.Date.from_string(vals['invoice_date']))
                else:
                    vals['date_issue_datetime'] = fields.Datetime.now()
        return super().create(vals_list)

    @api.onchange('invoice_date')
    def _onchange_invoice_date_set_issue_datetime(self):
        if self.invoice_date and not self.date_issue_datetime:
            # Si invoice_date cambia y date_issue_datetime no está establecido, sincronizar
            self.date_issue_datetime = fields.Datetime.to_string(fields.Date.from_string(self.invoice_date))