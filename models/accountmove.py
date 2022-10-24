# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string='Dimension', readonly=True)

