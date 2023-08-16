# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercityStudent(models.Model):
    _name = 'univercity.student'

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    indentity_card = fields.Char('Identity card')
    adress = fields.Text('Adresse')
    birthday = fields.Date('Birthday')
    inscrition_date = fields.Datetime('Date of inscription')
    email = fields.Char()
    phone = fields.Char()

    #creeation champs many2one
    departement_id = fields.Many2one(comodel_name='univercity.departement')
    classroom_id = fields.Many2one(comodel_name='univercity.classroom')