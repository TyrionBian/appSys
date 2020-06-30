from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import os

bootstrap_servers = os.environ['KAFKA_SERVER']
# produce json messages
producer = KafkaProducer(bootstrap_servers=[bootstrap_servers])

def send_msg(data):
    future = producer.send(topic=data['topic'],
                           key=data['key'].encode('utf-8'),
                           value=data['value'].encode('utf-8'))
    try:
        future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        pass
    response_object = {
        'uuid': data['key'],
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201
