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

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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

@app.route('/home', methods=['GET','POST'])
def home():
    ''' Si el usuario ya hizo login, recupera su nombre. Si no ha hecho login y entro directo a /home, regresalo al login screen '''
    if 'user' in session:
        username = session['user']
    else: 
        return redirect(url_for('login')) 

    mongodb = api.API()
    data = mongodb.get()
    paths = []
    names = []
    locations = []
    descriptions = []

    if request.method == 'POST':
        print('hola')
        autor = request.form['Autor']
        lugar = request.form['Lugar']
        desc = request.form['Desc']
        print(autor)
        print(lugar)
        print(desc)
        return redirect(url_for('upload'))
    
    for i in range(len(data)):
        paths.append(data[i]['picture'])
        names.append(data[i]['name'])
        locations.append(data[i]['location'])
        descriptions.append(data[i]['description'])

    
    return render_template('home.html', user=username, paths=paths, names=names, locations=locations, descriptions=descriptions)

@app.route('/upload', methods=['GET','POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')
    if request.method == 'POST':
        #print('hola')
        if not os.path.isdir(target):
            os.mkdir(target)
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            # This is to verify files are supported
            ext = os.path.splitext(filename)[1]
            if (ext == ".jpg") or (ext == ".png") or (ext == ".jpeg"):
                print("File supported moving on...")
                destination = "/".join([target, filename])
                print("Accept incoming file:", filename)
                print("Save it to:", destination)
                upload.save(destination)
                print('File uploaded')
            return redirect(url_for('home'))
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
