# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Transport Management System',
    'version': '1.2',
    'summary': 'stocks',
    'category': 'Real Estate/Invoicing',
    'depends': ['fleet','stock_picking_batch'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_batch_views.xml',
        'views/fleet_vehicle_model_category_views.xml',
    ],
    'demo': [],
    'application': True,
    'license': "LGPL-3",
    
}