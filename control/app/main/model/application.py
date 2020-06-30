
from app.main import db
import base64
from Crypto.Cipher import XOR

class Application(db.Model):
    
    """ Model for storing application related details """
    __tablename__ = "application"

    uuid = db.Column(db.String(36), unique=True, primary_key=True, nullable=False)
    productNum = db.Column(db.String(30), nullable=False)
    channelNum = db.Column(db.String(30), nullable=False)

    name = db.Column(db.String(30), nullable=False)
    idcard = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    applytime = db.Column(db.String(20), nullable=False)
    

    # @property
    # def idcard(self):
    #     raise AttributeError('idcard: write-only field')

    # @idcard.setter
    # def idcard(self, idcard):
    #     self.idcard = self.__encrypt('sult',idcard)

    def __encrypt(self, key, plaintext):
        cipher = XOR.new(key)
        return base64.b64encode(cipher.encrypt(plaintext)).decode('utf-8')




