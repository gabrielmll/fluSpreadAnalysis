import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

# Reading data to a list of dictionaries
#rawData = list(csv.DictReader(open('./spreadFluFeatures_singleDay.csv', 'rU')))

# Reading data to numpy array
data = np.loadtxt('./spreadFluFeatures_singleDay.csv', delimiter=',', skiprows=1)

# Split data to training[75%] and test[25%] sets
dataTrain, dataTest = train_test_split(data, test_size=0.25, random_state=66)

#nbrs = NearestNeighbors(n_neighbors=2).fit(data)
#distances, indices = nbrs.kneighbors(data)
#print(indices)
#print(distances)