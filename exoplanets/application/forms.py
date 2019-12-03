from flask_wtf import FlaskForm
from flask_login import LoginManager, current_user
from wtforms import BooleanField, SubmitField, StringField, PasswordField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput
from application import app
from application.models import Users

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
                
class ExampleForm(FlaskForm):
    choices = MultiCheckboxField('Routes', coerce=int)
    submit = SubmitField("Set User Choices")

#class PlanetsForm(FlaskForm):
    #checkbox = BooleanField('Add')
    
    #submit = SubmitField('Add to favourites')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
        validators=[DataRequired()])
                                        
    remember = BooleanField('Remember me')
    
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
        validators= [DataRequired(), EqualTo('password')])
                                                
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')

class UpdateAccountForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(), Email()])                             
    
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')



