# from ...app import app # with 'flask run' command
from app import app # with Visual Studio Code
from flask import render_template, redirect, request, url_for, flash
from app.models.Guesser import Guesser
from app.forms.DataUserInputForm import DataUserInputForm

@app.route('/', methods=['GET'])
def index():
    template = render_template('index.html')

    return template

@app.route('/train', methods=['GET'])
def train():
    template = render_template('train.html')

    return template

@app.route('/guess/<string:type>', methods=['GET','POST'])
def guess(type, positive=None):
    template = 'error'
    if type == "user":
        form_user = DataUserInputForm()
        if form_user.validate_on_submit():
            flash('{}_tsé'.format(request.form.get('field_data_input')))
            print('form validated')
            return redirect(url_for('guess', type='user'))
        template = render_template('userInputForm.html', form=form_user, positive=positive)
    elif type == "twitter":
        template ='twitter'
    else:
        template = 'error'

    return template