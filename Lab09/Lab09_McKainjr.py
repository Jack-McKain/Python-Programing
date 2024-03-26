#N_estimator = 7 or 8 gives you the most accurate results of 98.76% fit

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Modify this to your file system
heart_disease = pd.read_csv('heart.csv')

#Create Feature Matrix
X = heart_disease.drop(['target'], axis=1)
Y = heart_disease['target']

#Choose the right model
clf = RandomForestClassifier(n_estimators=1)

#Fit Model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
clf.fit(X_train, Y_train)

#Make Predictions
y_pred = clf.predict(X_test)

#Evaluate Model
print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))

# My Output
# 0.987603305785124
# 0.8524590163934426

print(classification_report(Y_test, y_pred))
#print(confusion_matrix(Y_test, y_pred))
#print(accuracy_score(Y_test, y_pred))

#Improve Model
for i in range(1, 10):
  clf = RandomForestClassifier(n_estimators = i)
  clf.fit(X_train, Y_train)
  print(f"Trying n_estimators = {i}")
  print(f"Model score: {clf.score(X_train, Y_train) * 100}")
  print("")