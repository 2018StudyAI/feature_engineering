import pandas as pd
import seaborn as sns

features_path = 'features.csv'

data = pd.read_csv(features_path)
X = data.drop(['filename', 'mal/benign'], axis=1)
y = data['mal/benign']

before_col = X.columns
print(before_col)

ax = sns.countplot(y, label="Count")
B, M = y.value_counts()
print("Number of malware: ", B)
print("Number of benign: ", M)

print(X.describe())