from odoo import models, fields, api

class unidad_ventas_stock_quant(models.Model):

    _inherit = 'stock.quant'
    unidad_disponible_venta = fields.Float(string="Unidad(es) Disponible Ventas", readonly=True, store=True,
                               compute='_calcular_unidades_disponible_venta')

    @api.multi
    @api.depends('reserved_quantity', 'quantity')
    def _calcular_unidades_disponible_venta(self):
        for rec in self:
            factor = round(1 / rec.product_id.product_tmpl_id.uom_venta_id.factor)
            rec.unidad_disponible_venta = round(rec.quantity - rec.reserved_quantity) / factor

