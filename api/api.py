from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from datetime import datetime
from functions import images
from bson import ObjectId


app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def list():
    mongodb = images.Images()
    return mongodb.find()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
