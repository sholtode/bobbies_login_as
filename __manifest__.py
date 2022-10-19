# -*- coding: utf-8 -*-
# (C) 2021 Bobbies (<https://www.bobbies.com>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
# add branch 15.0 for Odoo 15 - 2022 MS Systems e.K. (<https://mw-systems.eu>)

{
    'name': 'Login as another user',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Tools',
    'author': 'Bobbies',
    'website': 'https://bobbies.com',
    'depends': [
        'web',
    ],
    'data': [
        'security/login_as_security.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'wizards/login_as_views.xml',
    ],
    'qweb': [
        'static/src/xml/login_as.xml',
    ],
    'installable': True,
    'application': True,
}
