## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Visualising pairplot"""

import seaborn as sns
df = dataset.copy()
sns.pairplot(data=df)

"""## Encoding dependent variable"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

print(X_train)

print(y_train)

print(X_test)

print(y_test)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)

print(X_test)

"""## Training the Random Forest Classification model on the Training set"""

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

"""## Predicting a new result"""

print(classifier.predict(sc.transform([[31.6036, 11.7235, 2.5185, 0.5303, 0.3773, 26.2722, 23.8238, -9.9574, 6.3609, 205.261]])))

"""## Predicting the Test set results"""

y_pred = classifier.predict(X_test)

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""## Visualising predictions"""

import seaborn as sns
sns.countplot(y_pred, data=dataset)
plt.title('0 = g , 1 = h')
plt.xlabel('class')
plt.show()

"""## Visualising real values"""

sns.countplot(y_test,  data=dataset)
plt.title('0 = g , 1 = h')
plt.xlabel('class')
plt.show()

"""## Visualising ROC curve"""

from sklearn.metrics import roc_curve
from sklearn.preprocessing import binarize
for i in range(1,5):
    cm2=0
    y_pred_prob_yes=classifier.predict_proba(X_test)
    y_pred2=binarize(y_pred_prob_yes,i/10)[:,1]
    cm2=confusion_matrix(y_test,y_pred2)
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_yes[:,1])
plt.plot(fpr,tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('MAGIC Gamma Telescope (ROC-curve)')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.grid(True)

"""## ROC curve accuracy"""

from sklearn.metrics import roc_auc_score
roc_auc_score(y_test,y_pred_prob_yes[:,1])
