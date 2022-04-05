# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Timesheet With Subtotal',
    'version': '15.1.0',
    'summary' : 'Report Timesheet with Subtotal in account.analytic.line',
    'author': '',
    'description':"""
       
    """,
    'category' : 'Customization',
    'depends':['hr_timesheet'],
    'data' : [
       'report/report_timesheet_with_subtotal_templates.xml',
       'report/report_timesheet_with_subtotal.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license':'LGPL-3',
}
