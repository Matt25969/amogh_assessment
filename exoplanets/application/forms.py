from flask_wtf import FlaskForm
from flask_login import LoginManager
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import app
from application.models import Users

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class PlanetsForm(FlaskForm):
    checkbox = BooleanField('Add',validators=[DataRequired()])
    submit = SubmitField('Add to favourites')

class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
                ]
            )

    password = StringField('Password',
            validators=[
                DataRequired(),
                ]
            )

    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
                ]
            )

    password = PasswordField('Password',
            validators=[
                DataRequired(),
                ]
            )

    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use!')



