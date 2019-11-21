from odoo import api, fields, models, _


class productos_unidad_ventas(models.Model):

    _inherit = 'product.template'

    def _get_default_uom_venta_id(self):
        return self.env["product.uom"].search([], limit=1, order='id').id

    uom_venta_id = fields.Many2one('product.uom', 'Unidad de medida venta', default=_get_default_uom_venta_id , required=True)
    product_template_id = fields.One2many('product.product', 'product_tmpl_id', readonly=True, string="Inventario Producto")
    productos_disponible = fields.Float(string="Productos Disponibles", readonly=True, store=True, compute='_calcula_inventatio_producto')

    @api.depends('product_template_id.stock_id.product_qty')
    def _calcula_inventatio_producto(self):
        cantidad = 0
        total = 0
        factor = 0
        for template in self:
            for producto in template.product_template_id:
                for stock in producto.stock_id:
                    cantidad += stock.product_qty

        factor = 1 / template.uom_venta_id.factor
        total = cantidad / factor

        template.update({
            'productos_disponible': total
        })


class productos_inventario(models.Model):

    _inherit = 'product.product'

    stock_id = fields.One2many('stock.move.line', 'product_id', readonly=True, string="Inventario Producto")





