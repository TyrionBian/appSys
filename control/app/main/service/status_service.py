import uuid
import datetime


from app.main import db
from app.main.model.status import Status

def save_new_status(data):
    status = Status.query.filter_by(uuid=data['uuid']).first()
    now = datetime.datetime.now().isoformat(sep=' ')
    if not status:
        new_status = Status(
            uuid=data['uuid'],
            chainid = data['chainid'],
            chainversion = data['chainversion'],
            status = data['status'],
            createtime = now,
            updatetime = now,
            applytime = data['applytime']
        )
        save_changes(new_status)
        response_object = {
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

def update_status(data):
    status = Status.query.filter_by(uuid=data['uuid']).first()
    now = datetime.datetime.now().isoformat(sep=' ')
    if not status:
        response_object = {
            'status': 'fail',
            'message': 'uuid do not exists.',
        }
        return response_object, 409
    else:
        for key,_ in data.items():
            setattr(status, key, data[key])
        status.updatetime = now
        update_changes()
        response_object = {
            'status': 'success',
            'message': 'Successfully update.'
        }
        return response_object, 201
        

def get_all_status():
    return Status.query.all()


def get_a_status(uuid):
    return Status.query.filter_by(uuid=uuid).first()


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()
    
def update_changes():
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

