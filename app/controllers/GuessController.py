from app import app
from app.models.Guesser import Guesser
from sklearn.model_selection import cross_val_score
from app.forms.DataUserInputForm import DataUserInputForm
from flask import render_template, redirect, request, url_for, flash

@app.route('/guess/<string:type>', methods=['GET'])
def guess(type, positive=None):
    template = 'error'
    if type == "user":
        form_user = DataUserInputForm()
        template = render_template('userInputForm.html', form=form_user, positive=positive)
        if form_user.validate_on_submit():
            guesser = Guesser()
            guesser.loadGuesser('LogisticRegression.model')
            model = guesser.getModel()
            flash('{}{}'.format(guesser.getGuess(request.form.get('field_data_input')), request.form.get('field_data_input')))
            # return redirect(url_for('guess', type='user'))
            # score = cross_val_score(model, x, y, scoring='accuracy', cv=10).mean()
            template = render_template('userInputForm.html', form=form_user, positive=positive, model_chooser_info = {
                                                                                                'name': type(model).__name__,
                                                                                                # 'score': score
                                                                                            })
    elif type == "twitter":
        template ='twitter'
    else:
        template = 'error'

    return template

@app.route('/result', methods=['POST'])
def getResult():
    guesser = Guesser()
    guesser.loadGuesser('LogisticRegression.model')
    list_result = [guesser.getGuess(request.form.get('field_data_input')), request.form.get('field_data_input')]
    result = ' '.join([str(elem) for elem in list_result])

    return result