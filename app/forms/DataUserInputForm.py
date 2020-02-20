from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired

class DataUserInputForm(FlaskForm):
        field_data_input = TextAreaField('Put your input', [
                                                        DataRequired(),
                                                        Length(min=2, message=('Your input is too short.'))
                                                ], render_kw={
                                                        'rows': 3,
                                                        'placeholder': 'Put your input'})
        button_submit = SubmitField('Guess!')