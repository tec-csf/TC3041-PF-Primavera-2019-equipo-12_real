from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from flask_api import FlaskAPI, status, exceptions
from backend import api
import cgi
import os
import jinja2

env = jinja2.Environment()
env.globals.update(zip=zip)

app = FlaskAPI(__name__)
app.jinja_env.filters['zip'] = zip

app.secret_key = "super secret key" # La llave para la sesion

@app.route("/", methods=['GET','POST'])
def login():
    s = api.API()
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        if s.verifyPassword(username, password) == False:
            error = '  Invalid credentials. Please try again.'

        else:
            session['logged_in'] = True
            session['user'] = request.form['username']
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/home')
def home():
    mongodb = api.API()
    data = mongodb.get()
    paths = []
    names = []
    locations = []
    descriptions = []
    
    for i in range(len(data)):
        paths.append(data[i]['picture'])
        names.append(data[i]['name'])
        locations.append(data[i]['location'])
        descriptions.append(data[i]['description'])

    return render_template('home.html', user=session['user'], paths=paths, names=names, locations=locations, descriptions=descriptions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
