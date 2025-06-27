{
    'name': 'Account Custom Features',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Customizations for Odoo Accounting',
    'depends': ['account', 'sale_management'], # 'sale_management' si quieres vincular a pedidos de venta
    'data': [
        'security/ir.model.access.csv', # Si creas nuevos modelos
        'data/sales_channel_data.xml',
        'views/account_move_views.xml',
        'reports/account_invoice_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}