from flask import Flask
import os
from flask import render_template, flash, redirect, url_for, send_from_directory
from app.database import *
app = Flask(__name__)
from app.config import Config
app.config.from_object(Config)

img_folder = os.path.join("static", "img")

from app.forms import LoginForm

image_names = os.listdir('./img')
list_length = len(image_names)
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
        create( form.username.data, "arnar", " blabla", form.password.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)



@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("img", filename)

@app.route('/gallery')
def get_gallery():
    img_list = get_img()

    #check()
    #image_names = os.listdir('./img')
    list_length= len(img_list)
    return render_template("gallery.html", image_names=img_list, list_length = list_length)

if __name__ == '__main__':
      app.run()