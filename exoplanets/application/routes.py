from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Planets, Users, Favourites
from application.forms import PlanetsForm, LoginForm, RegisterForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('planets'))
    return render_template('register.html', title='Register', form=form)

@app.route('/planets', methods=['GET', 'POST'])
def planets():
    postData = Planets.query.all()
    form=PlanetsForm()
    if form.validate_on_submit:
        planetData = Favourites(
        planet_id=Planets.query.with_entities(Planets.planet_id)
    )        

        db.session.add(planetData)
        db.session.commit()
        return redirect(url_for('favourites'))
    return render_template('planets.html', title='Planets', planets=postData, form=form)

@app.route('/favourites')
@login_required
def favourites():
    if user:
        favouritesData = Favourites.query.all()
    return render_template('favourites.html', title='Favourites', favourites=favouritesData)

login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))




