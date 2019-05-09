from pymongo import MongoClient
from bson import ObjectId
from flask import Flask, request, url_for, jsonify
from app import config

class Users(object):
    
    def __init__(self):
        '''
            Para poder usar el URI: python -m pip install pymongo[srv]
            '''
        client = MongoClient(config.MONGO_URI)
        db = client.AMAYA
        self.collection = db.users
    
    def create(self, user):
        """
            Insertar un usuario nuevo            """
        result = self.collection.insert_one(user)
        
        return result
    
    def findOne(self, id):
        """
            Obtener el usuario con id
            """
        result = self.collection.find_one({'_id': id})
        
        if result is not None:
            result['_id'] = str(result['_id'])
        
        return result
    
    def delete(self, id):
        """
            Eliminar un usuario
            """
        result = self.collection.delete_one({'_id': id})
        
        return result

