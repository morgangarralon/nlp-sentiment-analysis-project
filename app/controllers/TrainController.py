from app import app
from flask import render_template

@app.route('/train', methods=['GET'])
def train():
    template = render_template('train.html')

    return template