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
import time

class ModelChooser:
    def __init__(self):
        self.models = app.config["MODELS"]

    def findBestModel(self, x, y):
        param_grid =  app.config["MODEL_PARAM_GRID"]
        self.best_name = ''
        self.score = 0
        for name, classifier in self.models.items():
            start_time = time.time()
            print("\ntryin' w/ classifier ", name, " at ", time.strftime("%H:%M:%S", time.gmtime(start_time)))
            score = cross_val_score(classifier, x, y, scoring='accuracy', cv=10).mean() #TODO use 'f1' score instead
            if score > self.score:
                self.best_score = float(score)
                self.best_name = name
            elapsed_time = time.time() - start_time
            print("elapsed time w/ classifier ", name, " is ", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), "with accuracy:", self.score, "\n")
        
        start_time = time.time()
        print("---\nthe best model is:", self.best_name, " at ", time.strftime("%H:%M:%S", time.gmtime(start_time)))
        grid_count = GridSearchCV(self.models[self.best_name], param_grid, scoring='accuracy', cv=10) #TODO use 'f1' score instead
        print("fittin' the model...")
        grid_count.fit(x, y)

        self.train_x = x
        self.train_y = y
        self.best_model = grid_count.best_estimator_
        self.best_score = float(grid_count.best_score_)
        elapsed_time = time.time() - start_time
        print("elapsed time w/ best model ", self.best_name, " is ", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), "with accuracy:", self.score)
        print("best params:", grid_count.best_params_, "\n")

    def saveBestModel(self, filename):
        self.best_model.fit(self.train_x, self.train_y)
        guesser = Guesser(self.best_model, self.best_score)
        joblib.dump(guesser, filename + '.guesser')

    def getScore(self):
        return self.best_score
    
    def getName(self):
        return self.best_name