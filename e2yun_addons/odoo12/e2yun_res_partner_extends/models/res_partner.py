# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing tailsde.
from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    @api.multi
    def _compute_strategic_edit(self):
        is_edit = False
        if self.user_has_groups('e2yun_customer_info.group_crm_sale_lead'):
            is_edit = True
        for s in self:
            s.strategic_edit = is_edit

    parent_account = fields.Many2one('res.partner',string='Parent Account',domain="[('customer','=',True)]")
    is_strategic = fields.Boolean(string='Is Strategic')
    strategic_edit = fields.Boolean(string='Strategic Edit',compute=_compute_strategic_edit)


    _sql_constraints = [
        ('name_unique', 'unique(name)', "The name you entered already exists"),
    ]