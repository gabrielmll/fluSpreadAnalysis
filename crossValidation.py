import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.metrics import precision_score, recall_score, confusion_matrix

data = np.loadtxt('./spreadFluFeatures_singleDay.csv', delimiter=',', skiprows=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(data[:, 3:15], data[:, 2], test_size=0.25, random_state=0)

# ???
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf_y_pred = clf.predict(X_test)

clf_pr = precision_score(y_test,clf_y_pred)
clf_rc = recall_score(y_test,clf_y_pred)
clf_CM = confusion_matrix(y_test,clf_y_pred)

#print clf.score(X_test, y_test)
#print y_test
#scores = cross_validation.cross_val_score(clf, data[:, 3:15], data[:, 2], cv=5)
#print scores

# Nearest Neighbor
nbrs = KNeighborsClassifier(n_neighbors=2).fit(X_train, y_train)
nbrs_y_pred = nbrs.predict(X_test)
nbrs_pr = precision_score(y_test,nbrs_y_pred)
nbrs_rc = recall_score(y_test,nbrs_y_pred)
nbrs_CM = confusion_matrix(y_test,nbrs_y_pred)
print "------------------"
print "\tNearest Neighbor"
print "------------------"
print "Real: "
print y_test
print "Predict"
print nbrs_y_pred
print "Score:"
print nbrs_pr

# NearestCentroid
clf = NearestCentroid().fit(X_train, y_train)
print "------------------"
print "\tNearest Centroid"
print "------------------"
print "Real: "
print y_test
print "Predict"
print clf.predict(X_test)
print "Score: "
print clf.score(X_test, y_test)