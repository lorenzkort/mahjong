from ast import Sub
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class GameStart(FlaskForm):

    submit = SubmitField('Exchange flowers')

