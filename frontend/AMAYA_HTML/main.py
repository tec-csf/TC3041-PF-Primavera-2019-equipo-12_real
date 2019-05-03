from flask import Flask, request, redirect, url_for, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello", methods=['POST'])
def hello():
    first_name= request.form['firts_name']
    template= jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)