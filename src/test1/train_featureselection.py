import pandas as pd
import sklearn.ensemble as ske
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
import joblib

data = pd.read_csv('[test2]features_dos_header_additional.csv')
X = data.drop(['filename', 'mal/benign'], axis=1)
y = data['mal/benign']

clf = ske.RandomForestClassifier()
trans = SelectFromModel(clf, threshold='median')
X_trans = trans.fit_transform(X, y)
print("We started with {0} features but retained only {1} of them!".format(X.shape[1] - 1, X_trans.shape[1]))

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2)
model = ske.RandomForestClassifier()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print("%f %%" % (score*100))

# Save the algorithm and the feature list for later predictions
print('Saving algorithm and feature list in classifier directory...')
joblib.dump(model, 'classifier/model2.pkl')