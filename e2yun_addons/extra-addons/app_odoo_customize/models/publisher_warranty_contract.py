# Copyright 2015-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2016 Stanislav Krotov <https://it-projects.info/team/ufaks>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import logging

from odoo import models, api
from odoo.release import version_info

_logger = logging.getLogger(__name__)


class PublisherWarrantyContract(models.AbstractModel):
    _inherit = 'publisher_warranty.contract'

    @api.multi
    def update_notification(self, cron_mode=True):
        is_enterprise = version_info[5] == 'e'
        _logger.debug('is_enterprise=%s', is_enterprise)
        # Running Odoo EE without calling super is illegal. So, make it impossible to disable in enterprise. See README.rst for details
        if is_enterprise and self.env['ir.config_parameter'].get_param('app_send_publisher_warranty_url',default='0') == '1':
            return super(PublisherWarrantyContract, self).update_notification(cron_mode)
        else:
            return True
