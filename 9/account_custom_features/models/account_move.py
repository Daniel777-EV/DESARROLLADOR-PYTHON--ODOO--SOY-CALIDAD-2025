# -*- coding: utf-8 -*-
# ... (imports y clase AccountMove existente)

class AccountMove(models.Model):
    _inherit = 'account.move'

    # ... (Campos existentes)

    picking_ids = fields.Many2many(
        'stock.picking',
        string='Transferencias Relacionadas',
        compute='_compute_picking_ids',
        store=True,
        help="All stock pickings related to the sales order that generated this invoice."
    )

    @api.depends('invoice_origin_id') # invoice_origin_id es el pedido de venta (sale.order)
    def _compute_picking_ids(self):
        for move in self:
            if move.invoice_origin_id and move.invoice_origin_id._name == 'sale.order':
                # Obtener los pickings asociados al pedido de venta
                pickings = self.env['stock.picking'].search([
                    ('sale_id', '=', move.invoice_origin_id.id)
                ])
                move.picking_ids = [(6, 0, pickings.ids)]
            else:
                move.picking_ids = False