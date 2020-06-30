from flask_restplus import Namespace, fields

class ApplicationDto:
    api = Namespace('application', description='application related operations')
    application = api.model('application', {
        'uuid': fields.String(description='application uuid'),
        'productNum': fields.String(required=True, description='application productNum'),
        'channelNum': fields.String(required=True, description='application channelNum'),
        'name': fields.String(required=True, description='application name'),
        'idcard': fields.String(required=True, description='application idcard'),
        'phone': fields.String(description='application phone'),
        'applytime': fields.String(description='application applytime')
    })

class StatusDto:
    api = Namespace('status', description='status related operations')
    status = api.model('status', {
        'uuid': fields.String(required=True, description='application uuid'),
        'chainid': fields.String(description='status chain id'),
        'chainversion': fields.String(description='status chain version'),
        'status': fields.String(description='status status'),
        'createtime': fields.String(description='status createtime'),
        'updatetime': fields.String(description='status updatetime'),
        'applytime': fields.String(description='application applytime')
    })

class ScheduleDto:
    api = Namespace('schedule', description='schedule related operations')
    schedule = api.model('schedule', {
        'topic': fields.String(required=True, description='topic name'),
        'key': fields.String(required=True, description='msg key'),
        'value': fields.String(required=True, description='msg value')
    })