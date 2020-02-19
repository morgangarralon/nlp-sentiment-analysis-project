import builtins
import jsonpickle
import numpy as np
from app import app
from app.models.Guesser import Guesser
from sklearn.model_selection import cross_val_score
from app.forms.DataUserInputForm import DataUserInputForm
from flask import render_template, redirect, request, session, url_for, flash, json, g

def getGuesserFromContext(json_txt):
    tolisted_guesser = jsonpickle.decode(json_txt)
    NoneType = type(None)
    primitive_type_names = (int, str, float, bool, type, object, NoneType)
    builtin_type_names = tuple(filter(lambda x: not x.startswith('_'), dir(builtins)))

    getUntolistedGuesser([tolisted_guesser], [tolisted_guesser], (primitive_type_names + builtin_type_names))
    
    return tolisted_guesser

def getUntolistedGuesser(mother_object, tolisted_object, primitive_types):
    list_attributes = [x for x in dir(tolisted_object[0]) if not callable(getattr(tolisted_object[0], x))
                        and not x.startswith('__')
                        and not x.endswith('__')]

    for i, j in enumerate(list_attributes):
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
            
# @app.before_request
# def before_request():
#     print("this function will run once")
#     if 'guesser' not in session.keys():
#         guesser = Guesser()
#         guesser.loadGuesser('LogisticRegression.model')
#         context_guesser = guesser.getSerializableSelf()
#         g.guesser = context_guesser
#         session['guesser'] = context_guesser
#         print("executed once !!!")

@app.route('/guess/<string:type>', methods=['GET'])
def guess(type):
    template = 'error'
    if type == "user":
        form_user = DataUserInputForm()
        guesser = Guesser()
        guesser.loadGuesser('LogisticRegression.model')
        session_guesser = guesser.getSerializableSelf()
        session['guesser'] = session_guesser
        # guesser = Guesser()
        # guesser.loadGuesser('LogisticRegression.model')
        guesser = getGuesserFromContext(session_guesser)
        model = guesser.getModel()
        # session_guesser = guesser.getSerializableSelf()
        # session['guesser'] = session_guesser
        # session.modified = True
        
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
    # guesser = Guesser()
    # guesser = session.get('guesser', None)
    # guesser.loadGuesser('LogisticRegression.model')
    session_guesser = session.get('guesser', None)
    if session_guesser is None:
        input_text = "ERROR"
        input_status = "neg"
    else:
        guesser = getGuesserFromContext(session_guesser)
        input_text = request.form.get('field_data_input')
        input_status = guesser.getGuess(request.form.get('field_data_input'))

    return render_template('result.html', input_text=input_text, input_status=input_status)