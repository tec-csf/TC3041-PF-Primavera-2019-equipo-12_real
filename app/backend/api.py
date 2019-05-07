from .functions import images
from .functions import users
from .functions import sessions

class API(object):

    def get(self):
        mongodb = images.Images()
        allImages = mongodb.findAll()
        return allImages

    def getByFilter(self,lugar,usuario,tag):
        mongodb = images.Images()
        i_filter = {}

        if lugar == "" and tag == "" and usuario != "":
            i_filter = {"owner":usuario}
        elif lugar != "" and tag == "" and usuario == "":
            i_filter = {"location":lugar}
        elif lugar != "" and tag == "" and usuario != "":
            i_filter = {"location":lugar,"owner":usuario}
        elif lugar == "" and tag != "" and usuario == "":
            i_filter = {"tags":tag}
        elif lugar == "" and tag != "" and usuario != "":
            i_filter = {"owner":usuario, "tags":tag}
        elif lugar != "" and tag != "" and usuario == "":
            i_filter = {"location":lugar,"tags":tag}
        elif lugar != "" and tag != "" and usuario != "":
            i_filter = {"location":lugar, "owner":usuario, "tags":tag}

        allImages = mongodb.findAllWithFilter(i_filter)
        return allImages


    def verifyPassword(self,user,password):
        s = sessions.Sessions()

        user_password = s.get_user_password(user)
        
        if user_password != None and user_password.decode() == password:
            return True
        return False  

    def insertImage(self, owner, path, name, description, location, tags):
        mongodb = images.Images()
        query = {"owner":owner,"picture":path,"name": name,"description": description,"location": location,"tags": tags}
        result = mongodb.create(query)
        return result
    
    def removeImage(self, owner):
        mongodb = images.Images()
        mongodb.deleteAll(owner)

    def insertUserMongo(self, name, middlename, lastname, email):
        mongodb = users.Users()
        existe = mongodb.findOne(email)
        
        if existe == None:
            query = {"nombre":name,"apellido_m":middlename,"apellido_p": lastname,"_id": email}
            result = mongodb.create(query)
        else:
            result = 'abort'
        return result

    def insertUserRedis(self, user, password):
        s = sessions.Sessions()
        s.set_user(user, password)

    def removeUserMongo(self, email):
        mongodb = users.Users()
        mongodb.delete(email)
    
    def insertUserRedis(self, user, password):
        s = sessions.Sessions()
        s.set_user(user, password)
    
    def removeUserRedis(self, user):
        s = sessions.Sessions()
        s.delete_user(user)
