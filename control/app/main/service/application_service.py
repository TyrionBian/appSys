import uuid
import datetime


from app.main import db
from app.main.model.application import Application
import base64
from Crypto.Cipher import XOR

__key = 'sult'


def save_new_application(data):
    data['uuid']=str(uuid.uuid4())
    application = Application.query.filter_by(uuid=data['uuid']).first()
    if not application:
        new_application = Application(
            uuid=data['uuid'],
            productNum = data['productNum'],
            channelNum = data['channelNum'],
            name = encrypt(key=__key, plaintext=data['name']),
            idcard = encrypt(key=__key, plaintext=data['idcard']),
            phone = encrypt(key=__key, plaintext=data['phone']),
            applytime = datetime.datetime.now().isoformat(sep=' ')
        )
        save_changes(new_application)
        response_object = {
            'uuid': data['uuid'],
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'uuid already exists.',
        }
        return response_object, 409

def get_all_applications():
    return Application.query.all()


def get_a_application(uuid):
    application = Application.query.filter_by(uuid=uuid).first()
    application.name = decrypt(__key,application.name)
    application.idcard = decrypt(__key,application.idcard)
    application.phone = decrypt(__key,application.phone)
    return application


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def encrypt(key, plaintext):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext)).decode('utf-8')

def decrypt(key, ciphertext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8')


