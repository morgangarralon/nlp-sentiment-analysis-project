from sklearn.metrics import f1_score, accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from app.models.Guesser import Guesser
import flask, joblib
from app import app

class ModelChooser:
    def __init__(self):
        self.models = app.config["MODELS"]

    def findBestModel(self, x, y):
        param_grid = {'C': [0.1,1,10,100]}
        self.name = ''
        self.score = 0
        for name, classifier in self.models.items():
            score = cross_val_score(classifier, x, y, scoring='accuracy', cv=10).mean()
            if score > self.score:
                self.score = float(score)
                self.name = name
        grid_count = GridSearchCV(self.models[self.name], param_grid, cv=10)
        grid_count.fit(x, y)

        self.train_x = x
        self.train_y = y
        self.best_model = grid_count.best_estimator_

    def saveBestModel(self, filename):
        self.best_model.fit(self.train_x, self.train_y)
        guesser = Guesser(self.best_model, self.score)
        joblib.dump(guesser, filename + '.guesser')

    def getScore(self):
        return self.score
    
    def getName(self):
        return self.name