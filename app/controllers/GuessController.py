import joblib
import builtins
import jsonpickle
import numpy as np
from app import app
from app.models.Guesser import Guesser
from sklearn.model_selection import cross_val_score
from app.forms.DataTwitterInputForm import DataTwitterInputForm
from app.models.DataInputTwitter import DataInputTwitter
from app.forms.DataUserInputForm import DataUserInputForm
from flask import render_template, redirect, request, session, url_for, flash, json

def loadGuesser(filename):
    return joblib.load(filename)
    
def getGuesserFromContext(json_txt):
    tolisted_guesser = jsonpickle.decode(json_txt)
    NoneType = type(None)
    primitive_type_names = (int, str, float, bool, type, object, NoneType, np.float64)
    builtin_type_names = tuple(filter(lambda x: not x.startswith('_'), dir(builtins)))

    getUntolistedGuesser([tolisted_guesser], [tolisted_guesser], (primitive_type_names + builtin_type_names))
    
    return tolisted_guesser

def getUntolistedGuesser(mother_object, tolisted_object, primitive_types):
    list_attributes = [x for x in dir(tolisted_object[0]) if not callable(getattr(tolisted_object[0], x))
                        and not x.startswith('__')
                        and not x.endswith('__')]

    for i in range(len(list_attributes)):
        attribute = tolisted_object[0].__getattribute__(list_attributes[i])
        tolisted_attributes = mother_object[0].tolisted_attributes
        tolisted_attribute_name = (tolisted_object[0].__class__.__name__ + '.' + list_attributes[i])
        if tolisted_attribute_name in tolisted_attributes:
            attribute = np.asarray(attribute)
            # tolisted_attributes.remove(tolisted_attribute_name)
            tolisted_object[0].__setattr__(list_attributes[i], attribute)
            # mother_object[0].__setattr__('tolisted_attributes', tolisted_attributes)
        elif type(attribute) not in primitive_types:
            getUntolistedGuesser(mother_object,[attribute], primitive_types)

@app.route('/guess/<string:typ>', methods=['GET'])
def guess(typ):
    template_name = 'inputForm'
    if typ == "user":
        form = DataUserInputForm(field_type_input='user')
        # if form_user.validate_on_submit():
        #     flash('{}{}'.format(guesser.getGuess(request.form.get('field_data_input')), request.form.get('field_data_input')))
            # return redirect(url_for('guess', type='user'))
    elif typ == "twitter":
        # twitter = DataInputTwitter()
        form = DataTwitterInputForm(field_type_input='twitter')
    
    guesser = loadGuesser('LogisticRegression.guesser')
    session_guesser = guesser.getSerializableSelf()
    session['guesser'] = session_guesser
    guesser = getGuesserFromContext(session_guesser)
    model = guesser.getModel()
    
    template = render_template(template_name + '.html', form=form, model_chooser_info = {
                                                                'name': model.__class__.__name__,
                                                                'score': guesser.score
                                                            })

    return template

@app.route('/result', methods=['POST'])
def getResult():
    # guesser = Guesser()
    # guesser = session.get('guesser', None)
    # guesser.loadGuesser('LogisticRegression.model')
    session_guesser = session.get('guesser', None)
    if session_guesser is None:
        input_text = "ERROR"
        input_status = "neg"
    else:
        guesser = getGuesserFromContext(session_guesser)
        input_type = request.form.get('field_type_input')
        input_text = request.form.get('field_data_input')
        if input_type == 'twitter':
            twitter = DataInputTwitter()
            input_text = twitter.getData(input_text)
        input_status = guesser.getGuess(input_text)

    return render_template('result.html', input_text=input_text, input_status=input_status)