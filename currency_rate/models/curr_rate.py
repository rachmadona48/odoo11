# -*- coding: utf-8 -*-

from odoo import models, fields, api
from time import strftime
import datetime


class currency_rate(models.Model):
    _inherit = 'res.currency.rate'

    kurs_jual = fields.Float(string="Selling Rate",digits=(16,2),index=True)
    kurs_beli = fields.Float(string="Buying Rate",digits=(16,2))
    # divider = fields.Float(string="Divider",digits=(16,2))

    @api.onchange('kurs_jual','kurs_beli')
    def _curr(self):
        # print(self.name)
        # print(self.currency_id.rate)
        idr = self.env['res.currency'].search([('name', '=', 'IDR')])

        if self.kurs_jual != 0 and self.kurs_beli !=0 and idr.rate != False:
            rate = round(((self.kurs_jual + self.kurs_beli)/2),2)
            self.rate = idr.rate/rate
        else:
            rate = 0
            self.rate = 0

        # print('rate : ',rate)

    # @api.model
    # def create(self, values):
    #     # print(self.currency_id)
    #     print('mmmmmmm')

