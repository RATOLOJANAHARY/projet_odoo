# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercityProffesor(models.Model):
    _name = 'univercity.proffesor'

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    indentity_card = fields.Char('Identity card')
    adress = fields.Text('Adresse')
    birthday = fields.Date('Birthday')
    start_date = fields.Datetime('Date to Start')
    email = fields.Char()
    phone = fields.Char()

    departement_id = fields.Many2one(comodel_name='univercity.departement')
    subject_id = fields.Many2one(comodel_name='univercity.subject')