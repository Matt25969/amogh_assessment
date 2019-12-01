from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Planets
from application.forms import PostForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/planets', methods=['GET', 'POST'])
def planets():
    postData = Planets.query.all()
    form=PostForm()
    if request.form:
        request.form.get('favourite', allow_multiple=True)
        return redirect(url_for('favourites'))
    return render_template('planets.html', title='Planets', planets=postData, form=form)

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='Favourites')


