import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def read_csv(file_path, has_header = True):
    with open(file_path) as f:
        if has_header: f.readline()
        data = []
        for line in f:
            line = line.strip().split(",")
            data.append([float(x) for x in line])
    return data

def write_csv(file_path, data):
    with open(file_path,"w") as f:
        for line in data: f.write(",".join(line) + "\n")

rawData = list(csv.DictReader(open('./spreadFluFeatures_singleDay.csv', 'rU')))
xAxisL = 'gotFlu'
yAxisL = 'interactions'
xAxis = []
yAxis = []
for rows in rawData:
	xAxis.append(rows[xAxisL])
	yAxis.append(rows[yAxisL])

#data = np.loadtxt('./spreadFluFeatures_singleDay.csv', delimiter=',', skiprows=1)
#print data[0][0]

fig = plt.figure()

ax1 = fig.add_subplot(1,1,1, axisbg='white')

plt.scatter(xAxis,yAxis)

plt.title('bla')
plt.ylabel(yAxisL)
plt.xlabel(xAxisL)
plt.show()