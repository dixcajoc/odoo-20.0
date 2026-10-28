from odoo import http
from odoo.http import request

"""
class School(http.Controller):
    @http.route('/school/school', auth='public')
    def index(self, **kw):
        projects = http.request.env['project.project'].search([])
        for project in projects:
            print(project['name'])
        #return projects
        return "Projects printed in the console"
"""

class School(http.Controller):

    @http.route(
        '/api/projects',
        #type='json',
        type='http',
        auth='public',
        methods=['GET'],
        csrf=False
    )
    def get_projects(self):

        projects = request.env['project.project'].sudo().search([])

        result = []

        for project in projects:
            result.append({
                'id': project.id,
                'name': project.name,
                'active': project.active,
            })

        return request.make_json_response( {
            'success': True,
            'data': result
        })

    @http.route(
    '/api/projects/<int:project_id>',
    #type='json',
    type='http',
    auth='public',
    methods=['GET'],
    csrf=False
    )
    
    
    def get_project(self, project_id):

        project = request.env['project.project'].sudo().browse(project_id)

        if not project.exists():
            return request.make_json_response({
                'success': False,
                'message': 'Project not found'
            })

        return request.make_json_response({
            'success': True,
            'data': {
                'id': project.id,
                'name': project.name,
                'active': project.active,
            }
        })

    


