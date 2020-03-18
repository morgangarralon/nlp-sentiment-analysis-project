from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired
from wtforms import TextAreaField, SubmitField, HiddenField

class DataUserInputForm(FlaskForm):
        field_data_input = TextAreaField('Put your input keywords', [
                                                        DataRequired(),
                                                        Length(min=2, message=('Your input is too short.'))
                                                ], render_kw={
                                                        'rows': 3,
                                                        'placeholder': 'Please, write your input'})
        field_type_input = HiddenField('manual input')
        button_submit = SubmitField('Guess!')