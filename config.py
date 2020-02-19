from sklearn.linear_model import LogisticRegression
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'
    WTF_CSRF_ENABLED = True
    DB_SERVER = '192.168.1.56'
    SECRET_KEY = os.urandom(32)
    WTF_CSRF_SECRET_KEY = os.urandom(32)
    MODEL_FOLDER = 'static/data/models/'
    MODELS = {
        'LR': LogisticRegression(max_iter=4000)
    }

    @property
    def DATABASE_URI(self):         # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)

class ConfigProduction(Config):
    DB_SERVER = '192.168.19.32'

class ConfigDevelopment(Config):
    DB_SERVER = 'localhost'
    DEBUG = True