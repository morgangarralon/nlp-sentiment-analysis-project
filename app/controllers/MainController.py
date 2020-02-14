# from ...app import app # with 'flask run' command
from app import app # with Visual Studio Code
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    template = render_template('index.html')

    return template