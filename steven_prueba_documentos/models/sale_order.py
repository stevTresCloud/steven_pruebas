# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'documents.mixin']

    is_sale_contract = fields.Boolean(
        string='Is a sale contract',
        default=False
        )

    def _get_document_tags(self):
        company = self.company_id or self.env.company
        return company.sale_tags

    def _get_document_folder(self):
        company = self.company_id or self.env.company
        return company.sale_folder

    def _check_create_documents(self):
        company = self.company_id or self.env.company
        return company.documents_sale_settings and super()._check_create_documents()

    def _get_document_vals(self, attachment):
        res = super(SaleOrder, self)._get_document_vals(attachment)
        if self.is_sale_contract:
            res['is_contract_document'] = True
            res['sale_order_id'] = self.id
        return res
