# -*- coding: utf-8 -*-
{
    'name': "unidad-venta",

    'summary': """
        Agrega una nuevo tipo de unidad solo para la venta y sus reportes""",

    'description': """
        Agrega una nuevo tipo de unidad solo para la venta y sus reportes
    """,

    'author': "Fimar",
    'website': "http://www.fimarcorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/uom.xml',
        'views/unidadventa.xml',
        'views/sale_report_saleorder_document_inherit.xml',
        'views/account_report_invoice_document_inherit.xml',
        'views/menus.xml',
        'views/products.xml',
        'views/stock_report_picking_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}