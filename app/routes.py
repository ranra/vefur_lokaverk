from flask import Flask
import os
from flask import render_template, flash, redirect, url_for
#from new_app.database import *
app = Flask(__name__)
from new_app.config import Config
app.config.from_object(Config)

img_folder = os.path.join("static", "img")

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    img = os.path.join(img_folder, "img2.jpg")
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, img = img, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        #create(form.username.data, "arnar", " blabla", form.password.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
      app.run()