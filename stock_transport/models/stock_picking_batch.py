# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'
    
    
    dock_id = fields.Many2one('stock.transport.dock',string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle',string="Vehicle")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
    weight = fields.Integer(string="Weight",compute="_compute_weight" )
    volume = fields.Integer(string="Volume",compute="_compute_volume",store=True )
    total_volume = fields.Integer(string = 'total volume',compute='_compute_total_volume')
    total_weight = fields.Integer(string = 'total weight', compute='_compute_total_weight')
    transfer = fields.Integer(string = 'transfer', compute='_compute_transfer',store=True)
    lines = fields.Integer(string = 'lines', compute='_compute_lines',store = True)
    
    
    @api.depends('picking_ids.volume', 'vehicle_category_id')
    def _compute_volume(self):
        for record in self:
            record.volume = sum(product.volume for product in record.picking_ids) if record.vehicle_category_id else 0
            
    @api.depends('picking_ids')
    def _compute_total_volume(self):
        for record in self:
            record.total_volume = sum(product.volume for product in record.picking_ids)
            
    @api.constrains('volume')
    def _check_price(self):
        for record in self:
            if (record.volume>record.vehicle_category_id.max_volume):
                raise ValidationError("you cannot overloaded")


    @api.depends('picking_ids.weight', 'vehicle_category_id')
    def _compute_weight(self):
        for record in self:
            record.weight = sum(product.shipping_weight for product in record.picking_ids) if record.vehicle_category_id else 0

    @api.depends('picking_ids')
    def _compute_total_weight(self):
        for record in self:
            record.total_weight = sum(product.shipping_weight for product in record.picking_ids)
        
    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)

    @api.depends('move_ids')
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_ids)

