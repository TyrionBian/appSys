from flask import request
from flask_restplus import Resource

from app.main.util.dto import StatusDto
from app.main.service.status_service import save_new_status, update_status, get_all_status, get_a_status

api = StatusDto.api
_status = StatusDto.status

@api.route('/')
class StatusList(Resource):
    @api.doc('list_of_status')
    @api.marshal_list_with(_status, envelope='data')
    def get(self):
        """List all status"""
        return get_all_status()

    @api.response(201, 'status successfully created.')
    @api.doc('create a new status')
    @api.expect(_status, validate=True)
    def post(self):
        """Creates a new Status """
        data = request.json
        return save_new_status(data=data)


@api.route('/uuid/<uuid>')
@api.param('uuid', 'The status identifier.')
@api.response(404, 'status not found.')
class Status(Resource):
    @api.doc('get an status')
    @api.marshal_with(_status)
    def get(self, uuid):
        """get an status given its identifier."""
        status = get_a_status(uuid)
        if not status:
            api.abort(404)
        else:
            return status


@api.route('/uuid/')
@api.response(404, 'status not found.')
class StatusUpdate(Resource):    
    @api.response(201, 'status successfully update.')
    @api.doc('update a new status')
    @api.expect(_status, validate=True)
    def post(self):
        """Update a new Status """
        data = request.json
        return update_status(data)