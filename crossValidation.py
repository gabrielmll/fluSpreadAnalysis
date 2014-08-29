import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors.nearest_centroid import NearestCentroid

data = np.loadtxt('./spreadFluFeatures_singleDay.csv', delimiter=',', skiprows=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(data[:, 3:15], data[:, 2], test_size=0.25, random_state=0)

# ???
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)
print y_test
scores = cross_validation.cross_val_score(clf, data[:, 3:15], data[:, 2], cv=5)
print scores

# Nearest Neighbor
#nbrs = NearestNeighbors(n_neighbors=2).fit(X_train, y_train)

# NearestCentroid
clf = NearestCentroid().fit(X_train, y_train)
print clf.predict(X_test)
print y_test
print clf.score(X_test, y_test)