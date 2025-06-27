{
    'name': 'POS Custom Features',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Customizations for Odoo Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_views.xml', # Para vistas de backend si fuera necesario
        'data/ir_ui_view_data.xml', # Si necesitas modificar ir.ui.view para el listado
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_custom_features/static/src/js/pos_models.js',
            'pos_custom_features/static/src/xml/pos_templates.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}