#allows rendering templates
from flask import render_template
#import the app from __init__.py
from app import app

#home route
@app.route('/')
def home():
	return render_template('index.html')

#index route
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}
	#render_template takes the name of the html, and the variables
	#written in the template
	return user
