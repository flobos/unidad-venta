from odoo import api, fields, models, _


class productos_unidad_ventas(models.Model):

    _inherit = 'product.template'

    def _get_default_uom_venta_id(self):
        return self.env["product.uom"].search([], limit=1, order='id').id

    uom_venta_id = fields.Many2one('product.uom', 'Unidad de medida venta', default=_get_default_uom_venta_id , required=True)



