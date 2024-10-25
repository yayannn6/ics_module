# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_double_currency  = fields.Boolean("Double Currency")
    other_currency      = fields.Many2one("res.currency", string="Other Currency")
    rate                = fields.Float("Rate")
    total_other_cur     = fields.Monetary("Total")
    total_tax_other_cur = fields.Monetary("Tax Total")
    untaxed_other_cur   = fields.Monetary("Amount untaxed")

    @api.onchange('rate', 'invoice_line_ids')
    def onchange_rate(self):
        for rec in self:
            untaxed = 0
            if rec.is_double_currency:
                for line in rec.invoice_line_ids:
                    line.price_unit_currency = line.price_unit * rec.rate
                    line.subtotal_other_currency = line.total_amount * rec.rate
                    untaxed += line.subtotal_other_currency

                rec.untaxed_other_cur = untaxed
                rec.total_tax_other_cur = rec.rate * rec.amount_tax
                rec.total_other_cur = rec.rate * rec.amount_total




class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit_currency     = fields.Monetary("Price other currency")
    subtotal_other_currency = fields.Monetary("Subtotal other currency")


