# from ...app import app # with 'flask run' command
from app import app # with Visual Studio Code
from app import app
from flask import render_template

@app.route('/api', methods=['GET'])
def api():
    template = render_template('api.html')

    return template