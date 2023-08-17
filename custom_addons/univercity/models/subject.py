# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercitySubject(models.Model):
    _name = 'univercity.subject'

    name = fields.Char()
    code = fields.Char()


    #objet manytomany plusieurs plusieurs
    departement_id = fields.Many2one(comodel_name='univercity.departement')
    #classroom_id = fields.Many2one(comodel_name='univercity.classroom')

