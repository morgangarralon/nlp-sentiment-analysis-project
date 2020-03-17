from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.urandom(32)
    # WTF_CSRF_SECRET_KEY = os.urandom(32)
    MODEL_FOLDER = 'static/data/models/'
    MODEL_PARAM_GRID = {'C': np.logspace(-4, 4, 20)}
    DATABASE_URL = os.environ['DATABASE_URL']
    TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
    TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
    TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
    TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
    MODELS = {
        'LR': LogisticRegression(max_iter=4000, class_weight='balanced', random_state=33),
        # 'GB': GradientBoostingClassifier(n_estimators=5000, learning_rate=1.0, max_features=2, max_depth=2, random_state=33),
        # 'DT': DecisionTreeClassifier(class_weight='balanced', random_state=33),
        # 'RF': RandomForestClassifier(class_weight='balanced', random_state=33),
        # 'KNN': KNeighborsClassifier(),
        # 'NB': GaussianNB(),
        # 'SVC': SVC(class_weight='balanced', kernel='linear')
    }

class ConfigProduction(Config):
    DB_SERVER = '192.168.19.32'
    APP_CONFIG_MODE = "prod"

class ConfigDevelopment(Config):
    APP_CONFIG_MODE = "dev"
    DB_SERVER = 'localhost'
    DEBUG = True