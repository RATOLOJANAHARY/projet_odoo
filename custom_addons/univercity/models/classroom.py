# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnivercityClassroom(models.Model):
    _name = 'univercity.classroom'

    name = fields.Char()
    code = fields.Char()