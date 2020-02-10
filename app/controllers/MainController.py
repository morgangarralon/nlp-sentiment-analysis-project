# from ...app import app # with 'flask run' command
from app import app # with Visual Studio Code
from flask import render_template
from app.models.Guesser import Guesser
from app.forms.DataUserInputForm import DataUserInputForm

@app.route('/', methods=['GET'])
def index():
    return "Hello World!"

@app.route('/train', methods=['GET'])
def train():
    return "train"

@app.route('/guess/<string:type>', methods=['GET'])
def guess(type):
    guesser = Guesser(type)
    if type == "user":
        form_user = DataUserInputForm()

        return render_template('UserInputForm.html', form=form_user)
    elif type == "twitter":
        print('twitter')
    else:
        print('error')

    return "guess"