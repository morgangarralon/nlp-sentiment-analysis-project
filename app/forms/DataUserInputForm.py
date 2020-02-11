from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class DataUserInputForm(FlaskForm):
        field_data_input = StringField('Put your input', [
                        DataRequired(),
                        Length(min=2, message=('Your input is too short.'))
                ])
        button_submit = SubmitField('Guess!')