
from flask_restplus import Api
from flask import Blueprint


from .main.controller.application_controller import api as application_ns
from .main.controller.status_controller import api as status_ns
from .main.controller.schedule_controller import api as schedule_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(application_ns, path='/application')
api.add_namespace(status_ns, path='/status')
api.add_namespace(schedule_ns, path='/schedule')
