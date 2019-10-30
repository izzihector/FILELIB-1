# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'e2yun_Online Ticket Submission',
    'category': 'Website',
    'summary': 'e2yun 服务订单表单在线提交 ',
    'depends': [
        'website_form_editor',
        'website_helpdesk',
        'helpdesk',
        'website_helpdesk_form',
        'im_livechat'
    ],
    'description': """在线提交服务订单.
    """,
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/website_helpdesk.xml',
        'views/helpdesk_templates.xml',
        'views/commonproblems_templates.xml',
        'views/helpdesk_views.xml',
        'views/helpdesk_ticket_brand_type.xml'
    ],
    'license': 'OEEL-1',
}