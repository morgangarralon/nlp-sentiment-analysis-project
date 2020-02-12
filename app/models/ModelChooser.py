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
import flask, joblib

class ModelChooser:
    def __init__(self):
        self.models = {
            'LR': LogisticRegression(max_iter=4000),
            # 'GB': GradientBoostingClassifier(),
            # 'RF': RandomForestClassifier(),
            # 'NB': GaussianNB(),
            # 'SVC': SVC(max_iter=4000),
            # 'KNN': KNeighborsClassifier()
        }

    def findBestModel(self, x, y):
        param_grid = {'C': [0.1,1,10,100]}
        max_name_count = ''
        max_score = 0
        for name, classifier in self.models.items():
            score = cross_val_score(classifier, x, y, scoring='accuracy', cv=10).mean()
            if score > max_score:
                max_score = score
                max_name_count = name
        grid_count = GridSearchCV(self.models[max_name_count], param_grid, cv=10)
        grid_count.fit(x, y)

        self.train_x = x
        self.train_y = y
        self.best_model = grid_count.best_estimator_

    def saveBestModel(self, filename):
        self.best_model.fit(self.train_x, self.train_y)
        joblib.dump(self.best_model, filename + '.model')