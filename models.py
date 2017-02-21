from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

import date_transformer
import imputing_transformer
import column_extractor
import categorical_transformer
import cleanup_transformer
import ModelTransformer
import classification_model
import pandas_column_utilities

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

classification_model= reload(classification_model)

def run_logit(X_train, X_test, y_train, y_test):
    param_grid = [{'C':[0.001, 0.01,0.1,1],'penalty':['l1','l2']}]
    clf = GridSearchCV(LogisticRegression(), param_grid)
    clf.fit(X_train, y_train)

    print clf.best_param_

    mod1 = kfold_classification_model(clf)
    mod1.score(X_test, y_test)

def run_knn(X_train, X_test, y_train, y_test):
    param_grid = [
    {'n_neighbors':[3,5,7],'leaf_size':[5, 10,30,50,100]}]
    clf = GridSearchCV(KNeighborsClassifier(), param_grid)
    clf.fit(X_train, y_train)

    print clf.best_param_

    mod2 = kfold_classification_model(clf)
    mod2.score(X_test, y_test)



def run_randomforestclassifier(X_train, X_test, y_train, y_test):
    param_grid = [
    {'n_estimators':[5,10,20,30,50,100],'criterion':['entropy','gini'],'max_depth':[None, 2,5,10],
    'min_samples_split':[5,7,10,15], 'oob_score':[True, False]}]
    clf = GridSearchCV(RandomForestClassifier(), param_grid)
    clf.fit(X_train, y_train)

    print clf.best_param_

    mod2 = kfold_classification_model(clf)
    mod2.score(X_test, y_test)