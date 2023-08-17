# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercityDepartement(models.Model):
    _name = 'univercity.departement'

    name = fields.Char()
    code = fields.Char()

    # objet many2one ou un ou plusieurs
    departement_ids = fields.One2many(comodel_name='univercity.proffesor',inverse_name='departement_id')
    subject_ids = fields.One2many(comodel_name='univercity.subject'.inverse_name='departement.id')
