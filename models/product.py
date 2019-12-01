from odoo import api, fields, models, _


class productos_unidad_ventas(models.Model):

    _inherit = 'product.template'

    def _get_default_uom_venta_id(self):
        return self.env["product.uom"].search([], limit=1, order='id').id

    uom_venta_id = fields.Many2one('product.uom', 'Unidad de medida venta', default=_get_default_uom_venta_id , required=True)
    product_template_id = fields.One2many('product.product', 'product_tmpl_id', readonly=True)
    product_stock_quant = fields.One2many('stock.quant', 'product_tmpl_id', readonly=True)
    productos_disponible = fields.Float(string="Productos Disponibles", readonly=True, store=True, compute='_calcula_inventatio_producto')

    @api.depends('product_stock_quant.unidad_disponible_venta')
    def _calcula_inventatio_producto(self):
        total = 0
        for product in self:
            for quant in product.product_stock_quant:
                if quant.company_id.id != False:
                    print(quant.company_id.id)
                    print(quant.unidad_disponible_venta)
                    total += quant.unidad_disponible_venta

        product.productos_disponible = total

    def action_open_quants(self):
        products = self.mapped('product_variant_ids')
        action = self.env.ref('stock.product_open_quants').read()[0]
        action['domain'] = [('product_id', 'in', products.ids)]
        action['context'] = {'search_default_internal_loc': 1}
        return action

class productos_inventario(models.Model):

    _inherit = 'product.product'

    stock_id = fields.One2many('stock.move.line', 'product_id', readonly=True, string="Inventario Producto")





