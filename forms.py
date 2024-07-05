from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CompareForm(FlaskForm):
    player1 = StringField('Player 1',
    validators=[DataRequired(), Length(min=2, max=20)])
    player2 = StringField('Player 2',
    validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Compare')