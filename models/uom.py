from odoo import models, fields, api

class unidad_ventas_uom(models.Model):

    _inherit = 'product.uom'
    unidadventa_id = fields.Many2one('unidad_ventas.unidadventas', string="Unidad de Ventas", required=True)

    @api.multi
    def name_get(self):
        result = []
        for obj in self:
         # name = '[' +obj.name + ']' + ' ' + str(obj.unidadventa_id.name)
         name = '[' + str(obj.name) + ']'

        result.append((obj.id, name))
        return result


