# -*- coding: utf-8 -*-
{
    'name': "Steven documentos ventas",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Prueba de documentos en ventas
    """,
    'author': 'TRESCLOUD CIA LTDA',
    'maintainer': 'TRESCLOUD CIA LTDA',
    'website': 'http://www.trescloud.com',
    'category': 'Productivity/Documents',
    'version': '1.0',

    'depends': ['documents', 'sale_management'],

    'data': [
        # Data
        'data/sale_documents_data.xml',

        # Views
        'views/documents_views.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
