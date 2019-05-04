from flask import Flask, request, redirect, url_for, render_template, session
from flask_api import FlaskAPI, status, exceptions
import cgi
import os

app = FlaskAPI(__name__)

@app.route("/", methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['pass'] != 'admin':
            error = 'invalid credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
