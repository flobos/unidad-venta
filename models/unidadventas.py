from odoo import models, fields, api

class prescricion(models.Model):
    _name = "unidad_ventas.unidadventas"
    _order = 'id'

    name = fields.Char(string="Nombre", required=True)