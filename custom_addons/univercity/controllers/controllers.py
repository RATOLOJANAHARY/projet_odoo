# -*- coding: utf-8 -*-
# from odoo import http


# class Univercity(http.Controller):
#     @http.route('/univercity/univercity', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/univercity/univercity/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('univercity.listing', {
#             'root': '/univercity/univercity',
#             'objects': http.request.env['univercity.univercity'].search([]),
#         })

#     @http.route('/univercity/univercity/objects/<model("univercity.univercity"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('univercity.object', {
#             'object': obj
#         })
