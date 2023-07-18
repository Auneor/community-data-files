# Copyright 2022 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import re

import logging
from odoo import api, SUPERUSER_ID, _

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return

    cr.execute("DROP TABLE IF EXISTS res_partner_res_partner_nace_rel  RESTRICT;")