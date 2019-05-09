import redis
import hashlib, uuid
from app import config

class Sessions(object):

    def __init__(self):
        if hasattr(config, 'REDIS_PASSWORD'):
            self.instance = redis.StrictRedis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                password=config.REDIS_PASSWORD)
        else:
            self.instance = redis.StrictRedis(
                host= config.REDIS_HOST,
                port=config.REDIS_PORT)


    def get_hashed_password(self,password):

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        return hashed_password
    
    def set_user(self,user,password):
        h_passwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.instance.set(user,h_passwd)


    def get_user_password(self,user):

        password=self.instance.get(user)

        return password

    def delete_user(self, user):
        self.instance.delete(user)
