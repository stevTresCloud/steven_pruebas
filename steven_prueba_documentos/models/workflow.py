# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class WorkflowActionRulesaleOrder(models.Model):
    _inherit = ['documents.workflow.rule']

    has_business_option = fields.Boolean(default=True, compute='_get_business')
    create_model = fields.Selection(selection_add=[('sale.order', "Sale Order")])

    def create_record(self, documents=None):
        rv = super(WorkflowActionRulesaleOrder, self).create_record(documents=documents)
        if self.create_model == 'sale.order':
            # TODO: Realizar wizard de carga de archivos para ordenes de venta desde la interfaz de documentos, indicando si es para un contrato o es para una órden de venta normal
            sale_order = self.env[self.create_model].create({'name': 'sale order created from Documents'})
            for document in documents:
                # this_document is the document in use for the workflow
                this_document = document
                if (document.res_model or document.res_id) and document.res_model != 'documents.document':
                    attachment_copy = document.attachment_id.with_context(no_document=True).copy()
                    this_document = document.copy({'attachment_id': attachment_copy.id})
                this_document.write({
                    'res_model': sale_order._name,
                    'res_id': sale_order.id,
                })

            view_id = sale_order.get_formview_id()
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'name': "New sale order",
                'context': self._context,
                'view_mode': 'form',
                'views': [(view_id, "form")],
                'res_id': sale_order.id if sale_order else False,
                'view_id': view_id,
            }
        return rv
