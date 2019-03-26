# HOME PAGE ROUTE

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)
