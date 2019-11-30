from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    checkbox = BooleanField
    submit = SubmitField('Add to favourites')

