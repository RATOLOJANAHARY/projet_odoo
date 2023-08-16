# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercitySubject(models.Model):
    _name = 'univercity.subject'

    name = fields.Char()
    code = fields.Char()


    #objet manytomany plusieurs plusieurs
    proffesor_ids = fields.One2many(comodel_name='univercity.proffesor', inverse_name='departement_id')
    proffesor_ids = fields.One2many(comodel_name='univercity.proffesor', inverse_name='departement_id')
