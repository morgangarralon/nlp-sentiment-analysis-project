from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DataUserInputForm(FlaskForm):
        field_data_input = StringField('Put your input:', validators=[DataRequired()])
        button_submit = SubmitField('Deep input this!')