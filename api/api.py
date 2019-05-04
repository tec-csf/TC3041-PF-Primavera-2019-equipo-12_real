from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from datetime import datetime
from functions import images
from bson import ObjectId


app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def list():
    mongodb = images.Images()

    if request.method == 'POST':
        image = request.data

        result = mongodb.create(image)

        image['_id'] = str(image['_id'])

        return image, status.HTTP_201_CREATED

    return mongodb.find()


@app.route("/<string:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):

    mongodb = images.Images()

    note =  mongodb.find()
    if not note:
        raise exceptions.NotFound()
    else:
        return note

    return jsonify(key)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
