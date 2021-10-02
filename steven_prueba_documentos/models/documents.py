# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class DocumentsDocument(models.Model):
    _inherit = 'documents.document'

    is_contract_document = fields.Boolean(
        string="Is contract document",
        help=u"Is contract document. With this field, validate the Sale Order field.",
        default=False,
        store=True,
    )

    sale_order_id = fields.Many2one(
        "sale.order",
        string='Sale Order',
        help=u"Sale Order if the document is of a contract.",
        store=True,
    )


class DocumentsTag(models.Model):
    _inherit = "documents.tag"

    is_required_documents_tag = fields.Boolean(
        string="Validate category documents",
        help=u"Validate the category documents as required when confirming the contract. "
             u"There must be at least one document.",
        default=True,
    )
