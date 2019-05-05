from .functions import images
from .functions import sessions

class API(object):

    def get(self):
        mongodb = images.Images()
        allImages = mongodb.find()
        return allImages


    def verifyPassword(self,user,password):
        s = sessions.Sessions()

        user_password = s.get_user_password(user)
        
        if user_password != None and user_password == password:
            return True
        return False  

