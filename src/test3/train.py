import pandas as pd
import sklearn.ensemble as ske
from sklearn.model_selection import train_test_split
import joblib
import lightgbm as lgb

data = pd.read_csv('[test3]features.csv')
X = data.drop(['mal/benign','filename'], axis=1)
y = data['mal/benign']
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2)

model = ske.RandomForestClassifier()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print("%f %%" % (score*100))

# Save the algorithm and the feature list for later predictions
print('Saving algorithm and feature list in classifier directory...')
joblib.dump(model, 'classifier/model1.pkl')

#light gbm
#lgbm_train= lgb.Dataset(X_train, y_train)
#lgbm_eval = lgb.Dataset(X_test, y_test)
#lgbm_model = lgb.train({"application": "binary"}, lgbm_train, valid_sets=lgbm_eval, num_boost_round=209)
#y = lgbm_model.predict(X_test)
