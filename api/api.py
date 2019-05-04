from datetime import datetime
from functions import images
from bson import ObjectId


class API(object):

    def list(self):
        mongodb = images.Images()
        return mongodb.find()

