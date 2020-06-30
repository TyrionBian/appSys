from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from flask_restplus import Resource
from flask import request
from app.main.util.dto import ScheduleDto
from app.main.service.producer_service import send_msg

api = ScheduleDto.api
_schedule = ScheduleDto.schedule

@api.route('/')
class ScheduleList(Resource):
    @api.response(201, 'send msg success.')
    @api.doc('send kafka msg')
    @api.expect(_schedule, validate=True)
    def post(self):
        """send msg to kafka producer """
        data = request.json
        return send_msg(data=data)
