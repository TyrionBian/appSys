
from flask import request
from flask_restplus import Resource

from ..util.dto import ApplicationDto
from ..service.application_service import save_new_application, get_all_applications, get_a_application

api = ApplicationDto.api
_application = ApplicationDto.application

@api.route('/')
class ApplicationList(Resource):
    @api.doc('list_of_applications')
    @api.marshal_list_with(_application, envelope='data')
    def get(self):
        """List all applications"""
        return get_all_applications()

    @api.response(201, 'application successfully created.')
    @api.doc('create a new application')
    @api.expect(_application, validate=True)
    def post(self):
        """Creates a new Application """
        data = request.json
        return save_new_application(data=data)


@api.route('/<uuid>')
@api.param('uuid', 'The application identifier.')
@api.response(404, 'application not found.')
class Application(Resource):
    @api.doc('get an application')
    @api.marshal_with(_application)
    def get(self, uuid):
        """get an application given its identifier."""
        application = get_a_application(uuid)
        if not application:
            api.abort(404)
        else:
            return application




