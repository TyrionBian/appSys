from app.main import db

class Status(db.Model):
    
    """ Model for storing status related details """
    __tablename__ = "status"

    uuid = db.Column(db.String(36), unique=True, primary_key=True, nullable=False)
    chainid = db.Column(db.String(30), nullable=False)
    chainversion = db.Column(db.String(30), nullable=False)

    status = db.Column(db.String(30), nullable=False)
    createtime = db.Column(db.String(30), nullable=False)
    updatetime = db.Column(db.String(20), nullable=False)
    applytime = db.Column(db.String(20), nullable=False)
    


