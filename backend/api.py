from functions import images, sessions

class API(object):

    def get(self):
        mongodb = images.Images()
        return mongodb.find()


    def verifyPassword(self,user,password):
        s = sessions.Sessions()

        user_password = s.get_user_password(user)
        
        if user_password != None and user_password == password:
            return True
        return False  
