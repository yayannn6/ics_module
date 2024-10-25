# -*- coding: utf-8 -*-
# from odoo import http


# class IcsModule(http.Controller):
#     @http.route('/ics_module/ics_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ics_module/ics_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ics_module.listing', {
#             'root': '/ics_module/ics_module',
#             'objects': http.request.env['ics_module.ics_module'].search([]),
#         })

#     @http.route('/ics_module/ics_module/objects/<model("ics_module.ics_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ics_module.object', {
#             'object': obj
#         })
