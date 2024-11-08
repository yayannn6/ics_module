# -*- coding: utf-8 -*-

from odoo import models, fields, api
from decimal import Decimal, ROUND_DOWN


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_double_currency  = fields.Boolean("Double Currency")
    other_currency      = fields.Many2one("res.currency", string="Other Currency")
    rate                = fields.Float("Rate", digits=(16, 4))
    total_other_cur     = fields.Monetary("Total")
    total_tax_other_cur = fields.Monetary("Tax Total")
    untaxed_other_cur   = fields.Monetary("Amount untaxed")

    @api.onchange('rate', 'invoice_line_ids')
    def onchange_rate(self):
        for rec in self:
            untaxed = 0.0  # Tetap gunakan float
            if rec.is_double_currency:
                for line in rec.invoice_line_ids:
                    # Kalkulasi dengan pembulatan langsung ke dua desimal
                    line.price_unit_currency = round(line.price_unit * rec.rate, 2)
                    line.subtotal_other_currency = round(line.price_subtotal * rec.rate, 2)
                    untaxed += line.subtotal_other_currency
    
                rec.untaxed_other_cur = round(untaxed, 2)
                rec.total_tax_other_cur = round(untaxed * 0.09, 2)
                rec.total_other_cur = round(untaxed + rec.total_tax_other_cur, 2)





class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit_currency     = fields.Monetary("Price other currency")
    subtotal_other_currency = fields.Monetary("Subtotal other currency")


