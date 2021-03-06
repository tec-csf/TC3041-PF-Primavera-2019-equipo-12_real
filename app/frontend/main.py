from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from flask_api import FlaskAPI, status, exceptions
from app.api import api
import cgi
import os
import jinja2
''' para separar un string por espacios o comas '''
import re 

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
    owners = []
    names = []
    locations = []
    descriptions = []
    tags = []

    if request.method == 'POST' and 'Title' in request.form:
        title = request.form['Title']
        lugar = request.form['Lugar']
        desc = request.form['Desc']
        tags = request.form['Tags']

        target = os.path.join(APP_ROOT, 'static/images')
        target_db = 'static/images'
        if not os.path.isdir(target):
            os.mkdir(target)
        for upload in request.files.getlist("file"):
            filename = upload.filename
            # This is to verify files are supported
            ext = os.path.splitext(filename)[1]
            if (ext == ".jpg") or (ext == ".png") or (ext == ".jpeg"):
                destination = "/".join([target, filename])
                destination_db = "/".join([target_db, filename])
                upload.save(destination)
                split_tags = re.split('; |, | |,|;', tags)
                insertResult = mongodb.insertImage(username, destination_db, title, desc, lugar, split_tags)

        return redirect(url_for('home'))

    if request.method == 'POST' and 'Lugar_filter' in request.form:
        lugar = request.form['Lugar_filter']
        owner = request.form['Owner']
        tag = request.form['Tag']
        
        data = mongodb.getByFilter(lugar,owner,tag)

    if request.method == 'POST' and 'Title_borrar' in request.form:
        titulo = request.form['Title_borrar']
        mongodb.removeSpecificImage(titulo, username)
        data = mongodb.get()


        
        
    for i in range(len(data)):
        paths.append(data[i]['picture'])
        owners.append(data[i]['owner'])
        names.append(data[i]['name'])
        locations.append(data[i]['location'])
        descriptions.append(data[i]['description'])
        tags.append(data[i]['tags'])

    
    return render_template('home.html', user=username, paths=paths, owners=owners, names=names, locations=locations, descriptions=descriptions, tags=tags)

@app.route("/signUp", methods=['POST','GET'])
def signUp():
    error = None
    r = api.API()
    
    if request.method == 'POST':
        name = request.form['name']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['re_password']
        mongodb = api.API()
        s = api.API()
        
        if password != password2:
            error = 'Passwords do not match! Try again!'
        if password == password2:
            if len(password) < 5:
                error = 'Passwords length must be at least 5 characters long!'
            elif (len(name) > 0 and len(middlename) > 0 and len(lastname) > 0):
                #do something
                insertUser = mongodb.insertUserMongo(name, middlename, lastname, email)
                if(insertUser != 'abort'):
                    s.insertUserRedis(email,password)
                    print('good')
                    return redirect(url_for('login'))
                else:
                    error = 'Email already exists! Try again!'
            else:
                error = 'You have to fill every section!'
    return render_template('signup.html', error=error)

@app.route("/logOut")
def logOut():
    session.clear()
    return redirect(url_for('login'))

@app.route("/delete")
def delete():
    username = session['user']
    r = api.API()
    r.removeUserRedis(username)
    r.removeImage(username)
    r.removeUserMongo(username)
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
