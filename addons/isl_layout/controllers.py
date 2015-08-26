# -*- coding: utf-8 -*-
from openerp import http

# class IslLayout(http.Controller):
#     @http.route('/isl_layout/isl_layout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isl_layout/isl_layout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('isl_layout.listing', {
#             'root': '/isl_layout/isl_layout',
#             'objects': http.request.env['isl_layout.isl_layout'].search([]),
#         })

#     @http.route('/isl_layout/isl_layout/objects/<model("isl_layout.isl_layout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isl_layout.object', {
#             'object': obj
#         })