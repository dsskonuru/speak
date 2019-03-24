# HOME PAGE ROUTE

from flask import render_template
from app import app

# routes are the different URLs that the application implements
@app.route('/') # decorator modifies the following function
@app.route('/index')
def index():
    user = {'username': 'Kaka'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'hallaleuajh!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I am Ironman!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
