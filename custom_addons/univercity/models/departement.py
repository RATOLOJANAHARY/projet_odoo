# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercityDepartement(models.Model):
    _name = 'univercity.departement'

    name = fields.Char()
    code = fields.Char()

    # objet many2one ou un ou plusieurs
    departement_id = fields.Many2one(comodel_name='univercity.departement')