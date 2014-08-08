# Preprocess for statistical analysis
# data output format:
#	date[yyyymmdd], id[1-80], gotFlu[0-1], numOfInteractions, fluInteractions, healthInteractions,

import csv
import datetime, time

# This is to measure the running time. It has nothing to do with the whole algorithm
startTime = time.time()

# Function to increment one day
def incrementOneDay( d ):
	date = datetime.datetime.strptime(str(d), "%Y%m%d");
	date += datetime.timedelta(days=1);
	return date.strftime("%Y%m%d");

# Variables to manage days
current_day = 20090109;
#historical_threshold = -3;	# This doesn't matter for now, once I'm doing a file for each day

# Opening files
proximityFile = open('Proximity.csv', 'rb');
fluFile = open('FluSymptoms.csv', 'rb');
outputFile = open('output.csv', 'wb');

try:
	# csv reader objects
	proximityReader = csv.reader(proximityFile);
	fluReader = csv.reader(fluFile);
	w = csv.writer(outputFile, delimiter=',');
	
	# output File header
	w.writerows([['date','id','gotFlu','interactions']])

	while int(current_day) != 20090119:
		# skip the headers
		next(proximityReader, None);
		next(fluFile, None);

		print "---------------"
		print "Date "+str(current_day)
		# Output variables
		numOfInteractions = [0] * 81
		anyFluSymp = [0] * 81

		# each row of the fluSymptom file
		for row in fluReader:
			# Formatting dates
			proximityDate = long(row[1].replace("-", "").replace(":", "").replace(" ", ""))
			proximityDate = proximityDate/1000000 # remove hhmmss

			# for this day, compute the symptoms
			# The reason Flu is being analysed first is that after we can easily check the amount of flu interactions
			if proximityDate == int(current_day):
				if row[2] == '1' or row[3] == '1' or row[4] == '1' or row[5] == '1':
					anyFluSymp[int(row[0])] = 1

		# each row of the proximity file
		for row in proximityReader:
			# Formatting dates
			proximityDate = long(row[2].replace("-", "").replace(":", "").replace(" ", ""))
			proximityDate = proximityDate/1000000 # remove hhmmss

			# for this day, compute the number of interactions
			if proximityDate == int(current_day):
				numOfInteractions[int(row[0])]+=1
				numOfInteractions[int(row[1])]+=1

		# pop the 0ith array position
		numOfInteractions.pop(0)
		anyFluSymp.pop(0)
		for i in range(len(numOfInteractions)):
			w.writerow([current_day, i+1, anyFluSymp[i], numOfInteractions[i]]);

		current_day = incrementOneDay( current_day );
		proximityFile.seek(0);
		fluFile.seek(0);

except ValueError, e:
	print "Error ", e

finally:
	proximityFile.close()
	fluFile.close()

# This is to measure the running time. It has nothing to do with the whole algorithm
endTime = time.time() - startTime;
print(endTime);