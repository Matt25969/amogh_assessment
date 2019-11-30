from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm


@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all()
    return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/planets')
def planets():
    form=PostForm
    if form.validate_on_submit():
        postData= Favourites(
        choice_id=
        user_id=
        planet_id=
    )
        db.session.add(postData)
        db.session.commit
        return redirect(url_for('favourites'))
    return render_template('planets.html', title='Planets', form=form)

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='Favourites')


