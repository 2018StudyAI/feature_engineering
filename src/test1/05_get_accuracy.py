import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

data = pd.read_csv(r'C:\Users\kgg19\Documents\featureengineering\script\test1\result\output_not_selection.csv', names=['hash', 'y_pred'])
y_pred = data['y_pred']

label = pd.read_csv(r'C:\Users\kgg19\Documents\dataset\TestSet_final1_VX.csv', names=['hash', 'y'])
y = label['y']

accuracy = accuracy_score(y, y_pred)
print( accuracy)
print("accuracy : %.0000f%%" % (np.round(accuracy, decimals=4)*100))