# -*- coding: utf-8 -*-
# from odoo import http


# class Essai(http.Controller):
#     @http.route('/essai/essai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/essai/essai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('essai.listing', {
#             'root': '/essai/essai',
#             'objects': http.request.env['essai.essai'].search([]),
#         })

#     @http.route('/essai/essai/objects/<model("essai.essai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('essai.object', {
#             'object': obj
#         })
