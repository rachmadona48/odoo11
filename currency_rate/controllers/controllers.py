# -*- coding: utf-8 -*-
from odoo import http

# class CurrencyRate(http.Controller):
#     @http.route('/currency_rate/currency_rate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/currency_rate/currency_rate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('currency_rate.listing', {
#             'root': '/currency_rate/currency_rate',
#             'objects': http.request.env['currency_rate.currency_rate'].search([]),
#         })

#     @http.route('/currency_rate/currency_rate/objects/<model("currency_rate.currency_rate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('currency_rate.object', {
#             'object': obj
#         })