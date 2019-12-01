from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Planets
from application.forms import PlanetsForm, LoginForm, RegisterForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
         return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('login.html', title='Login', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        postData = Users(
        username=form.username.data,
        password=form.password.data,
    )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)
    return render_template('register.html', title='Register', form=form)

@app.route('/planets', methods=['GET', 'POST'])
def planets():
    postData = Planets.query.all()
    form=PlanetsForm()
    if request.form:
        request.form.get('favourite', allow_multiple=True)
        return redirect(url_for('favourites'))
    return render_template('planets.html', title='Planets', planets=postData, form=form)

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='Favourites')


