from functions import images

class API(object):

    def get(self):
        mongodb = images.Images()
        return mongodb.find()

