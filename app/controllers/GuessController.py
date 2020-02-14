from app import app
from flask import render_template, redirect, request, url_for, flash
from app.models.Guesser import Guesser
from app.forms.DataUserInputForm import DataUserInputForm

@app.route('/guess/<string:type>', methods=['GET','POST'])
def guess(type, positive=None):
    template = 'error'
    if type == "user":
        form_user = DataUserInputForm()
        if form_user.validate_on_submit():
            guesser = Guesser()
            guesser.loadGuesser('LogisticRegression.model')
            flash('{}{}'.format(guesser.getGuess(request.form.get('field_data_input')), request.form.get('field_data_input')))
            return redirect(url_for('guess', type='user', form=form_user))
        template = render_template('userInputForm.html', form=form_user, positive=positive)
    elif type == "twitter":
        template ='twitter'
    else:
        template = 'error'

    return template