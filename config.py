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
    DB_SERVER = '192.168.1.56'
    SECRET_KEY = os.urandom(32)
    # WTF_CSRF_SECRET_KEY = os.urandom(32)
    MODEL_FOLDER = 'static/data/models/'
    MODEL_PARAM_GRID = {'C': np.logspace(-4, 4, 20)}
    DATABASE_URL = "postgres://dlvfjyawlvxzlv:2b097d102248b8595c29d54d8713cae282f3e13da21d9f7d3a93faf965ef8a8d@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/deelvmnbkk1bh4"
    TWITTER_API_KEY = "x0HaExKYjbSwPrZowVWjRS9gW"
    TWITTER_API_SECRET = "ei2L80gwrebvWZ28o5P2GbpqntujBML1X8zEyEenLFsKgI0mId"
    TWITTER_ACCESS_TOKEN = "212573211-5fSf6stgeeCfFOY43aPnbNu52M9JdeMX5sZCaMQh"
    TWITTER_ACCESS_SECRET = "NP2xaRdzQdAyIFLLnVidJdtQ01MNYdZJAAXOHTMh5KYwf"
    MODELS = {
        'LR': LogisticRegression(max_iter=4000, class_weight='balanced', random_state=33),
        # 'GB': GradientBoostingClassifier(n_estimators=5000, learning_rate=1.0, max_features=2, max_depth=2, random_state=33),
        # 'DT': DecisionTreeClassifier(class_weight='balanced', random_state=33),
        # 'RF': RandomForestClassifier(class_weight='balanced', random_state=33),
        # 'KNN': KNeighborsClassifier(),
        # 'NB': GaussianNB(),
        # 'SVC': SVC(class_weight='balanced', kernel='linear')
    }

    @property
    def DATABASE_URI(self):
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)

class ConfigProduction(Config):
    DB_SERVER = '192.168.19.32'
    APP_CONFIG_MODE = "prod"

class ConfigDevelopment(Config):
    APP_CONFIG_MODE = "dev"
    DB_SERVER = 'localhost'
    DEBUG = True