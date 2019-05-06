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
        
        if user_password.decode() != None and user_password.decode() == password:
            return True
        return False  

    def insertImage(self, owner, path, name, description, location, tags):
        mongodb = images.Images()
        query = {"owner":owner,"picture":path,"name": name,"description": description,"location": location,"tags": ["tag1", "tag2"]}
        result = mongodb.create(query)
        return result

