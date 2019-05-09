from pymongo import MongoClient
from bson import ObjectId
from flask import Flask, request, url_for, jsonify
from app import config

class Images(object):

    def __init__(self):
        '''
        Para poder usar el URI: python -m pip install pymongo[srv]
        '''
        client = MongoClient(config.MONGO_URI)
        db = client.AMAYA
        self.collection = db.images

    def findAll(self):
        """
        Obtener todos las imagenes
        """
        cursor = self.collection.find()

        images = []

        for image in cursor:
            image['_id'] = str(image['_id']) 
            images.append(image)

        return images

    def findAllWithFilter(self, i_filter):
        """
        Obtener todos las imagenes
        """
        cursor = self.collection.find(i_filter)

        images = []

        for image in cursor:
            image['_id'] = str(image['_id']) 
            images.append(image)

        return images

    def findOne(self, id):
        """
        Obtener la imagen con id
        """
        image = self.collection.find_one({'_id': ObjectId(id)})

        if image is not None:
            image['_id'] = str(image['_id'])

        return image


    def create(self, imagen):
        """
        Insertar una imagen nueva
        """
        result = self.collection.insert_one(imagen)

        return result

    def delete(self, id):
        """
        Eliminar una imagen
        """
        result = self.collection.delete_one({'_id': ObjectId(id)})

        return result

    def deleteAll(self, id):
        """
            Eliminar todas las imágenes
            """
        result = self.collection.delete_many({'owner': id})
        
        return result
    def deleteByFilter(self, query):
        result = self.collection.delete_many(query)

        return result
