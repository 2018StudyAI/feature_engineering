import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dst', help='predict file(csv)')
parser.add_argument('-s', '--src', help='label of testdataset(csv)')
args = parser.parse_args()

data = pd.read_csv(args.dst, names=['hash', 'y_pred'])
y_pred = data['y_pred']

label = pd.read_csv(args.src, names=['hash', 'y'])
y = label['y']

accuracy = accuracy_score(y, y_pred)
print( accuracy)
print("accuracy : %.0000f%%" % (np.round(accuracy, decimals=4)*100))