from odoo import models, fields, api

class unidad_ventas_uom(models.Model):

    _inherit = 'product.uom'
    unidadventa_id = fields.Many2one('unidad_ventas.unidadventas', string="Unidad de Ventas", required=True)

    @api.multi
    def name_get(self):
        result = []
        for data_set in self:
           for unidad in data_set.unidadventa_id:
                nombre = str(unidad.name)
                result.append((data_set.id, nombre))
        return result


