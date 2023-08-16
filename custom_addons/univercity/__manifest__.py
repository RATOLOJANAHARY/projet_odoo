# -*- coding: utf-8 -*-
{
    'name': "univercity",

    'summary': """
        this  Module for University gestion""",

    'description': """
        cette module est creer pour gerer une etablissement universiter
    """,

    'author': "HERMAN",
    'website': "https://web.facebook.com/herman.ralahiniony/?_rdc=1&_rdr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'aplication':True
}
