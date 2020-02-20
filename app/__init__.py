import os
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template

app = Flask(__name__)

app_config_file = os.getenv('APP_CONFIG_FILE', 'development')
if app_config_file == 'production':
    app.config.from_object('config.ConfigProduction')
else:
    app.config.from_object('config.ConfigDevelopment')

CSRFProtect(app)
Session(app)
    
print('___app_config_file variable:', app_config_file)