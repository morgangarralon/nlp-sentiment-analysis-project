from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired
from wtforms import TextField, SubmitField, HiddenField

class DataApiInputForm(FlaskForm):
        field_data_input = TextField('Put your input', [
                                                        DataRequired(),
                                                        Length(min=2, message=('Your input is too short.'))
                                                ], render_kw={'placeholder': 'Please, write some keywords'})
        field_type_input = HiddenField('Twitter')
        button_submit = SubmitField('Guess!')