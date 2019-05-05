from datetime import datetime
from functions import images
from bson import ObjectId


class API(object):

    def getAll(self):
        mongodb = images.Images()
        return mongodb.find()

