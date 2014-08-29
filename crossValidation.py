import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

data = np.loadtxt('./spreadFluFeatures_singleDay.csv', delimiter=',', skiprows=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(data[:, 3:14], data[:, 2], test_size=0.25, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)