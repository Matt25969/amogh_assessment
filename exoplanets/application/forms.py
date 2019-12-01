from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Length

class PlanetsForm(FlaskForm):
    checkbox = BooleanField([DataRequired()])
    submit = SubmitField('Add to favourites')

class LoginForm(FlaskForm):
    username = StringField('Username',
            validators=[
                DataRequired(),
                Length(min=4, max=30)
                ]
            )

    password = StringField('Password',
            validators=[
                DataRequired(),
                Length(min=4, max=30)
                ]
            )

    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField('Username',
            validators=[
                DataRequired(),
                Length(min=4, max=30)
                ]
            )

    password = StringField('Password',
            validators=[
                DataRequired(),
                Length(min=4, max=30)
                ]
            )

    submit = SubmitField('Create Account')



