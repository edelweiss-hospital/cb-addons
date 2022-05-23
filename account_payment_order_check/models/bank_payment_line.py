# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class BankPaymentLine(models.Model):
    _inherit = "bank.payment.line"

    payment_date = fields.Date(
        related="payment_line_ids.date",
        readonly=True,
        string="Date of payment",
    )
    amount = fields.Monetary(
        related="amount_currency",
        currency_field="currency_id",
        readonly=True,
        string="Monetary amount",
    )
    check_amount_in_words = fields.Text(
        compute="_compute_amount_in_words",
    )
    check_number = fields.Integer(
        string="Check Number",
        readonly=True,
        copy=False,
        default=0,
        help="Number of the check corresponding to this payment.",
    )

    @api.depends("amount_currency")
    def _compute_amount_in_words(self):
        for rec in self:
            rec.check_amount_in_words = rec.currency_id.amount_to_text(
                rec.amount_currency
            )


class AccountPaymentLine(models.Model):
    _inherit = "account.payment.line"

    def _get_check_reference(self):
        invoice = self.move_line_id.move_id
        if invoice and invoice.invoice_payment_ref:
            return invoice.invoice_payment_ref
        return self.name
