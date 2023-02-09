from flask_wtf import FlaskForm
from wtforms import SubmitField

class RefreshForm(FlaskForm):
    submit = SubmitField('Refresh')