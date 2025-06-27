# -*- coding: utf-8 -*-
from odoo import fields, models

class ResSalesChannel(models.Model):
    _name = 'res.sales.channel'
    _description = 'Sales Channel'

    name = fields.Char(string='Sales Channel', required=True, translate=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The sales channel name must be unique !')
    ]