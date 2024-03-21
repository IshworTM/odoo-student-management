{
    'name': 'Student Report',
    'version': '3.02',
    'description': 'A student report module for Odoo',
    'summary': 'Student report module',
    'author': 'Rowshi',
    'license': 'LGPL-3',
    'depends': ['base', 'student_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_report_views.xml'
    ],
    'installable': True,
    'application': True,
}