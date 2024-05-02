# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    
    volume = fields.Float(string="Volume", compute="_compute_volume", default=0)

    
    @api.depends('move_ids_without_package')
    def _compute_volume(self):
        for record in self:
            volume = 0
            for move in record.move_ids_without_package:
                volume += move.product_id.volume * move.quantity
            record.volume = volume
        return True
