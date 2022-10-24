# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.move'

    dimension = fields.Char(string='Dimension', readonly=False) # or {related="sale_line_id.dimension"}




