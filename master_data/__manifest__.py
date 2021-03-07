# -*- coding: utf-8 -*-
{
    'name': "Master Data",

    'summary': """Data Test""",

    'description': """
    """,

    'author': "Hall",

    'category': 'Data SET',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',

        'views/cron_data.xml',
        'views/master_data.xml',
    ],

}