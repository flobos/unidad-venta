from odoo import models, fields, api

class unidad_ventas_uom(models.Model):

    _inherit = 'product.uom'
    unidadventa_id = fields.Many2one('unidad_ventas.unidadventas', string="Unidad de Ventas", required=True)

    @api.multi
    def name_get(self):
        result = []
        for data_set in self:
           name = data_set.unidadventa_id.name
           result.append((data_set.id, name))
        return result


