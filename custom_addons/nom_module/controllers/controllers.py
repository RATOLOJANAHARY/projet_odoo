# -*- coding: utf-8 -*-
# from odoo import http


# class NomModule(http.Controller):
#     @http.route('/nom_module/nom_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nom_module/nom_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nom_module.listing', {
#             'root': '/nom_module/nom_module',
#             'objects': http.request.env['nom_module.nom_module'].search([]),
#         })

#     @http.route('/nom_module/nom_module/objects/<model("nom_module.nom_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nom_module.object', {
#             'object': obj
#         })
