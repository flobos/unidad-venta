from odoo import models, fields, api

class unidad_ventas_uom(models.Model):

    _inherit = 'product.uom'
    unidad_venta = fields.Char(string="Unidad para Venta",required=True)

    @api.multi
    def name_get(self):
        result = []
        for account in self:
            name = account.unidad_venta
            result.append((account.id, name))
        return result
