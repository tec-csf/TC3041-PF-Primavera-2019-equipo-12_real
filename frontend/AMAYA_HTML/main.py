from flask import Flask, request, redirect, url_for, render_template, session
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['pass'] != 'admin':
            error = 'invalid credentials. Please try again.'
        else:
            return render_template('home.html')
    return render_template('index.html', error=error)
    

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))