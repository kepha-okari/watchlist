from flask import render_template
from app import application

#Views
@app.route('/')
def index():
    '''
    view rot function that return the index page and its data
    '''
    return render_template('index.html')
