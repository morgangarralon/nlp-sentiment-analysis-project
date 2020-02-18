from app import app
from app.models.Guesser import Guesser
from sklearn.model_selection import cross_val_score
from app.forms.DataUserInputForm import DataUserInputForm
from flask import render_template, redirect, request, session, url_for, flash, json

@app.route('/guess/<string:type>', methods=['GET'])
def guess(type):
    template = 'error'
    if type == "user":
        form_user = DataUserInputForm()
        guesser = Guesser()
        guesser.loadGuesser('LogisticRegression.model')
        model = guesser.getModel()
        # guesser.getSerializableSelf()
        # session['guesser'] = guesser
        # session['guesser'] = json.dumps(guesser.__dict__)
        template = render_template('userInputForm.html', form=form_user, model_chooser_info = {
                                                                    'name': model.__class__.__name__
                                                                    # 'score': score
                                                                })
        # if form_user.validate_on_submit():
        #     flash('{}{}'.format(guesser.getGuess(request.form.get('field_data_input')), request.form.get('field_data_input')))
            # return redirect(url_for('guess', type='user'))
            # score = cross_val_score(model, x, y, scoring='accuracy', cv=10).mean()
    elif type == "twitter":
        template ='twitter'
    else:
        template = 'error'

    return template

@app.route('/result', methods=['POST'])
def getResult():
    # guesser = json.loads(session['guesser'])
    guesser = Guesser()
    guesser.loadGuesser('LogisticRegression.model')
    # guesser = session['guesser']
    
    if guesser is None:
        result = "ERROR"
    else:
        input_text = request.form.get('field_data_input')
        input_status = guesser.getGuess(request.form.get('field_data_input'))

    return render_template('result.html', input_text=input_text, input_status=input_status)