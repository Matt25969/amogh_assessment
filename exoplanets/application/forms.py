from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    checkbox = BooleanField([DataRequired()])
    submit = SubmitField('Add to favourites')

