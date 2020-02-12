from flask import Flask, render_template
import os

app = Flask(__name__)


app_config_file = os.getenv('APP_CONFIG_FILE', 'development')
if app_config_file == 'production':
    app.config.from_object('config.ConfigProduction')
else:
    app.config.from_object('config.ConfigDevelopment')
    
print('app_config_file variable:', app_config_file)