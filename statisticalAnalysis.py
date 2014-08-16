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

# Apply Unsupervised Nearest Neighbors
nbrs = NearestNeighbors(n_neighbors=2).fit(dataTrain, dataTest)
distances, indices = nbrs.kneighbors(data)
print(indices)
#print(distances)

# playing with plot
if False:
	xAxis = []
	yAxis = []
	for rows in indices:
		xAxis.append(rows[0])
		yAxis.append(rows[1])

	fig = plt.figure()

	ax1 = fig.add_subplot(1,1,1, axisbg='white')

	plt.scatter(xAxis, yAxis)

	plt.title('bla')
	#plt.ylabel(yAxisL)
	#plt.xlabel(xAxisL)
	plt.show()