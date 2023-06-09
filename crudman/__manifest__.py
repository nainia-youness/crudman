# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Crudman', #A module is called by two names one is its technical name which is the main folder name where all the module related folders
    'version': '1.0.0',
    'sequence':-100,#the lower the sequence, the module will show first in apps
    'author': 'Youness Nainia',
    'website': '',#website of author
    'images': ['static/description/icon.png','static/description/banner.gif'],#image path that will be set up as the banner of your module static/wherever
    'category': 'Extra Tools',
    'summary': 'Postman clone module that helps you test webservices',
    'description': """HTTP module""",
    'license':'LGPL-3',
    'depends': [],#specify modules that this module deppend on (they will be loaded)
    'external_dependencies': {'python': [],'bin':[]},#python and binary dependencies 
    'css': [],#custom CSS files to be imported
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'data/response.httpstatus.csv',
        'views/menu.xml',
        'views/request.xml',
        'views/workspace_view.xml',
        'views/response.xml',
        'views/http_status.xml'
    ],#all the data files including XML and CSV files that needed to be loaded when installing the module
    'demo': [],#list of data files that are only loaded when demonstration mode is activated during module installation
    'qweb': [],#loading all your qweb templates
    'installable': True,#whether a module is installable in a server from web UI or not.
    'application': True,#if true , it won t be a module, but an application (the module is independent of other modules)
    'auto_install': False,#If it is true, the module will be automatically installed if all its dependencies are installed.
    'assets': {},
}
