import pandas as pd
import sklearn.ensemble as ske
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import joblib
import lightgbm as lgb
import argparse
from sklearn.metrics import classification_report

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--feature', help='feature files')
parser.add_argument('-o', '--output', help='output file(pkl)')
args = parser.parse_args()

data = pd.read_csv(args.feature)
X = data.drop(['mal/benign','filename'], axis=1)
y = data['mal/benign']
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2)

# #default parameter
model = ske.RandomForestClassifier()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print("%f %%" % (score*100))

# GridSearch for randomforest
params = {
    'n_estimators': [1000, 1500, 2000, 2500],    
    'max_depth': [200, 230, 240],
}

print('start----------------------------')

grid = GridSearchCV(model, params, cv=3)
grid_model = grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

clf = grid_model.best_estimator_
score = clf.score(X_test, y_test)
print("%f %%" % (score*100))
print(classification_report(clf.predict(X_test), y_test))


# # GridSearch for lightgbm
# params = {
#     'verbosity': [0], 
#     'learning_rate': [0.15, 0.2],  #default 0.1
#     'num_leaves': [31, 47], #defaut 31
#     'bossting_type]': ['gbdt'],
#     'objective': ['binary'],
#     'max_bin': [127, 255], #default 255
#     'random_state': [501], #update from seed
#     'n_estimators': [2000]
# }

# #grid = lgb.LGBMClassifier(cv=3, verbose=10, n_jobs=-1)
# clf = lgb.LGBMClassifier()

# grid = GridSearchCV(clf, params, verbose=10, cv=3, n_jobs=-1)
# grid.fit(X_train, y_train)

# #print best params
# print(grid.best_params_)
# print(grid.best_score_)

# Save the algorithm and the feature list for later predictions
#print('Saving algorithm and feature list in classifier directory...')
#joblib.dump(model, args.output)

#light gbm
#lgbm_train= lgb.Dataset(X_train, y_train)
#lgbm_eval = lgb.Dataset(X_test, y_test)
#lgbm_model = lgb.train({"application": "binary"}, lgbm_train, valid_sets=lgbm_eval, num_boost_round=209)
#y = lgbm_model.predict(X_test)